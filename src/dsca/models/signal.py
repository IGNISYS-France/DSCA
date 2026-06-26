"""
DSCA Signal Model

A Signal represents a measurable quantity handled by DSCA.

Future versions will progressively integrate:

- Units
- Time series
- Validation
- Metadata
- Physical quantity
"""

from dataclasses import dataclass


@dataclass(slots=True)
class Signal:
    """
    Smallest measurable unit handled by DSCA.

    Every Signal references one Canonical Signal defined
    by the DSCA Signal Registry.
    """

    id: str
    canonical_id: str
    name: str