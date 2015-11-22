from python_programming_by_john_zelle.chapter10_classes.graphics import *
import math


def in_circle(mouse_point, circle_origin, radius):
    """
    Takes the position of the mouse and the circle origin and returns True
    if mouseclick was within the circle and False if the click was outside.
    :param mouse_point: object
    :param circle_origin: object
    :param radius: int
    :return: boolean
    """
    return math.sqrt((mouse_point.x - circle_origin.x) ** 2 + (mouse_point.y - circle_origin.y) ** 2) < radius


def main():
    win = GraphWin('THE GAME OF GAMES!')
    circle_origin = Point(100, 100)
    my_circle = Circle(circle_origin, 20)
    my_circle.draw(win)
    for i in range(10):
        try:
            my_circle.move(2, 2)
            mouse_position = win.getMouse()
            print('You clicked at', mouse_position.getX(), mouse_position.getY())
            print('Radius', my_circle.getRadius())
            if in_circle(mouse_position, my_circle.getCenter(), my_circle.radius):
                print('You clicked inside the circle!')
        except GraphicsError:
            print('You closed the graphics window!')
            return


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
