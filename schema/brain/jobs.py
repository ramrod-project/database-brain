"""

"""


STATES = frozenset([["Ready", "Pending", "Done", "Error", "Stopped", "Waiting"]])


def verify_state(state):
    return state in STATES