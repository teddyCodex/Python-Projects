# **Turtle Spirograph**

This Python program uses the turtle module to create a colorful spirograph drawing. The spirograph is a geometric drawing toy that produces intricate and symmetrical patterns. Each pattern is created by drawing circles and rotating the turtle by a certain angle.

## Prerequisites

Before running this program, make sure you have Python installed on your machine. You can download the latest version of Python from the official website: python.org.

## Installation

1. Clone the repository or download the Python script.
2. Open a terminal or command prompt.
3. Navigate to the directory where the script is located.
4. Run the following command to execute the script:

```
python spirograph.py
```

## Usage

Once the program is running, a turtle window will appear displaying the spirograph drawing. The turtle starts at the center of the screen and creates colorful circles while rotating by a specified angle.

The **draw_spiro(spacing)** function controls the spirograph creation. It takes an argument spacing, which determines the angle by which the turtle rotates after drawing each circle. Adjusting this value will result in different patterns.

## Customization

You can customize the spirograph drawing by modifying the following aspects of the code:

- **tim.speed(0)**: Adjust the speed of the turtle. Higher values make it faster.
- **tim.circle(100)**: Change the radius of the circles. A larger radius will create bigger patterns.
- **draw_spiro(5)**: Change the spacing value to control the rotation angle. Experiment with different values for unique designs.

## Dependencies

This program requires the following Python modules:

- **turtle**: The turtle graphics module that provides a drawing board and methods for creating graphics.
- **random.randint**: A function that generates random integers within a specified range.

These modules are part of Python's standard library and should be available by default.

## Contributing

If you have suggestions, improvements, or bug fixes, please feel free to contribute! Fork this repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute the code as needed.
