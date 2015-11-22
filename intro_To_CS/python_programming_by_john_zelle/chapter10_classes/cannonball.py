import python_programming_by_john_zelle.chapter10_classes.graphics as graphics
import math


def main():
    win, my_cannon = draw_cannon()
    angle, velocity, h0, time = get_inputs()
    x_pos, y_pos = 0, h0
    x_velocity, y_velocity = xy_components(velocity, angle)
    while y_pos >= 0.0:
        x_pos, y_pos, y_velocity = update_cannon_ball(time, x_pos, y_pos, x_velocity, y_velocity)
        move_cannon(win, my_cannon, x_pos, y_pos)
    print('\nDistance traveled {0:0.1f} meters'.format(x_pos))


def get_inputs():
    """
    Get user inputs and return them
    :return: tuple
    """
    angle = float(input('Enter the launch angle (in degrees): '))
    velocity = float(input('Enter the initial velocity (in meters/sec): '))
    h0 = float(input('Enter the initial height (in meters): '))
    time = float(input('Enter the time interval between position calculations: '))
    return angle, velocity, h0, time


def xy_components(velocity, angle):
    """
    Take as input the velocity and angle of an object and return it's velocity in each direction
    :param velocity: float
    :param angle: float
    :return: tuple
    """
    theta = math.radians(angle)
    x_velocity = velocity * math.cos(theta)
    y_velocity = velocity * math.sin(theta)
    return x_velocity, y_velocity


def update_cannon_ball(time, x_pos, y_pos, x_velocity, y_velocity):
    """
    Take in the time, position and of the object in x/y direction, and return the new
    x and y positons. Also return the updated y_velocity.
    :param time: float
    :param x_pos: float
    :param y_pos: float
    :param x_velocity: float
    :param y_velocity: float
    :return: tuple
    """
    x_pos += time * x_velocity
    y_velocity1 = y_velocity - time * 9.8
    y_pos += time * (y_velocity + y_velocity) / 2.0
    y_velocity = y_velocity1
    return x_pos, y_pos, y_velocity


def draw_cannon():
    """"
    Creates and returns a window and a cannon object
    """
    win = graphics.GraphWin(title='Cannonball!', width=400, height=400)
    my_cannon = graphics.Circle(graphics.Point(400, 400), 20)
    my_cannon.draw(win)
    return win, my_cannon


def move_cannon(Window, Circle, x_pos, y_pos):
    """
    Move the cannon on the screen with the given x, y positions
    :param Circle:
    :param x_pos:
    :param y_pos:
    :return:
    """
    Window.getMouse()
    Circle.move(-x_pos, -y_pos)


def in_circle(mouse_xy, circle_xy, radius):
    """
    Takes the position of the mouse and the circle origin and returns True
    if mouseclick was within the circle and False if the click was outside.
    :param mouse_point: object
    :param circle_origin: object
    :param radius: int
    :return: boolean
    """
    return math.sqrt((mouse_point.x - circle_origin.x) ** 2 + (mouse_point.y - circle_origin.y) ** 2) < radius


def moving_circle():
    win = graphics.GraphWin('THE GAME OF GAMES!')
    circle_origin = graphics.Point(100, 100)
    my_circle = graphics.Circle(circle_origin, 20)
    my_circle.draw(win)
    for i in range(10):
        try:
            my_circle.move(8, 8)
            mouse_position = win.getMouse()
            print('You clicked at', mouse_position.getX(), mouse_position.getY())
            print('Radius', my_circle.getRadius())
            if in_circle(mouse_position, my_circle.getCenter(), my_circle.radius):
                print('You clicked inside the circle!')
        except GraphicsError:
            print('You closed the graphics window!')
            return


# moving_circle()



if __name__ == '__main__':
    main()

# EXAMPLE PROGRAM
# def main():
#     win = GraphWin("Click Me!")
#     for i in range(10):
#         try:
#             p = win.getMouse()
#             print('You clicked at', p.getX(), p.getY())
#         except GraphicsError:
#             print('You closed the graphics window!')
#             return
#
# main()
