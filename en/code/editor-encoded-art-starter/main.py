from p5 import *

# Define the encoding: each letter maps to [shape name, size, colour]
code = {
    "a": ["shape_1", 150, primary_1],
}

# Get the user's name
print("Enter your name to make some encoded artwork:")
name = input()


# Define the draw function that p5 will call repeatedly
def draw():
    seed(10)  # Generate the same random numbers each time
    no_stroke()
    draw_background()

    # Draw one shape from the code
    shape_1(150, primary_1)


# Run the artwork
run(frame_rate=10)
