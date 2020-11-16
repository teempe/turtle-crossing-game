"""Utility functions to create nice looking game board. """

from turtle import Turtle

line = Turtle()
line.hideturtle()
line.speed("fastest")
line.pensize(2)


def draw_dashed_line(start_pos, end_pos):
    """
    Draws white dashed line between given points.

    Arguments
    ---------
    start_pos : pair of numbers
        coordinates of starting point.
    end_pos : pair of numbers
        coordinates of end point
    """

    line.color("white")
    xs, ys = start_pos
    xe, ye = end_pos
    line.penup()
    line.goto(xs, ys)
    line.pendown()

    cur_x = xs
    while cur_x <= xe:
        cur_x += 40
        line.goto(cur_x, ys)
        line.penup()
        cur_x += 20
        line.goto(cur_x, ys)
        line.pendown()


def draw_lanes():
    """Draws paving, verges and median strip."""

    # Draw road verges
    line.color("white", "green")
    # Bottom verge
    points = ((300, -220), (-300, -220), (-300, -300), (300, -300), (300, -220))
    line.begin_fill()
    line.penup()
    for point in points:
        line.goto(point)
        line.pendown()
    line.end_fill()

    # Median strip
    points = ((300, -20), (-300, -20), (-300, 20), (300, 20), (300, -20))
    line.begin_fill()
    line.penup()
    for point in points:
        line.goto(point)
        line.pendown()
    line.end_fill()

    # Top verge
    points = ((300, 220), (-300, 220), (-300, 300), (300, 300), (300, 220))
    line.begin_fill()
    line.penup()
    for point in points:
        line.goto(point)
        line.pendown()
    line.end_fill()

    # Draw top lanes
    for start_y in range(20, 220, 40):
        draw_dashed_line((-300, start_y), (300, start_y))

    # Draw bottom lanes
    for start_y in range(-20, -220, -40):
        draw_dashed_line((-300, start_y), (300, start_y))
