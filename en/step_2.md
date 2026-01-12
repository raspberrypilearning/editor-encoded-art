<h2 class="c-project-heading--task">Use the code dictionary to draw shapes</h2>
--- task ---
Expand your encoding dictionary look up letters to draw their matching shapes.
--- /task ---

Add more letters to your encoding look them up in the dictionary to draw the correct shape.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 4
line_highlights: 7-8, 22-32
---
# Define the encoding: each letter maps to [shape name, size, colour]
code = {
    'a': ['shape_1', 150, primary_1],
    'b': ['shape_2', 50, secondary_2],
    'c': ['shape_3', 75, secondary_1],
}

# Get the user's name
print('Enter your name to make some encoded artwork:')
name = input()


# Define the draw function that p5 will call repeatedly
def draw():
    seed(10)  # Generate the same random numbers each time
    no_stroke()
    draw_background()
    
    # Look up the first letter in the code dictionary
    letter = name[0].lower()
    shape_info = code[letter]
    
    # Draw the shape based on what's in the dictionary
    if shape_info[0] == 'shape_1':
        shape_1(shape_info[1], shape_info[2])
    elif shape_info[0] == 'shape_2':
        shape_2(shape_info[1], shape_info[2])
    elif shape_info[0] == 'shape_3':
        shape_3(shape_info[1], shape_info[2])
--- /code ---
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

- `name[0]` gets the first letter of the name
- `code[letter]` looks up that letter in the dictionary
- The `if/elif` statements check which shape to draw
- Try different first letters (a, b, or c) to see different shapes!

</div>

--- /task ---

--- task ---
**Run your code**

Test it by typing names starting with 'a', 'b', or 'c'.

Each first letter should display as a different shape with the size and colour you encoded!

Try "Alice", "Bob", or "Charlie" to see different shapes. 

--- /task ---

<div class="c-project-output">
![A square appears when 'Bob' is entered](images/square.png)
</div>
