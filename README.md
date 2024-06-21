```markdown
# German Flashcards

This is a simple flashcard application built with Python and Tkinter to help you practice German vocabulary. The application reads vocabulary from an Excel file and displays flashcards, allowing you to navigate through the list and flip cards to see translations.

## Features

- **Two Modes**: 
  - **Normal Mode**: Go through the vocabulary in the order read from the Excel file.
  - **Random Mode**: Go through the vocabulary in a random order.
- **Interactive Navigation**:
  - **Left/Right Arrow Keys**: Navigate through the flashcards.
  - **Spacebar**: Flip the flashcard to reveal the English translation.
  - **M Key**: Switch between Normal and Random modes.
  - **Escape Key**: Quit the application.
- **Visual Indicators**:
  - Different background colors for German (light green) and English (light red) words.
  - A status bar that provides instructions on how to use the application.
  
## Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/german-flashcards.git
   cd german-flashcards
   ```

2. **Install the necessary libraries**:
   Make sure you have `pandas` and `openpyxl` installed. You can install them using pip:
   ```sh
   pip install pandas openpyxl
   ```

3. **Prepare your vocabulary file**:
   - Create an Excel file named `vocabulary.xlsx` in the root directory of the project.
   - Ensure the file has two columns: "German" and "English" with appropriate vocabulary.

## Usage

Run the application with the following command:
```sh
python flashcard_app.py
```

### Controls

- **Left/Right Arrow Keys**: Navigate through the flashcards.
- **Spacebar**: Flip the flashcard to reveal the English translation.
- **M Key**: Switch between Normal and Random modes.
- **Escape Key**: Quit the application.

## Example

Ensure your `vocabulary.xlsx` looks like this:

| German | English |
|--------|---------|
| Hund   | Dog     |
| Katze  | Cat     |
| Haus   | House   |

## Customization

You can customize the fonts, colors, and other properties in the `flashcard_app.py` file to suit your preferences.

## Contributing

Feel free to fork this repository and submit pull requests. Any improvements or bug fixes are welcome.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Special thanks to the [Tkinter](https://docs.python.org/3/library/tkinter.html) and [Pandas](https://pandas.pydata.org/) communities for their invaluable libraries and documentation.

---

```
