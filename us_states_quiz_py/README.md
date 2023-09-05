# **US States Game**

This is a Python program that allows users to play a game where they guess the names of different states in the United States. The program utilizes the Turtle module to create a graphical interface and the pandas library to read and manipulate data from a CSV file.

## **Requirements**

To run this program, you need to have the following installed:

- Python 3.x
- Turtle module
- pandas library

## **Installation**

1. Clone or download the repository to your local machine.
2. Make sure you have Python installed.
3. Install the required dependencies by running the following command:

```
pip install pandas
```

## **Usage**

1. Open a terminal or command prompt.
2. Navigate to the directory where the program files are located.
3. Run the following command to start the game:

```
python main.py
```

4. A window titled "US States Game" will appear with a blank map of the United States.
5. The program will prompt you to guess a state by displaying a dialog box. Enter the name of a state and press Enter.
6. If your guess is correct, the state's name will be displayed on the map in red, and your score will increase by 1.
7. Repeat steps 4 and 5 until you have guessed all 50 states or you decide to quit by typing "Quit" as your guess.

The game keeps track of your score and displays it at the top right corner of the screen.

If you exit the game before guessing all the states, a CSV file named **states_to_learn.csv** will be created. This file contains the names of the states you haven't guessed yet.

## **Customization**

You can customize the game by modifying the following aspects:

- Window size: In the screen.setup(width, height) line of the main.py file, you can change the width and height values to adjust the size of the game window.
  Background color: The background color of the game window is set using the screen.bgcolor(color) line. You can change the color parameter to any valid color code or color name.
- State name font: The font used for displaying the state names on the map is set in the turtle.write function call within the check_answer function. You can modify the font parameters to change the appearance of the text.
- Scoreboard font: The font used for displaying the user's score is set in the Scoreboard.display_score method. You can modify the font parameters to change the appearance of the text.

## **Acknowledgments**

The game was inspired by the "U.S. States Game" project from the "100 Days of Code - The Complete Python Pro Bootcamp" course by Dr. Angela Yu.

The state names and coordinates are sourced from the 50_states.csv file, which is based on publicly available data.

## **License**

This project is licensed under the MIT License - see the LICENSE file for details.
