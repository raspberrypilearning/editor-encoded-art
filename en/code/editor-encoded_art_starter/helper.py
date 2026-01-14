#!/bin/python3

from p5 import *
from random import randint, seed

# -- Colour palette -- Using primary, secondary and complementary colours
# Stored as RGB tuples to avoid Color constructor issues at import time

# Primary colours
primary_1 = (14, 92, 151)
primary_2 = (77, 135, 179)
primary_3 = (45, 111, 161)
primary_4 = (8, 71, 120)
primary_5 = (5, 55, 93)

# Secondary colours
secondary_1 = (29, 29, 164)
secondary_2 = (92, 92, 191)
secondary_3 = (60, 60, 176)

# Complementary colours
complementary_1 = (234, 137, 8)
complementary_2 = (255, 188, 99)
complementary_3 = (251, 168, 57)


def shape_1(size, colour):
    """Draws a circle with a thick outline"""
    x = randint(0, 400)
    y = randint(0, 400)
    fill(*colour)
    ellipse(x, y, size, size)
    fill(251, 168, 57)
    ellipse(x, y, size - 20, size - 20)


def shape_2(size, colour):
    """Draws a rectangle"""
    x = randint(0, 400)
    y = randint(0, 400)
    fill(*colour)
    rect(x, y, size, size)


def shape_3(size, colour):
    """Draws a triangle"""
    x = randint(0, 400)
    y = randint(0, 400)
    fill(*colour)
    triangle(x, y, x + 50, y - 100, x + 100, y)


def draw_background():
    """Draws the background"""
    fill(5, 55, 93)
    rect(0, 0, 400, 400)


def setup():
    """Sets up the canvas"""
    size(400, 400)
