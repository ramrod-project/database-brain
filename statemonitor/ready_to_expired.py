from time import sleep, time
import os
import sys
from random import randint

_path = os.path.abspath(os.path.join(os.path.abspath(__file__), "../../"))+"/schema"
sys.path.append(_path)

from brain.queries.writes import transition_expired


CHECKING_PERIOD = 3  # seconds


if __name__ == "__main__":
    while True:
        try:
            transition_expired(time())
        except ValueError:
           pass  # forget it and restart
        sleep(randint(CHECKING_PERIOD-1, CHECKING_PERIOD+1))  # thundering herd

