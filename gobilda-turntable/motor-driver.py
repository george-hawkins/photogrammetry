from time import sleep
import board
from digitalio import DigitalInOut, Direction

DIR = DigitalInOut(board.D9)
DIR.direction = Direction.OUTPUT

STEP = DigitalInOut(board.D8)
STEP.direction = Direction.OUTPUT

SPR = 200

ratio = 48 / 16
step_count = SPR * ratio
delay = 0.01

for x in range(step_count):
    STEP.value = True
    sleep(delay)
    STEP.value = False
    sleep(delay)

sleep(0.5)
DIR.value = not DIR.value

for x in range(step_count):
    STEP.value = True
    sleep(delay)
    STEP.value = False
    sleep(delay)
