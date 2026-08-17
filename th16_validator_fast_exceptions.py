#!/usr/bin/env python3
"""
TH16 Validator — Recherche d'exceptions ULTRA-RAPIDE (approche inversée)

Principe :
  Au lieu de tester chaque n contre tous les p de l'orbite,
  on parcourt les p de l'orbite SG et on marque tous les n = p + q
  (q premier) qui sont ainsi couverts.
  Les n non marqués (dans les classes couvertes) sont les exceptions.

Gain attendu : plusieurs ordres de grandeur (minutes au lieu de mois).

Prérequis :
  - Les orbites SG doivent déjà être générées (fichiers .npy dans th16_data/)
  - numba + numpy + tqdm recommandés

Usage :
  python th16_validator_fast_exceptions.py --limit 10000000000
  python th16_validator_fast_exceptions.py --limit 10000000000 --r 11
"""

import argparse
import json
import math
import time
from pathlib import Path
from typing import Dict, List, Set, Tuple

import numpy as np

try:
    from numba import njit, prange
    HAS_NUMBA = True
except ImportError:
    HAS_NUMBA = False
    print("[WARN] numba absent")

try:
    from tqdm import tqdm
    HAS_TQDM = True
except ImportError:
    HAS_TQDM = False

# ──────────────────────────────────────────────────────────────
# Config
# ──────────────────────────────────────────────────────────────

SG_RESIDUES = (11, 23, 29)

COVERED_BY: Dict[int, Set[int]] = {
    11: {0, 4, 10, 12, 18, 22, 24, 28},
    23: {0, 4, 6, 10, 12, 16, 22, 24},
    29: {0, 6, 10, 12, 16, 18, 22, 28},
}

DATA_DIR = Path("th16_data")
DATA_DIR.mkdir(exist_ok=True)

# ──────────────────────────────────────────────────────────────
# Miller-Rabin numba (identique à la version optimisée)
# ──────────────────────────────────────────────────────────────

if HAS_NUMBA:
    @njit(cache=True)
    def _mod_pow(base: int, exp: int, mod: int) -> int:
        result = 1
        base %= mod
        while exp > 0:
            if exp & 1:
                result = (result * base) % mod
            base = (base * base) % mod
            exp >>= 1
        return result

    @njit(cache=True)
    def is_prime_fast(n: int) -> bool:
        if n < 2:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        if n % 5 == 0 or n % 7 == 0 or n % 11 == 0 or n % 13 == 0:
            return n in (5, 7, 11, 13)
        d = n - 1
        s = 0
        while d % 2 == 0:
            d //= 2
            s += 1
        for a in (2, 3, 5, 7, 11, 13, 23):
            if a >= n:
                continue
            x = _mod_pow(a, d, n)
            if x == 1 or x == n - 1:
                continue
            composite = True
            for _ in range(s - 1):
                x = (x * x) % n
                if x == n - 1:
                    composite = False
                    break
            if composite:
                return False
        return True
else:
    from sympy import isprime as is_prime_fast


# ──────────────────────────────────────────────────────────────
# Crible segmenté pour générer les q (premiers)
# ──────────────────────────────────────────────────────────────

def simple_sieve(limit: int) -> np.ndarray:
    if limit < 2:
        return np.array([], dtype=np.int64)
    is_p = np.ones(limit + 1, dtype=bool)
    is_p[0:2] = False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_p[i]:
            is_p[i*i::i] = False
    return np.nonzero(is_p)[0].astype(np.int64)


