"""PyBricks for LEGO SPIKE Hub"""
from pybricks.pupdevices import Motor, ForceSensor, Remote
from pybricks.parameters import Port, Direction, Button
from pybricks.hubs import PrimeHub
from pybricks.tools import wait, Matrix

ANGRY_FACE = Matrix(
    [
        [100, 100,  0,   100,  100],
        [0,   100,  0,   100,  0],
        [0,   0,    0,   0,    0],
        [100, 100,  100, 100,  100],
        [100, 0,    0,   0,    100],
    ]
)

SPEED = 500

hub = PrimeHub()
hub.display.icon(ANGRY_FACE)

button = ForceSensor(Port.F)
remote = Remote()

# Initialize motors on port A and B.
right_motor = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)
left_motor = Motor(Port.B, positive_direction=Direction.CLOCKWISE)

def autopilot():
    """Run Autopilot"""
    while Button.RIGHT not in remote.buttons.pressed():
        if button.force() == 0:
            left_motor.run(SPEED)
            right_motor.run(SPEED)
        else:
            right_motor.run(-SPEED)
            left_motor.run(-SPEED)
            wait(1000)
            right_motor.run(-SPEED)
            left_motor.run(SPEED)
            wait(1000)

def run():
    """Run Tank from RC controls"""
    while Button.RIGHT not in remote.buttons.pressed():
        pressed = remote.buttons.pressed()

        if button.force() > 0 or len(pressed) == 0:
            left_motor.stop()
            right_motor.stop()
        else:
            if Button.LEFT_PLUS in pressed:
                left_motor.run(SPEED)
                right_motor.run(SPEED)
            if Button.LEFT_MINUS in pressed:
                left_motor.run(-SPEED)
                right_motor.run(-SPEED)
            if Button.RIGHT_PLUS in pressed:
                right_motor.run(SPEED)
                left_motor.run(-SPEED)
            if Button.RIGHT_MINUS in pressed:
                right_motor.run(-SPEED)
                left_motor.run(SPEED)

        wait(200)

while True:
    while Button.RIGHT not in remote.buttons.pressed():
        run()

    autopilot()
