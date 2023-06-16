# **NATO Phonetic Alphabet Visualizer**

This Python script is a simple application that uses the turtle graphics module and pandas to visualize the NATO phonetic alphabet translation of a user's input word.

## **Requirements**

- Python (This script was written using Python 3.8, but it is likely to work with other versions as well.)
- pandas library
- turtle module (it comes pre-installed with Python)

## **Getting Started**

Before running the script, you need to have Python installed. You can download it from the official website: [Python Downloads](https://www.python.org/downloads/).

You also need the pandas library, which can be installed using pip:

```
pip install pandas
```

Make sure you have a file named `nato_phonetic_alphabet.csv` in the same directory as the script. This file should contain the NATO phonetic alphabet in the following format:

```
letter,code
A,Alfa
B,Bravo
...
Z,Zulu
```

## **How to Use**

1. Save the script into a file named nato_phonetic_visualizer.py.
2. Open a terminal or command prompt, navigate to the directory where the script is located.
3. Run the script using Python:

```
python nato_phonetic_visualizer.py
```

4. A window will pop up with a dark background. It will prompt you to enter a word.
5. Enter a word into the input box and press Enter.
6. The script will convert the word into its NATO phonetic alphabet equivalent and display it on the window.
7. To exit, you can close the window or press CTRL+C in your terminal/command prompt.

## **Example**

If you input the word "Hello", the script will display:

```py
Hello:

['Hotel', 'Echo', 'Lima', 'Lima', 'Oscar']
```

## **Future Improvements**

- Handle invalid input gracefully (e.g., numbers or symbols).
- Allow the user to convert multiple words without restarting the script.
- Add an option to save the output to a text file.

## **Contributing**

Feel free to fork the project and submit a pull request if you have any enhancements or fixes.

## **License**

This project is open source and available under the MIT License.
