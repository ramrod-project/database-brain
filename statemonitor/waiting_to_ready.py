from time import sleep, time
from random import randint
import pathfix  # appears unused but don't remove!

from brain.queries.writes import transition_waiting


CHECKING_PERIOD = 3  # seconds

if __name__ == "__main__":
    while True:
        try:
            transition_waiting(time())
        except ValueError:
           pass  # forget it and restart
        sleep(randint(CHECKING_PERIOD - 1, CHECKING_PERIOD + 1))
