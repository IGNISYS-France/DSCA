"""
DSCA System State Model
"""

from dataclasses import dataclass


@dataclass(slots=True)
class SystemState:
    """
    Represents the complete state of a dynamic system.
    """