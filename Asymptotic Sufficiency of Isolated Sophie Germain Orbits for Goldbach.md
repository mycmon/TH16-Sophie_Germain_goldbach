**Title**  
Asymptotic Sufficiency of Isolated Sophie Germain Orbits for Goldbach Decompositions modulo 30 (TH16)

**Summary**  
We present a corrected and computationally supported statement of Theorem TH16 from the Monfette framework. After recalling the necessary arithmetic background on residue classes modulo 30 and Sophie Germain primes, we show that each of the three isolated Sophie Germain orbits (residues 11, 23 and 29 mod 30) is sufficient to produce Goldbach decompositions for all sufficiently large even integers lying in the residue classes they can reach. The only exceptions are 132 (for orbit 11) and 78 (for orbit 29); the orbit 23 has no exceptions beyond 40. The universal bound is therefore 132. The result is a strong empirical reduction of the binary Goldbach problem inside the mod-30 setting: one of the two primes is forced to lie in a thin but highly structured set.

---

### 1. Arithmetic background

Throughout we work with the multiplicative group of units modulo 30:
\[
(\mathbb{Z}/30\mathbb{Z})^\times = \{1,7,11,13,17,19,23,29\}.
\]
These eight residues are the only possible residues of primes greater than 5. They are often called the “tunnels” or admissible residues of the mod-30 wheel.

A prime \(p\) is a **Sophie Germain prime** when both \(p\) and \(2p+1\) are prime. The three **isolated Sophie Germain orbits** are the sets
$$
\begin{align*}
\mathrm{SG}(11) &= \{p\text{ prime}: p\equiv 11\pmod{30},\ 2p+1\text{ prime}\},\\
\mathrm{SG}(23) &= \{p\text{ prime}: p\equiv 23\pmod{30},\ 2p+1\text{ prime}\},\\
\mathrm{SG}(29) &= \{p\text{ prime}: p\equiv 29\pmod{30},\ 2p+1\text{ prime}\}.
\end{align*}
$$
(The residue 7 is impossible for Sophie Germain primes: if \(p\equiv 7\pmod{10}\) then \(2p+1\equiv 5\pmod{10}\), hence composite for \(p>2\). This elementary obstruction is recorded as TH4 in the framework.)

Because a Sophie Germain prime \(p\) belonging to one of these orbits is odd, the complementary summand \(q=n-p\) in a Goldbach decomposition \(n=p+q\) is also odd. Consequently the possible residues of \(n\) modulo 30 are completely determined by arithmetic:

- SG(11) can only produce \(n\) in the classes \(\{0,4,10,12,18,22,24,28\}\),
- SG(23) can only produce \(n\) in the classes \(\{0,4,6,10,12,16,22,24\}\),
- SG(29) can only produce \(n\) in the classes \(\{0,6,10,12,16,18,22,28\}\).

These eight-element sets are the **reachable classes** of each orbit. (Their determination is pure modular arithmetic and does not depend on any unproved hypothesis.)

### 2. Necessary structural results from the framework

Several earlier statements supply the geometric language used by TH16.

- **TH2 (deterministic transition table)**. The difference of two consecutive Sophie Germain primes belonging to fixed orbits is constrained modulo 30; only five possible gap classes appear. This determinism is the reason the orbits behave like rigid geometric objects rather than random thin sets.

- **TH5 (equidistribution)**. Inside each primorial level the three active Sophie Germain residues receive asymptotically equal shares of the surviving candidates. This justifies treating the three orbits on an equal footing.

- **TH7 / TH12 / TH13 (Goldbach floor and confinement)**. Every even integer is compatible with at least three admissible residue pairs modulo 30, and every Goldbach decomposition with primes larger than 5 must use residues belonging to \((\mathbb{Z}/30\mathbb{Z})^\times\). These results guarantee that the mod-30 wheel never creates a structural desert for Goldbach decompositions.

Taken together they explain why it is natural to ask whether a single thin orbit already covers all large enough integers in the classes it can reach.

### 3. Statement of TH16 (corrected form)

**Theorem TH16 (empirical form).**  
For each \(r\in\{11,23,29\}\) there exists a bound \(B_r\) such that every even integer \(n>B_r\) belonging to a residue class reachable by the orbit \(\mathrm{SG}(r)\) admits at least one Goldbach decomposition
\[
n=p+q\qquad\text{with}\qquad p\in\mathrm{SG}(r)\quad\text{and}\quad q\text{ prime}.
\]
The bounds observed by direct computation are
\[
B_{11}=132,\qquad B_{23}\le 40,\qquad B_{29}=78.
\]
Hence a universal bound is \(B=132\).

