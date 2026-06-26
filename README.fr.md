🇫🇷 **Français** | [🇬🇧 English](README.md)

---

# DSCA — Dynamic System Causal Analysis

> **Des observations vers la compréhension.**

DSCA est un projet open source dédié à la compréhension explicable des systèmes dynamiques par le raisonnement causal.

Plutôt que de créer un nouvel outil de diagnostic, DSCA a pour ambition de développer un moteur de raisonnement générique capable de transformer des observations hétérogènes en une compréhension technique cohérente et explicable.

---

# Pourquoi DSCA ?

Les systèmes modernes génèrent des milliers de mesures chaque seconde.

Les outils de diagnostic actuels savent :

* lire les codes défaut ;
* afficher les données en temps réel ;
* enregistrer des journaux de fonctionnement.

En revanche, ils expliquent rarement **pourquoi** un système se comporte d'une certaine manière.

DSCA commence là où les outils de diagnostic traditionnels s'arrêtent.

Son objectif n'est pas simplement d'analyser des données.

Son objectif est de comprendre les systèmes dynamiques.

---

# Objectifs du projet

DSCA a pour objectif de :

* acquérir des observations provenant de sources hétérogènes ;
* normaliser les mesures dans un langage commun ;
* reconstruire le contexte d'un système ;
* détecter les événements significatifs ;
* identifier des comportements récurrents ;
* générer des hypothèses causales explicables ;
* accumuler des connaissances validées ;
* assister le raisonnement humain sans jamais le remplacer.

---

# Documentation

| Document                         |           English           |            Français            |
| -------------------------------- | :-------------------------: | :----------------------------: |
| README                           |      [🇬🇧](README.md)      |                ✅               |
| Manifeste                        | [📖](THE-DSCA-MANIFESTO.md) | [📖](THE-DSCA-MANIFESTO.fr.md) |
| Lexique                          |       [📖](LEXICON.md)      |       [📖](LEXICON.fr.md)      |
| Lois Fondamentales               |      [📖](DSCA_LAWS.md)     |      [📖](DSCA_LAWS.fr.md)     |
| Modèle de Données                |     [📖](DATA_MODEL.md)     |                —               |
| Feuille de Route                 |       [📖](ROADMAP.md)      |                —               |
| Feuille de Route du Raisonnement |  [📖](REASONING_ROADMAP.md) |                —               |

---

# État actuel du projet

🚧 **Version 0.1.0-dev — Observation**

La phase **Genesis** est désormais terminée.

DSCA entre officiellement dans sa première étape de développement : **Observation**.

Les travaux actuels portent sur :

* le modèle de Signal ;
* le modèle de Signal Canonique ;
* le Registre des Signaux DSCA ;
* le modèle d'Observation ;
* le premier importateur CSV générique.

---

# Architecture générale

```text
Sources de données externes
            │
            ▼
Importateurs
            │
            ▼
Registre des Signaux DSCA
            │
            ▼
Modèle d'Observation
            │
            ▼
Moteur de Contexte
            │
            ▼
Moteur d'Événements
            │
            ▼
Moteur de Comportements
            │
            ▼
Moteur de Raisonnement
            │
            ▼
Moteur de Connaissance
            │
            ▼
Compréhension humaine
```

---

# Principes fondamentaux

DSCA repose sur plusieurs principes essentiels :

* Les observations précèdent toujours les hypothèses.
* Le contexte donne du sens aux observations.
* Toute hypothèse doit être explicable.
* Toute hypothèse doit pouvoir être remise en question.
* La connaissance se construit par la validation.
* L'expertise humaine reste toujours centrale.

Pour découvrir la philosophie complète du projet, consultez le **Manifeste**.

---

# Structure du dépôt

```text
DSCA/

├── README.md
├── README.fr.md
├── THE-DSCA-MANIFESTO.md
├── THE-DSCA-MANIFESTO.fr.md
├── LEXICON.md
├── LEXICON.fr.md
├── DSCA_LAWS.md
├── DSCA_LAWS.fr.md
├── DATA_MODEL.md
├── ROADMAP.md
├── REASONING_ROADMAP.md
├── LICENSE
└── src/
    └── dsca/
```

---

# Développement

La feuille de route complète du projet est disponible dans **ROADMAP.md**.

L'évolution des capacités de raisonnement de DSCA est décrite dans **REASONING_ROADMAP.md**.

---

# Contribuer

DSCA accueille avec plaisir les contributions de :

* développeurs logiciels ;
* ingénieurs automobiles ;
* spécialistes du diagnostic ;
* chercheurs ;
* étudiants ;
* passionnés de systèmes dynamiques.

Si vous partagez la philosophie du projet, votre contribution est la bienvenue.

---

# Licence

Ce projet est distribué sous licence **MIT**.

Consultez le fichier **LICENSE** pour plus d'informations.

---

# Devise

> **Créer l'avenir, pas simplement demain.**
