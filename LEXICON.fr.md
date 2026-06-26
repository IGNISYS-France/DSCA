🇫🇷 **Français** | [🇬🇧 English](LEXICON.md)

---

# Lexique DSCA

> **Le langage officiel du moteur de raisonnement DSCA.**

L'objectif de ce document est de définir le vocabulaire officiel utilisé dans l'ensemble du projet DSCA.

Chaque contributeur devrait s'y référer avant d'introduire une nouvelle terminologie.

---

# Flux conceptuel

```text
Système Dynamique
        │
        ▼
Signaux
        │
        ▼
Observations
        │
        ▼
Contexte
        │
        ▼
État du Système
        │
        ▼
Événements
        │
        ▼
Comportements
        │
        ▼
Chaînes Causales
        │
        ▼
Hypothèses
        │
        ▼
Connaissance
        │
        ▼
Compréhension
        │
        ▼
Exploration
```

---

# Concepts Fondamentaux

---

# Signal

## Définition

Un **Signal** est la plus petite unité mesurable manipulée par DSCA.

Il représente l'évolution d'une grandeur physique, logique ou calculée au cours du temps.

Chaque Signal référence un **Signal Canonique** défini par le **Registre des Signaux DSCA**.

## Objectif

Les Signaux constituent les observations élémentaires à partir desquelles tous les concepts de niveau supérieur sont construits.

## Relations

* Les Signaux référencent des Signaux Canoniques.
* L'évolution des Signaux peut générer des Événements.
* Les Signaux composent les Observations.

## Exemples

* Régime moteur
* Pression de rampe
* Lambda
* Niveau de cliquetis
* Température du liquide de refroidissement
* Position de la pédale d'accélérateur

---

# Signal Canonique

## Définition

Un **Signal Canonique** est la représentation officielle DSCA d'une grandeur physique mesurable.

Il possède un identifiant unique indépendant des constructeurs, des outils de diagnostic, des langues ou des conventions de nommage.

Chaque Signal manipulé par DSCA référence un unique Signal Canonique.

## Objectif

Fournir un langage commun partagé par tous les importateurs, les moteurs de raisonnement et les outils de visualisation.

Les Signaux Canoniques permettent à différentes sources de données de décrire un même phénomène physique de manière cohérente.

## Exemple

Signal Canonique :

* Régime moteur

Alias possibles :

* RPM
* Engine RPM
* Motordrehzahl
* Régime moteur
* PID 0C
* N_ENGINE

---

# Alias de Signal

## Définition

Un **Alias de Signal** est un nom alternatif utilisé par un constructeur, un outil de diagnostic ou une source de données pour désigner un Signal Canonique.

Plusieurs alias peuvent représenter la même grandeur physique.

## Objectif

Permettre à DSCA de reconnaître des Signaux identiques provenant de sources hétérogènes.

Les Alias n'influencent jamais le raisonnement.

Ils sont uniquement utilisés lors de l'acquisition et de la normalisation des observations.

## Relations

Les Alias de Signal appartiennent à un Signal Canonique.

Les importateurs résolvent les alias grâce au Registre des Signaux DSCA.

---

# Registre des Signaux

## Définition

Le **Registre des Signaux** constitue le vocabulaire canonique utilisé dans l'ensemble du projet.

Il associe chaque Alias de Signal connu à un unique Signal Canonique.

Le registre représente la couche de traduction entre les sources de données externes et le langage interne de DSCA.

## Objectif

Fournir un langage universel indépendant :

* des constructeurs ;
* des outils de diagnostic ;
* des formats de fichiers ;
* des langues ;
* des conventions de nommage.

## Responsabilités

* Définir les Signaux Canoniques.
* Stocker les Alias de Signal.
* Définir les unités de mesure standard.
* Associer les grandeurs physiques.
* Catégoriser les Signaux.
* Stocker les métadonnées des Signaux.
* Permettre les contributions futures de la communauté.

## Relations

Le Registre des Signaux est utilisé par :