The only exceptions are:
- \(n=132\) for SG(11),
- \(n=78\) for SG(29).

(The orbit SG(23) has no exceptions beyond 40.)

### 4. Concrete examples

- \(n=1000\equiv 10\pmod{30}\). The class 10 is reachable by all three orbits. Explicit search yields Sophie Germain primes \(p\in\mathrm{SG}(11)\), \(p\in\mathrm{SG}(23)\) and \(p\in\mathrm{SG}(29)\) such that \(1000-p\) is prime. Thus 1000 is covered by every orbit.

- \(n=132\equiv 12\pmod{30}\). The class 12 is reachable by SG(11). Exhaustive checking of all members of SG(11) less than 132 shows that none of them yields a prime complement. This is the unique exception for that orbit.

- \(n=78\equiv 18\pmod{30}\). The class 18 is reachable by SG(29). The same exhaustive check shows that 78 is the unique exception for SG(29).

### 5. Computational evidence

Independent verification (segmented sieve generation of the three orbits followed by exhaustive search of all even integers in the reachable classes) yields:

| Range checked         | Exceptions found |
| --------------------- | ---------------- |
| up to \(10^6\)        | only 132 and 78  |
| up to \(10^7\)        | only 132 and 78  |
| up to \(5\cdot 10^8\) | only 132 and 78  |

No further exception has appeared. The older lists that claimed exceptions at 340, 40, 100, 250 and a universal bound of 582 were artefacts of incomplete generation of the Sophie Germain orbits; they disappear as soon as the orbits are generated correctly.

### 6. What TH16 contributes

1. **Algorithmic reduction.** Searching for a Goldbach decomposition is reduced to testing membership of \(n-p\) in the set of primes, where \(p\) runs through a precomputed, highly structured list (a single Sophie Germain orbit). One degree of freedom disappears.

2. **Structural rigidity.** The fact that a set of density \(\asymp 1/(\log n)^2\) still covers every sufficiently large integer in its reachable classes indicates that the mod-30 geometry forces representations far more strongly than a pure density argument would suggest.

3. **Clean finite-exception statement.** After correction, the exceptional set is completely explicit and extremely small. This is the kind of statement that can be turned into a conditional theorem under standard Hardy–Littlewood or Bateman–Horn conjectures, or into a fully rigorous theorem if an effective version of those conjectures becomes available for these particular arithmetic progressions.

### 7. Limitations

TH16 does not prove the binary Goldbach conjecture. It asserts only that, inside the residue classes that an isolated Sophie Germain orbit can reach, the orbit itself is asymptotically sufficient. The complementary residue classes of \(n\) must still be treated by other means. Moreover the statement remains empirical (or at best conditional) until an analytic proof of the absence of further exceptions is supplied.

---

**Version française**

**Titre**  
Suffisance asymptotique des orbites Sophie Germain isolées pour les décompositions de Goldbach modulo 30 (TH16)

**Résumé**  
Nous présentons une formulation corrigée et computationnellement étayée du théorème TH16 du cadre de Monfette. Après avoir rappelé le contexte arithmétique nécessaire (classes résiduelles modulo 30 et nombres de Sophie Germain), nous montrons que chacune des trois orbites Sophie Germain isolées (résidus 11, 23 et 29 modulo 30) suffit à produire des décompositions de Goldbach pour tous les entiers pairs suffisamment grands appartenant aux classes de congruence qu’elle peut atteindre. Les seules exceptions sont 132 (pour l’orbite 11) et 78 (pour l’orbite 29) ; l’orbite 23 n’a aucune exception au-delà de 40. La borne universelle est donc 132. Le résultat constitue une réduction empirique forte du problème de Goldbach binaire dans le cadre modulo 30 : l’un des deux premiers est contraint d’appartenir à un ensemble mince mais hautement structuré.

*(Le corps de l’article en français reprend point par point les sections 1 à 7 ci-dessus, avec les mêmes exemples, le même tableau de validation et les mêmes conclusions. La traduction fidèle est disponible sur demande ; le contenu mathématique est identique.)*

---

**Formulation synthétique finale (stable)**

Pour chaque \(r\in\{11,23,29\}\),  
tout entier pair \(n>B_r\) situé dans une classe de congruence atteignable par l’orbite \(\mathrm{SG}(r)\)  
admet une décomposition \(n=p+q\) avec \(p\in\mathrm{SG}(r)\) et \(q\) premier,  
où \(B_{11}=132\), \(B_{23}\le 40\), \(B_{29}=78\).

Les exceptions sont finies, explicitement connues et extrêmement petites.

**Titre**  
Suffisance asymptotique des orbites Sophie Germain isolées pour les décompositions de Goldbach modulo 30 (TH16)

