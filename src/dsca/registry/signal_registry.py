"""
DSCA Signal Registry
"""

from pathlib import Path

from dsca.models.canonical_signal import CanonicalSignal


class SignalRegistry:
    """
    Official DSCA Canonical Signal Registry.
    """

    def __init__(self) -> None:

        self.signals: dict[str, CanonicalSignal] = {}
        self.aliases: dict[str, str] = {}