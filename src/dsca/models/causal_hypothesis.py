"""
DSCA System State Model
"""

from dataclasses import dataclass

@dataclass(slots=True)
class CausalHypothesis:
    """
    Represents an explainable technical hypothesis.
    """