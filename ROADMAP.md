# DSCA Roadmap

> **From observations to understanding.**

This roadmap describes the long-term vision of the DSCA project.

The goal is not simply to develop software, but to progressively build a causal reasoning engine capable of assisting the understanding of dynamic systems.

---

# Phase 0 — Genesis

**Project Foundation**

* [x] Define the project philosophy
* [x] Write the Manifesto
* [x] Create the README documentation
* [ ] Define the software architecture
* [ ] Define the internal data model
* [ ] Choose the development stack
* [ ] Create the first development environment

---

# Phase 1 — Core Foundation

**The software must first understand data before interpreting it.**

## Data Import

* [ ] Generic CSV importer
* [ ] Launch CSV importer
* [ ] Autel CSV importer
* [ ] AutoTuner log importer
* [ ] Extensible plugin importer system

## Data Normalization

* [ ] Common internal data model
* [ ] Timestamp synchronization
* [ ] Unit conversion
* [ ] Signal validation
* [ ] Missing data management

---

# Phase 2 — System Representation

**Represent the state of a dynamic system at any instant.**

* [ ] System State model
* [ ] Context model
* [ ] Signal abstraction
* [ ] Dynamic context engine
* [ ] Time-series management

---

# Phase 3 — Event Engine

**Transform measurements into meaningful events.**

Examples:

* Pressure drop
* Pressure recovery
* Sudden temperature increase
* Torque limitation
* Misfire detection
* Knock detection
* Load transition
* Sensor incoherence

Features:

* [ ] Event detection engine
* [ ] Event classification
* [ ] Event timeline generation
* [ ] Event confidence evaluation

---

# Phase 4 — Behavioral Engine

**Understand system behavior instead of isolated values.**

* [ ] Behavioral pattern detection
* [ ] Event sequence recognition
* [ ] Behavioral signature library
* [ ] Pattern comparison
* [ ] Similar behavior search

---

# Phase 5 — Causal Reasoning Engine

**Build explainable technical hypotheses.**

The engine should:

* identify plausible causal chains;
* rank competing hypotheses;
* explain every conclusion;
* identify missing information;
* suggest additional measurements.

The engine must never claim certainty.

---

# Phase 6 — Knowledge Engine

**Learn from validated observations.**

* [ ] Behavioral knowledge base
* [ ] Signature management
* [ ] Validation workflow
* [ ] Knowledge versioning
* [ ] Community review

---

# Phase 7 — AI Assistant

The AI should never replace human reasoning.

Its role is to:

* explain observations;
* summarize complex situations;
* generate technical reports;
* answer questions about analyses;
* assist exploration.

---

# Phase 8 — Visualization

Understanding begins with visualization.

* [ ] Interactive timeline
* [ ] Event graph
* [ ] Signal comparison
* [ ] Context visualization
* [ ] Causal graph
* [ ] Hypothesis explorer

---

# Phase 9 — Plugin Ecosystem

Allow DSCA to support multiple domains.

Potential plugins:

* Automotive
* Motorcycle
* Heavy-duty vehicles
* Industrial systems
* Robotics
* Embedded systems
* Research applications

---

# Version 1.0

The first stable version should be capable of:

* importing diagnostic logs;
* reconstructing system behavior;
* detecting significant events;
* identifying behavioral signatures;
* generating explainable causal hypotheses;
* producing technical reports;
* assisting human reasoning.

---

# Long-Term Vision

DSCA is not intended to become another diagnostic tool.

Its ambition is to become a generic reasoning engine capable of helping humans understand complex dynamic systems through observation, contextualization and explainable causal analysis.

---

**Create the future, not simply tomorrow.**
