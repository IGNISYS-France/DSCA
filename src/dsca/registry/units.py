from enum import Enum


class Unit(str, Enum):
    """Official DSCA Canonical Units."""

    BAR = "bar"
    DEG = "deg"
    DEGC = "degC"
    PERCENT = "%"
    RPM = "rpm"
    KMH = "km/h"
    GS = "g/s"
    LAMBDA = "lambda"
    VOLT = "V"
    AMPERE = "A"
    OHM = "ohm"
    COUNT = "count"
    SECOND = "s"
    MILLISECOND = "ms"

    @property
    def symbol(self) -> str:
        """Human-readable display symbol."""

        return {
            Unit.DEG: "°",
            Unit.DEGC: "°C",
            Unit.PERCENT: "%",
            Unit.BAR: "bar",
            Unit.RPM: "rpm",
            Unit.KMH: "km/h",
            Unit.GS: "g/s",
            Unit.LAMBDA: "λ",
            Unit.VOLT: "V",
            Unit.AMPERE: "A",
            Unit.OHM: "Ω",
            Unit.COUNT: "",
            Unit.SECOND: "s",
            Unit.MILLISECOND: "ms",
        }[self]