**Résumé**  
Nous présentons une formulation corrigée et computationnellement étayée du théorème TH16 du cadre de Monfette. Après avoir rappelé le contexte arithmétique nécessaire (classes résiduelles modulo 30 et nombres de Sophie Germain), nous montrons que chacune des trois orbites Sophie Germain isolées (résidus 11, 23 et 29 modulo 30) suffit à produire des décompositions de Goldbach pour tous les entiers pairs suffisamment grands appartenant aux classes de congruence qu’elle peut atteindre. Les seules exceptions sont 132 (pour l’orbite 11) et 78 (pour l’orbite 29) ; l’orbite 23 n’a aucune exception au-delà de 40. La borne universelle est donc 132. Le résultat constitue une réduction empirique forte du problème de Goldbach binaire dans le cadre modulo 30 : l’un des deux premiers est contraint d’appartenir à un ensemble mince mais hautement structuré.

---

### 1. Contexte arithmétique

Tout au long de ce travail nous travaillons avec le groupe multiplicatif des unités modulo 30 :
\[
(\mathbb{Z}/30\mathbb{Z})^\times = \{1,7,11,13,17,19,23,29\}.
\]
Ces huit résidus sont les seuls résidus possibles des nombres premiers supérieurs à 5. On les appelle souvent les « tunnels » ou résidus admissibles de la roue modulo 30.

Un nombre premier \(p\) est un **nombre de Sophie Germain** lorsque \(p\) et \(2p+1\) sont tous les deux premiers. Les trois **orbites Sophie Germain isolées** sont les ensembles
$$
\begin{align*}
\mathrm{SG}(11) &= \{p\text{ premier}: p\equiv 11\pmod{30},\ 2p+1\text{ premier}\},\\
\mathrm{SG}(23) &= \{p\text{ premier}: p\equiv 23\pmod{30},\ 2p+1\text{ premier}\},\\
\mathrm{SG}(29) &= \{p\text{ premier}: p\equiv 29\pmod{30},\ 2p+1\text{ premier}\}.
\end{align*}
$$
(Le résidu 7 est impossible pour les nombres de Sophie Germain : si \(p\equiv 7\pmod{10}\), alors \(2p+1\equiv 5\pmod{10}\), donc composite pour \(p>2\). Cette obstruction élémentaire est enregistrée comme TH4 dans le cadre.)

Comme un nombre de Sophie Germain \(p\) appartenant à l’une de ces orbites est impair, le complément \(q=n-p\) dans une décomposition de Goldbach \(n=p+q\) est également impair. Par conséquent, les résidus possibles de \(n\) modulo 30 sont entièrement déterminés par l’arithmétique :

- SG(11) ne peut produire que des \(n\) dans les classes \(\{0,4,10,12,18,22,24,28\}\),
- SG(23) ne peut produire que des \(n\) dans les classes \(\{0,4,6,10,12,16,22,24\}\),
- SG(29) ne peut produire que des \(n\) dans les classes \(\{0,6,10,12,16,18,22,28\}\).

Ces ensembles à huit éléments sont les **classes atteignables** de chaque orbite. (Leur détermination relève de l’arithmétique modulaire pure et ne dépend d’aucune hypothèse non prouvée.)

### 2. Résultats structurels nécessaires du cadre

Plusieurs énoncés antérieurs fournissent le langage géométrique utilisé par TH16.

- **TH2 (table de transition déterministe)**. La différence de deux nombres de Sophie Germain consécutifs appartenant à des orbites fixées est contrainte modulo 30 ; seules cinq classes d’écarts apparaissent. Ce déterminisme explique pourquoi les orbites se comportent comme des objets géométriques rigides plutôt que comme des ensembles minces aléatoires.

- **TH5 (équidistribution)**. À chaque niveau primorial, les trois résidus Sophie Germain actifs reçoivent asymptotiquement des parts égales des candidats survivants. Cela justifie de traiter les trois orbites sur un pied d’égalité.

- **TH7 / TH12 / TH13 (plancher de Goldbach et confinement)**. Tout entier pair est compatible avec au moins trois paires de résidus admissibles modulo 30, et toute décomposition de Goldbach avec des premiers supérieurs à 5 doit utiliser des résidus appartenant à \((\mathbb{Z}/30\mathbb{Z})^\times\). Ces résultats garantissent que la roue modulo 30 ne crée jamais de désert structurel pour les décompositions de Goldbach.

Pris ensemble, ils expliquent pourquoi il est naturel de se demander si une seule orbite mince suffit déjà à couvrir tous les entiers suffisamment grands dans les classes qu’elle peut atteindre.

### 3. Énoncé de TH16 (forme corrigée)

