"""
DSCA System State Model
"""

from dataclasses import dataclass


@dataclass(slots=True)
class DiagnosticCode:
    """
    Represents a standardized diagnostic code.
    """