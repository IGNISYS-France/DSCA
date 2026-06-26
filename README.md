🇬🇧 **English** | [🇫🇷 Français](README.fr.md)

---

# DSCA — Dynamic System Causal Analysis

> **From observations to understanding.**

DSCA is an open-source project dedicated to the explainable understanding of dynamic systems through causal reasoning.

Rather than creating another diagnostic tool, DSCA aims to build a generic reasoning engine capable of transforming heterogeneous observations into coherent, explainable technical understanding.

---

# Why DSCA?

Modern systems generate thousands of measurements every second.

Today's diagnostic tools can:

* read fault codes;
* display live data;
* record logs.

However, they rarely explain **why** systems behave as they do.

DSCA starts where traditional diagnostic tools stop.

Its objective is not simply to analyze data.

Its objective is to understand dynamic systems.

---

# Project Objectives

DSCA aims to:

* acquire heterogeneous observations;
* normalize measurements into a common language;
* reconstruct system context;
* detect meaningful events;
* identify behavioral patterns;
* generate explainable causal hypotheses;
* accumulate validated knowledge;
* assist human reasoning without replacing it.

---

# Documentation

| Document            |           English           |            Français            |
| ------------------- | :-------------------------: | :----------------------------: |
| README              |              ✅             |      [🇫🇷](README.fr.md)        |
| Manifesto           |       [📖](MANIFESTO.md)    | [📖](MANIFESTO.fr.md)         |
| Lexicon             |       [📖](LEXICON.md)      |       [📖](LEXICON.fr.md)     |
| Fundamental Laws    |      [📖](DSCA_LAWS.md)     |      [📖](DSCA_LAWS.fr.md)    |
| Data Model          |     [📖](DATA_MODEL.md)     |                —               |
| Development Roadmap |       [📖](ROADMAP.md)      |                —               |
| Reasoning Roadmap   |  [📖](REASONING_ROADMAP.md) |                —               |

---

# Current Status

🚧 **Version 0.1.0-dev — Observation**

Genesis has been completed.

DSCA is now entering its first development milestone: **Observation**.

Current work focuses on:

* Signal model
* Canonical Signal model
* DSCA Signal Registry
* Observation model
* Generic CSV importer

---

# High-Level Architecture

```text
External Data Sources
        │
        ▼
Importers
        │
        ▼
DSCA Signal Registry
        │
        ▼
Observation Model
        │
        ▼
Context Engine
        │
        ▼
Event Engine
        │
        ▼
Behavior Engine
        │
        ▼
Reasoning Engine
        │
        ▼
Knowledge Engine
        │
        ▼
Human Understanding
```

---

# Core Principles

DSCA is built upon several fundamental principles:

* Observations always precede hypotheses.
* Context gives meaning to observations.
* Every hypothesis must remain explainable.
* Every hypothesis must remain falsifiable.
* Knowledge is built through validation.
* Human expertise always remains central.

For the complete philosophy of the project, please read the **Manifesto**.

---

# Repository Structure

```text
DSCA/

├── README.md
├── README.fr.md
├── MANIFESTO.md
├── MANIFESTO.fr.md
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

# Development

The complete development roadmap is available in **ROADMAP.md**.

The evolution of DSCA's reasoning capabilities is described in **REASONING_ROADMAP.md**.

---

# Contributing

DSCA welcomes contributions from:

* software developers;
* automotive engineers;
* diagnostic specialists;
* researchers;
* students;
* enthusiasts interested in dynamic systems.

If you share the project's philosophy, contributions are welcome.

---

# License

This project is released under the MIT License.

See the **LICENSE** file for details.

---

# Motto

> **Create the future, not simply tomorrow.**
