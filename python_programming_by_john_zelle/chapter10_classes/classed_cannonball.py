from python_programming_by_john_zelle.chapter10_classes.cannonball import get_inputs


def main():
    angle, vel, h0, time = get_inputs()
    cannon_ball = Projectile(angle, velocity, h0)
    while cannon_ball.y >= 0:
        cannon_ball.update(time)
    print('\nDistance traveled: {0:0.1f} meters.'.format(cannon_ball.x()))


class Projectile:
    def __init__(self, angle, velocity, height):
        pass
