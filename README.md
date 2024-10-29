# Sierpinski Fractal 

This Python program uses the Turtle graphics library to draw a colorful Sierpinski fractal, a famous recursive geometric figure.

## Overview

The Sierpinski triangle is a fractal with an overall shape of an equilateral triangle, subdivided recursively into smaller equilateral triangles. This project visualizes the Sierpinski triangle using a recursive function in Python, with each triangle randomly colored to enhance the visual appeal.

## Files

- `lab06b_fractal.py`: The main Python file that contains the code for generating the fractal pattern.

## Requirements

- Python 3.x
- Turtle graphics library (included with Python standard library)

## How to Run

1. Make sure you have Python installed on your system.
2. Download the `lab06b_fractal.py` file.
3. Run the program by executing the following command in the terminal or command prompt:
    ```bash
    python lab06b_fractal.py
    ```
4. A Turtle graphics window will open, drawing the colorful Sierpinski fractal pattern. Click anywhere on the window to close it when finished.

## Code Structure

The fractal is created through a recursive function:

- **Base Case**: When `depth` is 0, a filled triangle is drawn with a randomly assigned color.
- **Recursive Case**: The function divides the triangle size in half and draws smaller triangles recursively in each of the three corners.

## Customization

You can customize the following parameters in `lab06b_fractal.py`:

- **`length`**: Adjust the initial size of the triangle.
- **`depth`**: Change the recursion depth to make the fractal more or less detailed. (Default is 5.)

## License

This project is open-source and free to use and modify.

## Author

Developed as a sample project to demonstrate recursive fractal generation with Turtle graphics.
