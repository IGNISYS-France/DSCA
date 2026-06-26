🇬🇧 **English** | [🇫🇷 Français](LEXICON.fr.md)

---

# DSCA Lexicon

> **The official language of the DSCA reasoning engine.**

The purpose of this document is to define the official vocabulary used throughout the DSCA project.

Every contributor should refer to this document before introducing new terminology.

---

## Conceptual Flow

```text
Dynamic System
        │
        ▼
Signals
        │
        ▼
Observations
        │
        ▼
Context
        │
        ▼
System State
        │
        ▼
Events
        │
        ▼
Behavioral Patterns
        │
        ▼
Causal Chains
        │
        ▼
Hypotheses
        │
        ▼
Knowledge
        │
        ▼
Understanding
        │
        ▼
Exploration
```

---

# Fundamental Concepts

---

# Signal

## Definition

A Signal is the smallest measurable unit handled by DSCA.

It represents the evolution of a physical, logical or calculated quantity over time.

Every Signal references one Canonical Signal defined by the DSCA Signal Registry.

## Purpose

Signals are the raw observations from which every higher-level concept is built.

## Relationships

* Signals reference Canonical Signals.
* Signal evolution may generate Events.
* Signals form Observations.

## Examples

* Engine Speed
* Rail Pressure
* Lambda
* Knock Level
* Coolant Temperature
* Accelerator Position

---

# Canonical Signal

## Definition

A Canonical Signal is the official DSCA representation of a measurable physical quantity.

It provides a unique identifier independent of manufacturers, diagnostic tools, languages or naming conventions.

Every Signal handled by DSCA references one Canonical Signal.

## Purpose

Provide a common language shared by every importer, reasoning engine and visualization component.

Canonical Signals allow heterogeneous data sources to describe the same physical phenomenon consistently.

## Example

Canonical Signal:

* Engine Speed

Possible aliases:

* RPM
* Engine RPM
* Motordrehzahl
* Régime moteur
* PID 0C
* N_ENGINE

---

# Signal Alias

## Definition

A Signal Alias is an alternative name used by a manufacturer, diagnostic tool or data source to describe a Canonical Signal.

Multiple aliases may refer to the same physical quantity.

## Purpose

Allow DSCA to recognize identical Signals originating from heterogeneous sources.

Aliases never influence reasoning.

They are only used during observation acquisition and normalization.

## Relationships

Signal Aliases belong to a Canonical Signal.

Importers resolve aliases through the DSCA Signal Registry.

---

# DSCA Signal Registry

## Definition

The DSCA Signal Registry is the canonical vocabulary used throughout the project.

It maps every known Signal Alias to one Canonical Signal.

The registry represents the translation layer between external data sources and the internal language of DSCA.

## Purpose

Provide a universal language independently of:

* manufacturers;
* diagnostic tools;
* file formats;
* languages;
* naming conventions.

## Responsibilities

* Define Canonical Signals.
* Store Signal Aliases.
* Define standard measurement units.
* Associate physical quantities.
* Categorize Signals.
* Store Signal metadata.
* Support future community contributions.

## Relationships

The DSCA Signal Registry is used by:

* Importers
* Observation Acquisition
* Observation Normalization
* Signal Validation
* Reasoning Engine
* Visualization

## Guiding Principle

DSCA never reasons on manufacturer-specific names.

DSCA always reasons on Canonical Signals.

---

# Observation

## Definition

A complete snapshot of every available Signal at a specific instant.

## Purpose

Represent the complete measurable state of a system.

## Relationships

* An Observation contains Signals.
* Observations belong to a Context.
* Multiple Observations describe system evolution.

---

# Context

## Definition

The set of environmental, operational or configuration conditions surrounding Observations.

## Purpose

Provide meaning to Signals and Observations.

Without Context, observations cannot be correctly interpreted.

## Examples

* Fuel type
* Ambient temperature
* Engine temperature
* Vehicle configuration
* Air conditioning state
* Calibration version

---

# System State

## Definition

The complete condition of a system during a specific period of time.

It combines:

* Observations
* Context
* Active Events

## Purpose

Represent what the system is experiencing.

---

# Interpretation Concepts

---

# Event

## Definition

A significant evolution detected from one or more Signals.

Events are not measured.

They are inferred.

## Purpose

Reduce continuous data into meaningful changes.

## Examples

* Pressure drop
* Pressure recovery
* Knock detected
* Torque limitation
* Misfire detected
* Sensor incoherence

---

# Behavioral Pattern

## Definition

A recurring organization of Events describing how a system behaves.

Behavioral Patterns are independent from manufacturers.

They describe physics rather than implementations.

## Purpose

Represent behaviors instead of isolated measurements.

## Examples

* Fuel starvation under load
* Thermal limitation
* Oscillating pressure regulation
* Ignition instability

---

# Causal Chain

## Definition

An ordered sequence of Events linked by plausible physical relationships.

## Purpose

Describe how one event may lead to another.

A Causal Chain is the foundation of hypothesis building.

---

# Causal Hypothesis

## Definition

An explainable interpretation of one or more Behavioral Patterns.

A hypothesis always remains provisional.

## Purpose

Assist reasoning.

Never replace it.

---

# Confidence Level

## Definition

An estimation of how strongly available observations support a hypothesis.

## Purpose

Rank competing hypotheses.

Confidence never represents certainty.

---

# Knowledge Concepts

---

# Validation

## Definition

The process of confirming or rejecting a hypothesis using additional observations or experiments.

## Purpose

Separate plausible explanations from validated knowledge.

---

# Experiment

## Definition

A deliberate modification performed in order to validate or invalidate one or more hypotheses.

## Purpose

Transform hypotheses into knowledge.

## Examples

* Disable air conditioning
* Increase fuel pressure
* Repeat the test
* Replace a component
* Perform oscilloscope measurements

---

# Knowledge

## Definition

Validated understanding obtained through repeated observations and successful experiments.

## Purpose

Provide reliable foundations for future reasoning.

Knowledge always remains open to revision when new evidence appears.

---

# Explanation

## Definition

A human-readable description generated by DSCA.

## Purpose

Explain:

* what happened;
* why it happened;
* which observations support the reasoning;
* which uncertainties remain;
* which additional tests are recommended.

---

# Reasoning

## Definition

The process of constructing coherent hypotheses from observations while respecting physical principles.

Reasoning is transparent.

Reasoning is explainable.

Reasoning is always open to revision.

---

# Understanding

## Definition

The coherent interpretation of a dynamic system based on observations, context, events, behavioral patterns and validated hypotheses.

## Purpose

Understanding is the ultimate objective of DSCA.

It is never absolute.

It continuously evolves as new observations become available.

---

# Exploration

## Definition

The iterative process of observing, contextualizing, reasoning, experimenting and refining understanding through evidence.

## Purpose

Explore the behavior of dynamic systems without assuming conclusions beforehand.

Exploration is the foundation of learning within DSCA.

---

# Domain Concepts

---

# Dynamic System

## Definition

Any system whose state evolves over time.

## Examples

* Internal combustion engine
* Electric powertrain
* Motorcycle
* Industrial machine
* Robot
* Hydraulic system

---

# DSCA

## Definition

Dynamic System Causal Analysis.

An open-source reasoning engine dedicated to understanding dynamic systems through observations, contextualization and explainable causal analysis.

DSCA does not replace human expertise.

It extends the ability to explore complex systems.

---

# Guiding Principle

**Words define concepts.**

**Concepts define architecture.**

**Architecture defines software.**

Every new feature introduced into DSCA must remain consistent with this Lexicon.