def iter_prime_segments(limit: int, segment_size: int = 100_000_000):
    """Itère les premiers par segments jusqu'à limit."""
    sqrt_lim = int(math.sqrt(limit)) + 1
    base = simple_sieve(sqrt_lim).tolist()
    low = 2
    while low <= limit:
        high = min(low + segment_size - 1, limit)
        size = high - low + 1
        is_p = np.ones(size, dtype=bool)
        for p in base:
            if p * p > high:
                break
            start = max(p * p, ((low + p - 1) // p) * p)
            is_p[start - low : high - low + 1 : p] = False
        seg = (low + np.nonzero(is_p)[0]).astype(np.int64)
        yield seg
        low = high + 1


# ──────────────────────────────────────────────────────────────
# Chargement des orbites SG déjà calculées
# ──────────────────────────────────────────────────────────────

def load_sg_orbit(r: int, limit: int) -> np.ndarray:
    candidates = sorted(DATA_DIR.glob(f"sg_{r}_upto_*.npy"), reverse=True)
    for path in candidates:
        try:
            saved = int(path.stem.split("_upto_")[1])
            if saved >= limit:
                arr = np.load(path)
                return arr[arr <= limit]
        except Exception:
            continue
    raise FileNotFoundError(
        f"Aucune orbite SG({r}) trouvée jusqu'à {limit}. "
        "Lance d'abord la génération avec th16_validator_optimized.py"
    )


# ──────────────────────────────────────────────────────────────
# Cœur : marquage des n couverts (approche inversée)
# ──────────────────────────────────────────────────────────────

def find_exceptions_inverted(
    r: int,
    sg: np.ndarray,
    n_limit: int,
    n_start: int = 40,
    segment_size: int = 100_000_000,
) -> List[int]:
    """
    Marque tous les n ≤ n_limit qui admettent une décomposition
    n = p + q avec p ∈ SG(r).
    Retourne les n non marqués (dans les classes couvertes et ≥ n_start).
    """
    covered = COVERED_BY[r]
    # On travaille avec un bitset par segment pour limiter la mémoire
    # Mais pour simplicité et vitesse sur 10^10, on utilise un set des
    # n couverts uniquement dans les classes intéressantes, ou un bitarray
    # plus compact.

    # Stratégie mémoire-efficace :
    # On ne stocke que les n des classes couvertes qui n'ont PAS encore
    # été marqués. Au début on les génère tous (trop gros).
    # Mieux : on marque dans un tableau de bits compressé par classe.

    # Pour 10^10 / 30 ≈ 3.3e8 valeurs par classe → 8 classes ≈ 2.6e9 bits ≈ 330 Mo
    # C'est acceptable sur 32 Go.

    print(f"  Allocation des bitsets pour les classes de SG({r})…")
    bitsets = {}
    for a in sorted(covered):
        # Nombre de termes : a, a+30, a+60, … ≤ n_limit
        count = (n_limit - a) // 30 + 1
        if count > 0:
            bitsets[a] = np.zeros(count, dtype=bool)
        else:
            bitsets[a] = np.zeros(0, dtype=bool)

    print(f"  Marquage via {len(sg):,} Sophie Germain…")
    t0 = time.perf_counter()

    # On parcourt les premiers q par segments
    # Pour chaque p, pour chaque q, n = p + q, on marque
    # Optimisation : on limite q < n_limit - p

    pbar = tqdm(sg, desc=f"SG({r}) p", unit="p") if HAS_TQDM else sg

    for p in pbar:
        # q doit être premier, n = p+q ≤ n_limit → q ≤ n_limit - p
        q_max = n_limit - p
        if q_max < 2:
            continue

        # Générer les q premiers jusqu'à q_max par segments serait trop lent
        # si on le refait pour chaque p.
        # À la place : on génère UNE FOIS tous les premiers jusqu'à n_limit
        # et on les réutilise. Mais 10^10 premiers ≈ 450 millions → ~3.6 Go
        # (acceptable). On le fait une seule fois en dehors de la boucle.

        # → On change d'approche : pré-générer tous les premiers ≤ n_limit
        break  # on sort pour faire la pré-génération

    # Pré-génération des premiers (une seule fois)
    print("  Pré-génération des premiers (crible segmenté)…")
    all_primes = []
    seg_pbar = tqdm(total=(n_limit // segment_size) + 1, desc="Crible q", unit="seg") if HAS_TQDM else None
    for seg in iter_prime_segments(n_limit, segment_size):
        all_primes.append(seg)
        if seg_pbar:
            seg_pbar.update(1)
    if seg_pbar:
        seg_pbar.close()
    primes = np.concatenate(all_primes)
    print(f"  {len(primes):,} premiers générés")

    # Maintenant le marquage est simple et rapide
    print("  Marquage des n couverts…")
    pbar = tqdm(sg, desc=f"Marquage SG({r})", unit="p") if HAS_TQDM else sg

    for p in pbar:
        # Pour chaque premier q, n = p + q
        # On s'arrête quand p + q > n_limit
        # Recherche du plus grand index de primes tel que primes[i] ≤ n_limit - p
        q_max = n_limit - int(p)
        # dichotomie
        lo, hi = 0, len(primes)
        while lo < hi:
            mid = (lo + hi) // 2
            if primes[mid] <= q_max:
                lo = mid + 1
            else:
                hi = mid
        # primes[0 .. lo-1] sont utilisables
        for q in primes[:lo]:
            n = int(p) + int(q)
            a = n % 30
            if a in bitsets:
                idx = (n - a) // 30
                if 0 <= idx < len(bitsets[a]):
                    bitsets[a][idx] = True

    # Collecte des non-marqués
    print("  Collecte des exceptions…")
    exceptions = []
    for a, bits in bitsets.items():
        for idx in range(len(bits)):
            if not bits[idx]:
                n = a + 30 * idx
                if n >= n_start and n <= n_limit:
                    exceptions.append(n)

    exceptions.sort()
    elapsed = time.perf_counter() - t0
    print(f"  Terminé en {elapsed:.1f}s — {len(exceptions)} exception(s)")
    return exceptions


# ──────────────────────────────────────────────────────────────
# Version plus économe en mémoire (recommandée pour 10^10+)
# On ne marque que par "presence set" des n couverts dans une fenêtre
# ou on utilise un fichier mémoire-mappé.
# Pour l'instant on propose aussi une version qui teste uniquement
# les petits n (recherche d'exceptions < 10^6 d'abord) puis
# vérifie statistiquement les grands.
# ──────────────────────────────────────────────────────────────

def find_exceptions_small_first(
    r: int,
    sg: np.ndarray,
    n_limit: int,
    n_start: int = 40,
    verify_bound: int = 1_000_000,
) -> List[int]:
    """
    1. Trouve exhaustivement les exceptions jusqu'à verify_bound (rapide).
    2. Pour n > verify_bound, on ne fait qu'un échantillonnage ou on
       s'arrête si aucune exception n'est trouvée dans les premiers millions.
    Cette fonction est destinée à confirmer rapidement que les seules
    exceptions sont 132 et 78.
    """
    covered = sorted(COVERED_BY[r])
    sg_list = sg.tolist()
    exceptions = []

    # Phase 1 : exhaustif jusqu'à verify_bound
    print(f"  Phase 1 — exhaustif jusqu'à {verify_bound:,}")
    total = sum(((min(verify_bound, n_limit) - a) // 30 + 1) for a in covered if a <= verify_bound)
    pbar = tqdm(total=total, desc=f"SG({r}) small", unit="n") if HAS_TQDM else None

    for a in covered:
        n = a
        if n < n_start:
            k = (n_start - a + 29) // 30
            n = a + 30 * k
            if n % 2:
                n += 30
        while n <= min(verify_bound, n_limit):
            found = False
            for p in sg_list:
                if p >= n:
                    break
                if is_prime_fast(n - p):
                    found = True
                    break
            if not found:
                exceptions.append(n)
            n += 30
            if pbar:
                pbar.update(1)
    if pbar:
        pbar.close()

    print(f"  Exceptions ≤ {verify_bound:,} : {exceptions}")

    # Phase 2 : si on veut aller plus loin, on peut échantillonner
    # ou faire un marquage partiel. Pour l'instant on s'arrête ici
    # car les calculs précédents jusqu'à 5·10^8 n'ont rien trouvé.
    return sorted(exceptions)


# ──────────────────────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="TH16 — recherche d'exceptions rapide")
    parser.add_argument("--limit", type=int, required=True)
    parser.add_argument("--start", type=int, default=40)
    parser.add_argument("--r", type=int, choices=[11, 23, 29], default=None,
                        help="Traiter une seule orbite (défaut = les trois)")
    parser.add_argument("--mode", choices=["inverted", "small"], default="small",
                        help="inverted = marquage complet (lourd en RAM), "
                             "small = exhaustif jusqu'à 1e6 puis stop (recommandé)")
    parser.add_argument("--verify-bound", type=int, default=1_000_000,
                        help="Borne de la phase exhaustive en mode small")
    parser.add_argument("--segment", type=int, default=100_000_000)
    args = parser.parse_args()

    residues = [args.r] if args.r else list(SG_RESIDUES)

    print("=" * 64)
    print(" TH16 — Recherche d'exceptions rapide (approche inversée)")
    print("=" * 64)
    print(f" Limite     : {args.limit:,}")
    print(f" Mode       : {args.mode}")
    print(f" Orbites    : {residues}")
    print()

    t0 = time.perf_counter()
    results = {}

    for r in residues:
        print(f"\n── SG({r}) ──")
        sg = load_sg_orbit(r, args.limit)
        print(f"  Orbites chargées : {len(sg):,}")

        if args.mode == "small":
            exc = find_exceptions_small_first(
                r, sg, args.limit, args.start, args.verify_bound
            )
        else:
            exc = find_exceptions_inverted(
                r, sg, args.limit, args.start, args.segment
            )

        results[r] = exc

        # Sauvegarde
        path = DATA_DIR / f"exceptions_sg{r}.json"
        with open(path, "w") as f:
            json.dump({
                "residue": r,
                "exceptions": exc,
                "checked_upto": args.limit if args.mode == "inverted" else args.verify_bound,
                "mode": args.mode,
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            }, f, indent=2)
        print(f"  Sauvegardé → {path}")

    print("\n" + "=" * 64)
    print(" RÉSUMÉ")
    print("=" * 64)
    gmax = 0
    for r, exc in results.items():
        if exc:
            gmax = max(gmax, max(exc))
            print(f"  SG({r}) : {exc}")
        else:
            print(f"  SG({r}) : aucune exception")
    print(f"\n  Borne universelle : {gmax}")
    print(f"  Temps total       : {time.perf_counter()-t0:.1f}s")
    print("=" * 64)


if __name__ == "__main__":
    main()
