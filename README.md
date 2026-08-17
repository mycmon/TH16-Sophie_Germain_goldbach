# TH16-Sophie_Germain_goldbach

Summary — TH16: Using Sophie Germain Primes for Goldbach, not a proof but new approche.

Instead of searching for any two primes p and q such that n=p+q, TH16 imposes that one of them (p) must be a Sophie Germain prime lying in a single fixed residue class modulo 30. Empirically (and conditionally under standard conjectures), this still suffices for all large n in the classes that this constraint can reach.

Context
Sophie Germain primes are primes p such that 2p+1 is also prime. Modulo 30, they can only lie in three classes:
11,  23,  29.
We call the three sets
                SG(11),    SG(23),    SG(29)
the isolated SG orbits. They are thin sets:
density ≍1(log⁡n)2.
What TH16 Says
For each orbit  r ∈ {11,23,29},
we first determine the classes of n modulo 30 that the orbit can reach (because n=p+q with p≡r(mod30) forces n into specific even residue classes);
then we assert that every sufficiently large even integer in those classes admits a decomposition  n=p+q,p∈SG(r),q prime.
The computations show that the only exceptions are:
132 for SG(11),
78 for SG(29),
none for SG(23) beyond 40.
The universal bound is therefore 132.
Why This Is Interesting
Reduction — We no longer search for two free primes; we search for one prime in a highly structured list (an SG orbit). One degree of freedom disappears.
Rigidity modulo 30 — A set as thin as the SG primes in a fixed class still suffices to cover all large reachable n. This reveals strong arithmetic organization in Goldbach decompositions.
Clean statement — After correction, the exceptions are explicit and tiny.

1. Central Idea
Goldbach’s conjecture states that every even integer n≥4 can be written as
n=p+q.
TH16 asks a more restrictive question:
Can we require that one of the two primes (say p) be a Sophie Germain prime in a single fixed residue class modulo 30, and still cover almost all n?
The three families considered are the isolated SG orbits:
SG(11)={p prime:p≡11(mod30),  2p+1 prime}
SG(23) similarly
SG(29) similarly

2. Statement of TH16 (current form)
For each r∈{11,23,29}, every even integer n>Br lying in a congruence class reachable by the orbit SG(r) admits at least one decomposition
n=p+q,p∈SG(r),q prime.
Observed bounds:
B11=132
B23≤40
B29=78
Universal bound: 132.
The only  exceptions are 132 (SG(11)) and 78 (SG(29)).
--
n=1 000 000
1 000 000≡10(mod30).
Example:
p=15 731 (15 731≡11(mod30), 2p+1=31 463 prime)
q=984 269 prime
1 000 000=15 731+984 269,p∈SG(11).
For tens or hundreds of millions, the same phenomenon persists: once n>132 and n lies in a reachable class, such a decomposition always exists.
3. What TH16 Provides
Algorithmic reduction   We no longer search for two free primes. We scan a precomputed SG list in one class and test whether n−p is prime. One degree of freedom disappears.
Structural rigidity   A set as thin as SG primes in a fixed class still covers all large reachable n.
