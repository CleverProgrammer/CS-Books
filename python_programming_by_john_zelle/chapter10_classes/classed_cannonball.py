from python_programming_by_john_zelle.chapter10_classes.cannonball import *
import math
GRAVITY = 9.8


class Projectile:
    def __init__(self, angle, velocity, height):
        self.x_pos, self.y_pos = 0.0, height
        theta = math.radians(angle)
        self.x_velocity, self.y_velocity = velocity * math.cos(theta), velocity * math.sin(theta)

    def update(self, time):
        self.x_pos += time * self.x_velocity
        y_velocity1 = self.y_velocity - time * GRAVITY
        self.y_pos += time * (self.y_velocity + y_velocity1) / 2.0
        self.y_velocity = y_velocity1


def get_inputs():
    angle = float(input('Enter the launch angle (in degrees): '))
    velocity = float(input('Enter the initial velocity (in meters/sec): '))
    h0 = float(input('Enter the initial height (in meters): '))
    time = float(input('Enter the time interval between position calculations: '))
    return angle, velocity, h0, time


def main():
    angle, velocity, h0, time = get_inputs()
    cannon_ball = Projectile(angle, velocity, h0)
    while cannon_ball.y_pos >= 0:
        cannon_ball.update(time)
    print('\nDistance traveled: {0:0.1f} meters.'.format(cannon_ball.x()))


obj = Projectile(45, 50, 0)
print(obj.y_velocity)
