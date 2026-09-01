from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait, StopWatch
import math

WHEEL_DIAMETER = 54  # mm

class PID:
    def __init__(self, kp, ki, kd, integral_limit=None):
        self.kp, self.ki, self.kd = kp, ki, kd
        self.integral_limit = integral_limit
        self.integral = 0
        self.last_error = 0

    def reset(self):
        self.integral = 0
        self.last_error = 0

    def update(self, error, dt):
        self.integral += error * dt
        if self.integral_limit is not None:
            self.integral = max(-self.integral_limit, min(self.integral_limit, self.integral))
        derivative = (error - self.last_error) / dt if dt > 0 else 0
        self.last_error = error
        return self.kp * error + self.ki * self.integral + self.kd * derivative


def move_straight(hub, left_motor, right_motor, distance_mm, speed):
    heading_pid = PID(kp=2.0, ki=0.0, kd=0.1, integral_limit=20)
    hub.imu.reset_heading(0)

    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    target_angle = (distance_mm / (math.pi * WHEEL_DIAMETER)) * 360

    timer = StopWatch()
    last_time = timer.time()

    while (abs(left_motor.angle()) + abs(right_motor.angle())) / 2 < target_angle:
        now = timer.time()
        dt = (now - last_time) / 1000
        last_time = now

        error = 0 - hub.imu.heading()
        correction = heading_pid.update(error, dt)

        left_motor.run(speed - correction)
        right_motor.run(speed + correction)
        wait(10)

    left_motor.brake()
    right_motor.brake()
