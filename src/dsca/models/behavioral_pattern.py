"""
DSCA System State Model
"""

from dataclasses import dataclass

@dataclass(slots=True)
class BehavioralPattern:
    """
    Represents a recurring organization of Events.
    """