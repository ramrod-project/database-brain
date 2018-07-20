from time import sleep, time
import os
import sys

_path = os.path.abspath(os.path.join(os.path.abspath(__file__), "../../"))+"/schema"
sys.path.append(_path)

from brain.queries.writes import transition_waiting


CHECKING_PERIOD = 3  # seconds


if __name__ == "__main__":
    while True:
        try:
            transition_waiting(time())
        except ValueError:
           pass  # forget it and restart
        sleep(CHECKING_PERIOD)

