# JSON Editor

This is a Python program that allows you to remove keys from a JSON file.

## How to Use

1. Install Python 3 if you don't already have it installed.
2. Clone or download the repository to your computer.
3. Open a terminal or command prompt and navigate to the directory where the repository is located.
4. Run the program by typing `python main.py input_file output_file --key_to_remove KEY_TO_REMOVE --text OUTPUT_TXT`, where:
   - `input_file` is the path to the JSON file you want to edit
   - `output_file` is the path to the output file that will be generated
   - `KEY_TO_REMOVE` is the name of the key you want to remove from the JSON file
   - `OUTPUT_TXT` is an optional argument that allows you to write the remaining keys or values to a text file
5. Press Enter to run the program.
6. Check the output file to make sure that the specified key has been removed.


## Examples

Here are some examples of how you can use the program:

python main.py input.json output.json --k age -t nigga.txt


This command removes the `city` key from the `input.json` file and saves the edited file as `output.json`.


```py
python main.py input.json output.json --k age
```


This command removes the `city` key from the `input.json` file, saves the edited file as `output.json`, and writes the remaining keys to `remaining.txt`.

## Contributions

Contributions to this program are welcome! If you find a bug or have a suggestion for how to improve the program, please create an issue or submit a pull request.
