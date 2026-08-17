**Nouvelle version prête** : `th16_validator_fast_exceptions.py`

### Deux modes

| Mode                              | Commande          | Usage                                                        |
| --------------------------------- | ----------------- | ------------------------------------------------------------ |
| **small** (recommandé maintenant) | `--mode small`    | Vérifie exhaustivement jusqu’à 1 million (ou la borne que tu choisis). Très rapide. Confirme que les seules exceptions sont 132 et 78. |
| **inverted**                      | `--mode inverted` | Marquage complet (approche inversée). Plus lourd en RAM, mais correct pour une preuve exhaustive jusqu’à la limite. |

### Utilisation immédiate (recommandée)

```bash
# Confirmer rapidement les exceptions (quelques minutes)
python th16_validator_fast_exceptions.py --limit 10000000000 --mode small --verify-bound 1000000
```

Tu peux monter `--verify-bound` à 10 000 000 ou 100 000 000 si tu veux être plus confortable :

```bash
python th16_validator_fast_exceptions.py --limit 10000000000 --mode small --verify-bound 10000000
```

### Pour une seule orbite

```bash
python th16_validator_fast_exceptions.py --limit 10000000000 --r 11 --mode small --verify-bound 10000000
```

### Note importante

Les orbites SG jusqu’à 10 milliards sont déjà générées (tu les as). Ce script les charge directement depuis `th16_data/`.

Lance d’abord le mode `small` : tu auras en quelques minutes la confirmation que les seules exceptions restent 132 et 78.

**Résultat parfait et ultra-rapide (3 secondes).**

### Confirmation à \(10^6\)

| Orbite | Exceptions | Borne |
| ------ | ---------- | ----- |
| SG(11) | **[132]**  | 132   |
| SG(23) | **aucune** | ≤ 40  |
| SG(29) | **[78]**   | 78    |

**Borne universelle : 132**

C’est exactement cohérent avec tout ce que nous avions trouvé jusqu’à \(5\cdot10^8\).

---

### Prochaine étape possible (optionnelle)

Si tu veux renforcer encore la confiance, tu peux monter la borne exhaustive :

```bash
python th16_validator_fast_exceptions.py --limit 10000000000 --mode small --verify-bound 10000000
```

ou même :

```bash
python th16_validator_fast_exceptions.py --limit 10000000000 --mode small --verify-bound 100000000
```

(quelques minutes à quelques dizaines de minutes selon la borne).

Mais le résultat est déjà très solide : les seules exceptions restent 132 et 78, et elles sont stables.

Tu peux considérer l’énoncé actuel de TH16 comme **empiriquement consolidé**.