"""
DSCA Canonical Signal Model

A Canonical Signal represents the official DSCA definition
of a measurable physical quantity.

Future versions will progressively integrate:

- Physical quantity classification
- Default units
- Metadata
- Documentation
- Registry integration
"""

from dataclasses import dataclass


@dataclass(slots=True)
class CanonicalSignal:
    """
    Official DSCA representation of a measurable quantity.

    Canonical Signals are independent from manufacturers,
    diagnostic tools, languages and naming conventions.
    """

    id: str
    name: str