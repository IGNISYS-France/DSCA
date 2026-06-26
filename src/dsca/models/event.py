"""
DSCA Event Model
"""

from dataclasses import dataclass


@dataclass(slots=True)
class Event:
    """
    Represents a meaningful evolution inferred
    from one or more Signals.
    """