* les Importateurs ;
* l'Acquisition des Observations ;
* la Normalisation des Observations ;
* la Validation des Signaux ;
* le Moteur de Raisonnement ;
* la Visualisation.

## Principe

DSCA ne raisonne jamais sur les noms propres aux constructeurs.

DSCA raisonne toujours sur des **Signaux Canoniques**.

---

# Code de Diagnostic

## Définition

Un Code de Diagnostic est un identifiant normalisé généré par un système de contrôle afin de signaler une condition anormale ou un dysfonctionnement détecté.

Un Code de Diagnostic représente l'interprétation d'une ou plusieurs observations réalisée par un contrôleur.

Il ne constitue pas une observation directe.

## Objectif

Fournir un élément de preuve diagnostique supplémentaire pouvant contribuer au raisonnement causal.

Les Codes de Diagnostic ne constituent jamais une preuve d'une cause racine.

## Relations

Les Codes de Diagnostic peuvent référencer :

* des Signaux Canoniques ;
* des Événements ;
* des Comportements.

Ils contribuent à l'élaboration d'hypothèses causales, sans jamais remplacer les observations.

## Exemples

* P0087
* P0299
* P0300
* P0101

---

# Registre des Codes de Diagnostic

## Définition

Le Registre des Codes de Diagnostic constitue la base de connaissances officielle de DSCA décrivant les Codes de Diagnostic normalisés.

Chaque définition de Code de Diagnostic peut inclure :

* une description ;
* les Signaux Canoniques associés ;
* les Comportements associés ;
* les causes possibles ;
* les observations recommandées ;
* les expériences suggérées.

## Objectif

Fournir une connaissance diagnostique structurée tout en restant indépendante de toute implémentation propre à un constructeur.

Le Registre assiste le raisonnement.

Le Registre complète les observations.

Il ne les remplace jamais.

Il ne détermine jamais les conclusions.

---

# Registre des Expériences

## Définition

Le Registre des Expériences constitue la base de connaissances officielle de DSCA décrivant les expériences diagnostiques utilisées pour valider ou invalider des hypothèses.

## Objectif

Fournir des procédures de validation réutilisables pour le raisonnement causal.

Les expériences transforment des hypothèses plausibles en connaissances validées.

---

# Observation

## Définition

Une **Observation** est un instantané complet de tous les Signaux disponibles à un instant donné.

## Objectif

Représenter l'état mesurable complet d'un système.

## Relations

* Une Observation contient des Signaux.
* Les Observations appartiennent à un Contexte.
* Plusieurs Observations décrivent l'évolution d'un système.

---

# Contexte

## Définition

Le **Contexte** regroupe l'ensemble des conditions environnementales, opérationnelles ou de configuration entourant les Observations.

## Objectif

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

# État du Système

## Définition

L'**État du Système** représente la condition complète d'un système pendant une période donnée.

Il combine :

* les Observations ;
* le Contexte ;
* les Événements actifs.

## Objectif

Représenter ce que le système est en train de vivre.

---

# Concepts d'Interprétation

---

# Événement

## Définition

Un **Événement** est une évolution significative détectée à partir d'un ou plusieurs Signaux.

Les Événements ne sont pas directement mesurés.

Ils sont déduits.

## Objectif

Transformer des mesures continues en changements significatifs.

## Exemples

* Chute de pression
* Récupération de pression
* Détection de cliquetis
* Limitation de couple
* Détection de ratés d'allumage
* Incohérence capteur

---

# Comportement

## Définition

Un **Comportement** est une organisation récurrente d'Événements décrivant la manière dont un système fonctionne.

Les Comportements sont indépendants des constructeurs.

Ils décrivent la physique plutôt que les implémentations.

## Objectif

Représenter des comportements plutôt que des mesures isolées.

## Exemples

* Manque d'alimentation en carburant sous forte charge
* Limitation thermique
* Régulation de pression oscillante
* Instabilité d'allumage

---

# Chaîne Causale

## Définition