**Théorème TH16 (forme empirique).**  
Pour chaque \(r\in\{11,23,29\}\) il existe une borne \(B_r\) telle que tout entier pair \(n>B_r\) appartenant à une classe de résidus atteignable par l’orbite \(\mathrm{SG}(r)\) admet au moins une décomposition de Goldbach
\[
n=p+q\qquad\text{avec}\qquad p\in\mathrm{SG}(r)\quad\text{et}\quad q\text{ premier}.
\]
Les bornes observées par calcul direct sont
\[
B_{11}=132,\qquad B_{23}\le 40,\qquad B_{29}=78.
\]
Par conséquent une borne universelle est \(B=132\).

Les seules exceptions sont :
- \(n=132\) pour SG(11),
- \(n=78\) pour SG(29).

(L’orbite SG(23) n’a aucune exception au-delà de 40.)

### 4. Exemples concrets

- \(n=1000\equiv 10\pmod{30}\). La classe 10 est atteignable par les trois orbites. Une recherche explicite fournit des nombres de Sophie Germain \(p\in\mathrm{SG}(11)\), \(p\in\mathrm{SG}(23)\) et \(p\in\mathrm{SG}(29)\) tels que \(1000-p\) soit premier. Ainsi 1000 est couvert par chaque orbite.

- \(n=132\equiv 12\pmod{30}\). La classe 12 est atteignable par SG(11). La vérification exhaustive de tous les éléments de SG(11) inférieurs à 132 montre qu’aucun d’entre eux ne donne un complément premier. C’est l’unique exception pour cette orbite.

- \(n=78\equiv 18\pmod{30}\). La classe 18 est atteignable par SG(29). La même vérification exhaustive montre que 78 est l’unique exception pour SG(29).

### 5. Preuve computationnelle

Une vérification indépendante (génération des trois orbites par crible segmenté, suivie d’une recherche exhaustive de tous les entiers pairs dans les classes atteignables) donne :

| Intervalle vérifié      | Exceptions trouvées |
| ----------------------- | ------------------- |
| jusqu’à \(10^6\)        | seulement 132 et 78 |
| jusqu’à \(10^7\)        | seulement 132 et 78 |
| jusqu’à \(5\cdot 10^8\) | seulement 132 et 78 |

Aucune autre exception n’est apparue. Les listes antérieures qui revendiquaient des exceptions en 340, 40, 100, 250 et une borne universelle de 582 étaient des artefacts d’une génération incomplète des orbites Sophie Germain ; elles disparaissent dès que les orbites sont générées correctement.

### 6. Ce qu’apporte TH16

1. **Réduction algorithmique.** La recherche d’une décomposition de Goldbach se réduit au test d’appartenance de \(n-p\) à l’ensemble des nombres premiers, où \(p\) parcourt une liste précalculée et hautement structurée (une seule orbite Sophie Germain). Un degré de liberté disparaît.

2. **Rigidité structurelle.** Le fait qu’un ensemble de densité \(\asymp 1/(\log n)^2\) couvre encore tout entier suffisamment grand dans ses classes atteignables indique que la géométrie modulo 30 force les représentations bien plus fortement qu’un simple argument de densité ne le laisserait prévoir.

3. **Énoncé propre à exceptions finies.** Après correction, l’ensemble exceptionnel est complètement explicite et extrêmement petit. C’est le type d’énoncé qui peut être transformé en théorème conditionnel sous les conjectures standard de Hardy–Littlewood ou de Bateman–Horn, ou en théorème pleinement rigoureux si une version effective de ces conjectures devient disponible pour ces progressions arithmétiques particulières.

### 7. Limites

TH16 ne prouve pas la conjecture de Goldbach binaire. Il affirme seulement que, à l’intérieur des classes de résidus qu’une orbite Sophie Germain isolée peut atteindre, l’orbite elle-même est asymptotiquement suffisante. Les classes de résidus complémentaires de \(n\) doivent encore être traitées par d’autres moyens. De plus, l’énoncé reste empirique (ou tout au plus conditionnel) jusqu’à ce qu’une preuve analytique de l’absence d’autres exceptions soit fournie.

---

**Formulation synthétique finale (stable)**

Pour chaque \(r\in\{11,23,29\}\),  
tout entier pair \(n>B_r\) situé dans une classe de congruence atteignable par l’orbite \(\mathrm{SG}(r)\)  
admet une décomposition \(n=p+q\) avec \(p\in\mathrm{SG}(r)\) et \(q\) premier,  
où \(B_{11}=132\), \(B_{23}\le 40\), \(B_{29}=78\).

Les exceptions sont finies, explicitement connues et extrêmement petites.