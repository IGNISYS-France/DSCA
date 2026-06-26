"""
DSCA Observation Model
"""

from dataclasses import dataclass


@dataclass(slots=True)
class Observation:
    """
    Represents a snapshot of Canonical Signals
    at a specific instant.
    """