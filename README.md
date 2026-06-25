# DSCA — Dynamic System Causal Analysis

> **Understanding systems, not simply reading data.**

DSCA is an open-source project dedicated to the causal analysis of dynamic systems.

Rather than creating another diagnostic tool, DSCA aims to provide a new way of understanding complex systems by analyzing recorded data, identifying interactions, and assisting the user in building coherent technical hypotheses.

---

# Why DSCA?

Modern systems generate thousands of measurements every second.

Today's diagnostic tools can:

* read fault codes;
* display live data;
* record logs.

However, they rarely help users understand how these data interact over time.

DSCA starts where traditional diagnostic tools stop.

---

# Project Objectives

DSCA aims to:

* Import logs from different acquisition tools.
* Normalize heterogeneous data.
* Detect significant events.
* Build contextual relationships between observations.
* Identify behavioral signatures.
* Generate explainable causal hypotheses.
* Assist human reasoning without replacing it.

---

# Project Status

🚧 **Early Research & Development**

DSCA is currently in its design phase.

The architecture, philosophy and core concepts are being defined before implementation begins.

---

# Planned Architecture

```text
Raw Logs
   │
   ▼
Importers
   │
   ▼
Normalization
   │
   ▼
System State Engine
   │
   ▼
Event Detection
   │
   ▼
Behavior Analysis
   │
   ▼
Causal Reasoning
   │
   ▼
Hypothesis Generation
   │
   ▼
Human Interpretation
```

---

# Planned Features

* Multi-format log import
* Launch CSV support
* Autel CSV support
* AutoTuner log support
* Generic CSV importer
* Event detection engine
* Behavioral pattern recognition
* Context-aware causal analysis
* Explainable reasoning engine
* AI-assisted technical reports

---

# Core Principles

* Observations always come before hypotheses.
* Context is essential.
* Every hypothesis must be explainable.
* Every hypothesis must be falsifiable.
* Human expertise always remains central.

For the complete philosophy of the project, please read **MANIFESTO.md**.

---

# Repository Structure

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

# Roadmap

## Genesis

* [ ] Repository initialization
* [ ] Core architecture
* [ ] Documentation

## Foundation

* [ ] Generic CSV importer
* [ ] Launch importer
* [ ] Data normalization

## Engine

* [ ] System state model
* [ ] Event engine
* [ ] Behavioral engine
* [ ] Causal engine

## Assistant

* [ ] Explainable reasoning
* [ ] Technical report generation
* [ ] AI-assisted analysis

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

License to be defined.

---

# Motto

**Create the future, not simply tomorrow.**
