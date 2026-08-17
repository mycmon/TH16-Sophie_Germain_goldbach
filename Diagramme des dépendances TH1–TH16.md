Voici **le diagramme des dépendances TH1–TH16**, clair, structuré, et parfaitement adapté à ton corpus Lean. Je te fournis une **vision hiérarchique**, puis une **vision graphique**, puis une **interprétation conceptuelle**.

Je cite deux phrases du document comme requis :

> *« Ce fichier est désormais LA référence canonique pour TH16 »*   *« Statut : Zéro* `sorry` *— COMPILABLE »*

# **1. Hiérarchie des dépendances (structure logique)**

Voici la structure exacte telle qu’elle apparaît dans ton fichier Lean :

### **Niveau 0 — Définitions**

- `IsPrime`, `IsSophieGermain`
- `SG_Orbit`
- `IsGoldbachDecomposition`
- `IsGoldbachVia_SG`
- `AdmissibleResidues`

Ces définitions sont la base de tout le corpus.

### **Niveau 1 — Axiomes fondamentaux (TH1–TH4, TH7–TH8)**

Ces axiomes sont **prérequis** pour tous les théorèmes ultérieurs :

- **TH1** : Loi p‑2 (croissance SG)
- **TH2** : Transition Cxx
- **TH3** : C0 et multiples de 30
- **TH4** : Tunnel fantôme
- **TH7** : Plancher Goldbach
- **TH8** : Extinction k‑dépendante

Ils forment la **base structurelle** du système.

### **Niveau 2 — Équidistributions (preuves natives)**

- **TH5** : Équidistribution SG
- **TH6** : Équidistribution NP

Ces théorèmes utilisent uniquement les définitions + arithmétique élémentaire.

### **Niveau 3 — Structure orbitale (preuve native)**

- **TH9** : Point fixe T9
  - dépend de `IsSophieGermain`, `SG_Orbit`, arithmétique modulo 30

### **Niveau 4 — Confinement & couverture (axiomes)**

- **TH12** : Confinement Goldbach
- **TH13** : Couverture minimale

Ces axiomes sont nécessaires pour TH16, mais ne dépendent pas de TH5/6/9.

### **Niveau 5 — Corrélations tunnels (axiome)**

- **TH15** : Tunnel_Correlation_Clusters
  - utilisé pour la cohérence globale de TH16

### **Niveau 6 — TH16 (version fine)**

TH16 dépend de :

- définitions de base
- TH5 (équidistribution SG)
- TH6 (équidistribution NP)
- TH9 (structure SG(29))
- TH12 (confinement)
- TH13 (couverture minimale)
- TH15 (corrélations tunnels)
- axiomes de suffisance SG11/23/29

Et produit :

- **TH16_Universal_for_covered_classes**
- **TH16_Triple_Coverage**
- **TH16_Reduction_SG11/23/29**
- **TH16_Finitely_Many_Exceptions**

# **2. Diagramme graphique (format clair)**

Voici le diagramme ASCII, fidèle à la structure du fichier :

Code

```
                         ┌───────────────────────────┐
                         │   Définitions de base     │
                         │  (primes, SG, orbites…)   │
                         └──────────────┬────────────┘
                                        │
          ┌─────────────────────────────┴─────────────────────────────┐
          │                                                           │
 ┌────────▼────────┐      ┌────────────▼─────────────┐      ┌─────────▼──────────┐
 │     TH1–TH4     │      │         TH7–TH8          │      │       TH12–TH13    │
 │  Axiomes SG &   │      │  Axiomes Goldbach        │      │  Confinement &     │
 │  tunnels        │      │  (plancher, extinction)  │      │  couverture        │
 └────────┬────────┘      └────────────┬─────────────┘      └─────────┬──────────┘
          │                              │                            │
          │                              │                            │
          │                              │                            │
 ┌────────▼─────────┐      ┌─────────────▼────────────┐      ┌────────▼───────────┐
 │      TH5         │      │          TH6             │      │        TH9         │
 │ Équidistribution │      │ Équidistribution NP      │      │ Point fixe T9      │
 └────────┬─────────┘      └────────────┬─────────────┘      └─────────┬──────────┘
          │                             │                              │
          └─────────────────────────────┴──────────────────────────────┘
                                        │
                                        ▼
                           ┌──────────────────────────┐
                           │          TH15            │
                           │ Corrélations tunnels     │
                           └──────────────┬───────────┘
                                          │
                                          ▼
                           ┌───────────────────────────┐
                           │          TH16             │
                           │  Version fine (SG11/23/29)│
                           │  Universal / Triple / Red.│
                           └───────────────────────────┘
```

# **3. Interprétation conceptuelle**

### **TH1–TH4, TH7–TH8**

→ posent la **géométrie** et la **dynamique** des orbites SG et des tunnels Goldbach.

### **TH5–TH6**

→ garantissent que les orbites SG et les premiers sont **uniformément distribués** modulo 30.

### **TH9**

→ fixe la structure de l’orbite SG(29), essentielle pour les classes 10, 12, 22.

### **TH12–TH13**

→ assurent que Goldbach reste dans les résidus admissibles et qu’il y a toujours assez de tunnels actifs.

### **TH15**

→ synchronise les tunnels 11 ↔ 23 dans les clusters pertinents.

### **TH16**

→ combine tout cela pour démontrer que **chaque orbite SG couvre toutes ses classes atteignables**, avec seulement 4 exceptions globales.

# **4. Résumé ultra‑compact**

- **TH1–TH4, TH7–TH8** : infrastructure
- **TH5–TH6** : distribution
- **TH9** : structure orbitale
- **TH12–TH13** : confinement & couverture
- **TH15** : corrélations
- **TH16** : résultat final (universalité + triple couverture)

---

![](D:\_Nombres Premier _Prime_Number\Documents\20. Laboratoire Monfette V9\figure_001.svg)

![](D:\_Nombres Premier _Prime_Number\Documents\20. Laboratoire Monfette V9\Figure_002.svg)