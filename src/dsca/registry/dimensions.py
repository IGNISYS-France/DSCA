"""
DSCA Signal Registry
"""

from enum import Enum


class Dimension(str, Enum):
    """Official DSCA physical dimensions."""

    PRESSURE = "pressure"
    TEMPERATURE = "temperature"
    ANGULAR_VELOCITY = "angular_velocity"
    LINEAR_VELOCITY = "linear_velocity"
    ACCELERATION = "acceleration"

    MASS_FLOW = "mass_flow"
    VOLUMETRIC_FLOW = "volumetric_flow"

    VOLTAGE = "voltage"
    CURRENT = "current"
    RESISTANCE = "resistance"

    RATIO = "ratio"
    PERCENTAGE = "percentage"

    TIME = "time"
    FREQUENCY = "frequency"

    POSITION = "position"

    COUNT = "count"

    STATE = "state"

    UNKNOWN = "unknown"