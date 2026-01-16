#!/bin/python3

from p5 import *
from helper import *

# Define the encoding: each letter maps to [shape name, size, colour]
code = {
    "a": ["shape 1", 150, primary_1],
    "b": ["shape 3", 50, complementary_3],
    "c": ["shape 3", 75, secondary_1],
    "d": ["shape 2", 80, secondary_1],
    "e": ["shape 1", 20, primary_2],
    "f": ["shape 2", 80, secondary_2],
    "g": ["shape 1", 10, secondary_2],
    "h": ["shape 2", 300, secondary_3],
    "i": ["shape 1", 200, primary_3],
    "j": ["shape 3", 90, secondary_3],
    "k": ["shape 1", 12, complementary_1],
    "l": ["shape 2", 43, complementary_1],
    "m": ["shape 1", 93, complementary_2],
    "n": ["shape 2", 64, complementary_2],
    "o": ["shape 1", 85, primary_4],
    "p": ["shape 2", 10, primary_3],
    "q": ["shape 1", 45, primary_3],
    "r": ["shape 1", 70, primary_4],
    "s": ["shape 1", 36, primary_4],
    "t": ["shape 3", 74, primary_1],
    "u": ["shape 1", 58, primary_3],
    "v": ["shape 2", 78, primary_1],
    "w": ["shape 1", 24, primary_4],
    "x": ["shape 2", 14, primary_4],
    "y": ["shape 3", 67, secondary_2],
    "z": ["shape 2", 70, complementary_2],
    " ": ["shape 1", 25, complementary_1],
}


def draw_artwork(name, encoding_dictionary):
    """Draws the encoded artwork based on the name and encoding dictionary"""
    seed(10)  # Generate the same random numbers each time
    no_stroke()
    draw_background()

    name = name.lower()  # Change the input to lowercase
    message = []  # Initialise the message list

    for letter in name:
        # Encode each letter with a shape and add it to a list
        if letter in encoding_dictionary:
            message.append(encoding_dictionary[letter])

    for item in message:  # For each letter, draw the chosen shape
        if item[0] == "shape 1":
            shape_1(item[1], item[2])
        elif item[0] == "shape 2":
            shape_2(item[1], item[2])
        elif item[0] == "shape 3":
            shape_3(item[1], item[2])


# Get the user's name
print("Enter your name to make some encoded artwork:")
name = input()


# Define the draw function that p5 will call repeatedly
def draw():
    draw_artwork(name, code)


# Run the artwork
run(frame_rate=10)
