[🇬🇧 English](README.md) | 🇫🇷 **Français**
---
## Documentation

| Document | English | Français |
|----------|:-------:|:---------:|
| README | ✅ | [🇫🇷](README.fr.md) |
| Manifesto | [📖](MANIFESTO.md) | [📖](MANIFESTO.fr.md) |
| Lexicon | [📖](LEXICON.md) | [📖](LEXICON.fr.md) |
| Fundamental Laws | [📖](DSCA_LAWS.md) | [📖](DSCA_LAWS.fr.md) |
---
# DSCA — Dynamic System Causal Analysis

> **Comprendre les systèmes, pas simplement lire les données.**

DSCA est un projet open source dédié à l'analyse causale des systèmes dynamiques.

Plutôt que de créer un nouvel outil de diagnostic, DSCA a pour objectif de proposer une nouvelle manière de comprendre les systèmes complexes en analysant les données enregistrées, en identifiant leurs interactions et en aidant l'utilisateur à construire des hypothèses techniques cohérentes.

---

# Pourquoi DSCA ?

Les systèmes modernes génèrent aujourd'hui des milliers de mesures chaque seconde.

Les outils de diagnostic actuels savent :

* lire les codes défaut ;
* afficher les données en temps réel ;
* enregistrer des journaux d'acquisition (logs).

En revanche, ils aident encore très peu à comprendre comment toutes ces données interagissent dans le temps.

DSCA commence là où les outils de diagnostic traditionnels s'arrêtent.

---

# Objectifs du projet

DSCA a pour objectif de :

* importer des journaux provenant de différents outils d'acquisition ;
* normaliser des données issues de sources hétérogènes ;
* détecter les événements significatifs ;
* construire des relations contextuelles entre les observations ;
* identifier des signatures comportementales ;
* générer des hypothèses causales explicables ;
* assister le raisonnement humain sans jamais le remplacer.

---

# État du projet

🚧 **Recherche & Développement – Phase de conception**

DSCA est actuellement en phase de conception.

Son architecture, sa philosophie et ses concepts fondamentaux sont définis avant le début du développement.

---

# Architecture prévisionnelle

```text
Journaux d'acquisition
        │
        ▼
Importeurs
        │
        ▼
Normalisation
        │
        ▼
Moteur d'état du système
        │
        ▼
Détection d'événements
        │
        ▼
Analyse comportementale
        │
        ▼
Raisonnement causal
        │
        ▼
Génération d'hypothèses
        │
        ▼
Interprétation humaine
```

---

# Fonctionnalités prévues

* Import de journaux multi-formats
* Prise en charge des fichiers CSV Launch
* Prise en charge des fichiers CSV Autel
* Prise en charge des journaux AutoTuner
* Importateur CSV générique
* Moteur de détection d'événements
* Reconnaissance de signatures comportementales
* Analyse causale contextualisée
* Moteur de raisonnement explicable
* Génération de rapports techniques assistés par IA

---

# Principes fondamentaux

* Les observations précèdent toujours les hypothèses.
* Le contexte est essentiel.
* Toute hypothèse doit pouvoir être expliquée.
* Toute hypothèse doit pouvoir être réfutée.
* L'expertise humaine demeure toujours au centre du processus.

Pour découvrir la philosophie complète du projet, consultez **MANIFESTO.fr.md**.

---

# Structure du dépôt

```text
DSCA/

├── README.md
├── README.fr.md
├── MANIFESTO.md
├── MANIFESTO.fr.md
├── docs/
├── src/
├── tests/
├── plugins/
└── examples/
```

---

# Feuille de route

## Genesis

* [ ] Initialisation du dépôt
* [ ] Conception de l'architecture principale
* [ ] Documentation

## Foundation

* [ ] Importateur CSV générique
* [ ] Importateur Launch
* [ ] Normalisation des données

## Engine

* [ ] Modèle d'état du système
* [ ] Moteur d'événements
* [ ] Moteur d'analyse comportementale
* [ ] Moteur de raisonnement causal

## Assistant

* [ ] Raisonnement explicable
* [ ] Génération de rapports techniques
* [ ] Assistance au diagnostic par IA

---

# Contribuer

DSCA accueille les contributions de :

* développeurs logiciels ;
* ingénieurs automobiles ;
* spécialistes du diagnostic ;
* chercheurs ;
* étudiants ;
* passionnés de systèmes dynamiques.

Si vous partagez la philosophie du projet, votre contribution est la bienvenue.

---

# Licence

Licence en cours de définition.

---

# Devise

**Créer l'avenir, pas simplement le demain.**
