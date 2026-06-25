[🇬🇧 English](LEXICON.md) | 🇫🇷 **Français**
---
# LEXICON.fr.md

# Lexique DSCA

> **Un langage commun pour comprendre les systèmes dynamiques.**

Ce document a pour objectif de définir le vocabulaire officiel utilisé au sein du projet DSCA.

Tout contributeur est invité à s'y référer avant d'introduire une nouvelle terminologie.

---

# Signal

## Définition

Un **Signal** est la plus petite unité mesurable manipulée par DSCA.

Il représente l'évolution d'une grandeur physique, logique ou calculée au cours du temps.

## Rôle

Les Signaux constituent les observations brutes à partir desquelles tous les concepts de niveau supérieur sont construits.

## Relations

Les Signaux composent les **Observations**.

L'évolution d'un ou plusieurs Signaux peut générer des **Événements**.

## Exemples

* Régime moteur
* Pression de rampe
* Lambda
* Niveau de cliquetis
* Température du liquide de refroidissement
* Position de la pédale d'accélérateur

---

# Observation

## Définition

Une **Observation** représente une photographie complète de tous les Signaux disponibles à un instant donné.

## Rôle

Représenter l'état mesurable complet d'un système à un moment précis.

## Relations

Une Observation regroupe plusieurs Signaux.

Les Observations appartiennent à un **Contexte**.

La succession des Observations décrit l'évolution d'un système.

---

# Contexte

## Définition

Le **Contexte** regroupe l'ensemble des conditions environnementales, opérationnelles ou de configuration dans lesquelles les Observations sont réalisées.

## Rôle

Donner du sens aux Signaux et aux Observations.

Sans Contexte, une Observation ne peut être interprétée correctement.

## Exemples

* Type de carburant
* Température ambiante
* Température moteur
* Configuration du véhicule
* État de la climatisation
* Version de calibration

---

# Événement

## Définition

Un **Événement** est une évolution significative détectée à partir d'un ou plusieurs Signaux.

Les Événements ne sont pas mesurés.

Ils sont déduits.

## Rôle

Transformer des données continues en changements significatifs.

## Exemples

* Chute de pression
* Remontée de pression
* Détection de cliquetis
* Limitation de couple
* Détection de ratés d'allumage
* Incohérence capteur

---

# État du système

## Définition

L'**État du système** représente la condition complète d'un système pendant une période donnée.

Il regroupe :

* les Observations ;
* le Contexte ;
* les Événements actifs.

## Rôle

Décrire ce que vit le système à un instant ou sur une période donnée.

---

# Signature comportementale

## Définition

Une **Signature comportementale** est une organisation récurrente d'Événements décrivant la manière dont un système se comporte.

Les Signatures comportementales sont indépendantes des constructeurs.

Elles décrivent les comportements physiques plutôt que les implémentations spécifiques.

## Rôle

Représenter des comportements plutôt que des valeurs isolées.

## Exemples

* Manque d'alimentation en carburant sous forte charge
* Limitation thermique
* Régulation de pression oscillante
* Instabilité de l'allumage

---

# Chaîne causale

## Définition

Une **Chaîne causale** est une succession ordonnée d'Événements reliés par des relations physiques plausibles.

## Rôle

Décrire comment un événement peut conduire à un autre.

Une Chaîne causale constitue la base de la construction d'une hypothèse.

---

# Hypothèse causale

## Définition

Une **Hypothèse causale** est une interprétation explicable d'une ou plusieurs Signatures comportementales.

Une hypothèse reste toujours provisoire.

## Rôle

Assister le raisonnement.

Jamais le remplacer.

---

# Niveau de confiance

## Définition

Le **Niveau de confiance** représente le degré de soutien apporté par les observations disponibles à une hypothèse.

## Rôle

Classer plusieurs hypothèses concurrentes.

Un Niveau de confiance ne représente jamais une certitude.

---

# Validation

## Définition

La **Validation** est le processus consistant à confirmer ou à réfuter une hypothèse au moyen d'observations ou d'expériences complémentaires.

## Rôle

Distinguer les explications plausibles des connaissances validées.

---

# Expérience

## Définition

Une **Expérience** est une modification volontaire réalisée afin de confirmer ou d'infirmer une ou plusieurs hypothèses.

## Rôle

Transformer une hypothèse en connaissance.

## Exemples

* Désactiver la climatisation
* Augmenter la pression de carburant
* Répéter un essai
* Remplacer un composant
* Réaliser des mesures à l'oscilloscope

---

# Connaissance

## Définition

Une **Connaissance** est une compréhension validée obtenue grâce à des observations répétées et à des expériences concluantes.

## Rôle

Fournir une base fiable pour les raisonnements futurs.

Une Connaissance demeure toujours révisable lorsqu'une nouvelle preuve apparaît.

---

# Explication

## Définition

Une **Explication** est une description compréhensible par l'humain, générée par DSCA.

## Rôle

Expliquer :

* ce qui s'est produit ;
* pourquoi cette hypothèse est proposée ;
* quelles observations soutiennent ce raisonnement ;
* quelles incertitudes subsistent ;
* quels essais complémentaires sont recommandés.

---

# Système dynamique

## Définition

Un **Système dynamique** est tout système dont l'état évolue au cours du temps.

## Exemples

* Moteur à combustion interne
* Groupe motopropulseur électrique
* Motocycle
* Machine industrielle
* Robot
* Système hydraulique

---

# Exploration

## Définition

L'**Exploration** est un processus itératif consistant à observer, contextualiser, raisonner, expérimenter et affiner progressivement la compréhension d'un système à partir de preuves.

## Rôle

Explorer le comportement des systèmes dynamiques sans supposer de conclusion à l'avance.

L'Exploration constitue le fondement de l'apprentissage au sein de DSCA.

---

# Raisonnement

## Définition

Le **Raisonnement** est le processus de construction d'hypothèses cohérentes à partir d'observations, dans le respect des principes physiques.

Le Raisonnement est transparent.

Le Raisonnement est explicable.

Le Raisonnement demeure toujours ouvert à la révision.

---

# DSCA

## Définition

**Dynamic System Causal Analysis.**

Un moteur open source de raisonnement dédié à la compréhension des systèmes dynamiques grâce aux observations, à leur contextualisation et à une analyse causale explicable.

DSCA ne remplace jamais l'expertise humaine.

Il prolonge la capacité de l'humain à explorer des systèmes complexes.

---

# Compréhension

## Définition

La **Compréhension** est l'interprétation cohérente d'un système dynamique fondée sur les observations, le contexte, les événements, les signatures comportementales et les hypothèses validées.

## Rôle

La Compréhension constitue l'objectif ultime de DSCA.

Elle n'est jamais absolue.

Elle évolue continuellement à mesure que de nouvelles observations deviennent disponibles.

---

# Principe directeur

**Les mots définissent les concepts.**

**Les concepts définissent l'architecture.**

**L'architecture définit le logiciel.**

Toute nouvelle fonctionnalité introduite dans DSCA doit rester cohérente avec ce Lexique.
