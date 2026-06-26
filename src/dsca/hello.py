"""
DSCA — Dynamic System Causal Analysis

Development Banner
"""
from pathlib import Path


def count_canonical_signals() -> int:
    """
    Return the number of Canonical Signal definitions
    currently available in the embedded registry.
    """

    directory = (
        Path(__file__).parent
        / "data"
        / "canonical_signals"
    )

    return len(list(directory.glob("*.yaml")))

def hello():
    print("=" * 56)
    print("           Dynamic System Causal Analysis")
    print("                          DSCA")
    print("=" * 56)
    print()
    print("Development Version : 0.1.0-dev \"Observation\"")
    print("Project Status      : Active Development")
    print(f"Canonical Signals : {count_canonical_signals()}")
    print()
    print("Current Mission")
    print("  Observe.")
    print("  Understand.")
    print("  Explore.")
    print()
    print("Next Milestone      : Contextualization")
    print()
    print("IGNISYS — OPEN SOURCE PROJECT")
    print("Create the future, not simply tomorrow.")


if __name__ == "__main__":
    
     hello()