Une **Chaîne Causale** est une succession ordonnée d'Événements reliés par des relations physiques plausibles.

## Objectif

Décrire comment un événement peut conduire à un autre.

Une Chaîne Causale constitue la base de la construction des hypothèses.

---

# Hypothèse Causale

## Définition

Une **Hypothèse Causale** est une interprétation explicable d'un ou plusieurs Comportements.

Une hypothèse reste toujours provisoire.

## Objectif

Assister le raisonnement.

Ne jamais le remplacer.

---

# Niveau de Confiance

## Définition

Le **Niveau de Confiance** estime dans quelle mesure les observations disponibles soutiennent une hypothèse.

## Objectif

Classer les hypothèses concurrentes.

La confiance ne représente jamais une certitude.

---

# Concepts de Connaissance

---

# Validation

## Définition

La **Validation** consiste à confirmer ou rejeter une hypothèse à l'aide d'observations supplémentaires ou d'expériences.

## Objectif

Distinguer les explications plausibles des connaissances validées.

---

# Expérience

## Définition

Une **Expérience** est une modification volontaire réalisée afin de confirmer ou d'infirmer une ou plusieurs hypothèses.

## Objectif

Transformer les hypothèses en connaissances.

## Exemples

* Désactiver la climatisation
* Augmenter la pression de carburant
* Répéter l'essai
* Remplacer un composant
* Réaliser des mesures à l'oscilloscope

---

# Connaissance

## Définition

La **Connaissance** est une compréhension validée obtenue grâce à des observations répétées et à des expériences concluantes.

## Objectif

Fournir des bases fiables pour les raisonnements futurs.

La Connaissance reste toujours ouverte à la révision lorsqu'une nouvelle preuve apparaît.

---

# Explication

## Définition

Une **Explication** est une description compréhensible par un humain générée par DSCA.

## Objectif

Expliquer :

* ce qui s'est produit ;
* pourquoi cela s'est produit ;
* quelles observations soutiennent le raisonnement ;
* quelles incertitudes subsistent ;
* quelles expériences complémentaires sont recommandées.

---

# Raisonnement

## Définition

Le **Raisonnement** est le processus de construction d'hypothèses cohérentes à partir des observations dans le respect des principes physiques.

Le Raisonnement est transparent.

Le Raisonnement est explicable.

Le Raisonnement est toujours révisable.

---

# Compréhension

## Définition

La **Compréhension** est l'interprétation cohérente d'un système dynamique fondée sur les observations, le contexte, les événements, les comportements et les hypothèses validées.

## Objectif

La Compréhension constitue l'objectif ultime de DSCA.

Elle n'est jamais absolue.

Elle évolue continuellement à mesure que de nouvelles observations deviennent disponibles.

---

# Exploration

## Définition

L'**Exploration** est le processus itératif consistant à observer, contextualiser, raisonner, expérimenter et affiner la compréhension à partir des preuves disponibles.

## Objectif

Explorer le comportement des systèmes dynamiques sans supposer de conclusions à l'avance.

L'Exploration constitue le fondement de l'apprentissage dans DSCA.

---

# Concepts du Domaine

---

# Système Dynamique

## Définition

Un **Système Dynamique** est tout système dont l'état évolue au cours du temps.

## Exemples

* Moteur thermique
* Groupe motopropulseur électrique
* Moto
* Machine industrielle
* Robot
* Système hydraulique

---

# DSCA

## Définition

**Dynamic System Causal Analysis.**

Un moteur de raisonnement open source dédié à la compréhension des systèmes dynamiques grâce aux observations, à la contextualisation et à l'analyse causale explicable.

DSCA ne remplace pas l'expertise humaine.

Il prolonge la capacité de l'humain à explorer des systèmes complexes.

---

# Principe Fondamental

**Les mots définissent les concepts.**

**Les concepts définissent l'architecture.**

**L'architecture définit le logiciel.**

Chaque nouvelle fonctionnalité introduite dans DSCA doit rester cohérente avec ce Lexique.
