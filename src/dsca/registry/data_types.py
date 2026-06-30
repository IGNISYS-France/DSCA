"""
DSCA Signal Registry
"""

from enum import Enum


class DataType(str, Enum):
    """Official DSCA canonical data types."""

    FLOAT = "float"

    INTEGER = "integer"

    BOOLEAN = "boolean"

    STRING = "string"

    ENUM = "enum"