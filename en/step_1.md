<h2 class="c-project-heading--task">Import the helper</h2>
--- task ---
Import the helper code and creating your first simple encoding.
--- /task ---

The helper file contains all the drawing functions, colours, and the logic to set up the canvas. Your job is to focus on the **encoding** - deciding which letter maps to which shape, size, and colour.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 2
---
from p5 import *
from helper import *

# Define the encoding: each letter maps to [shape name, size, colour]
code = {
    'a': ['shape_1', 150, primary_1],
}

# Get the user's name
print('Enter your name to make some encoded artwork:')
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
--- /code ---
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

- The `code` dictionary maps each letter to: `['shape name', size, colour]`
- Start simple with just the letter 'a' - you'll add more letters in the next steps
- The colours like `primary_1`, `primary_2`, etc. are defined in the helper file

</div>

--- /task ---

--- task ---
**Run your code**

Test it by typing a name with only the letter 'a' in it (like "aaa").

You should see a large circle appear on the screen!

--- /task ---

<div class="c-project-output">
![A large circle](images/circle.png)
</div>

