# PyScramble - Advanced Python Code Obfuscator

PyScramble is a Python code obfuscator with:

- Function & variable renaming
- String encryption (XOR + base64)
- Dummy code injection (to confuse analyzers)
- GUI frontend
- CLI support
- Local pip install option

--

To obfuscate what you want open the examples folder and open "sample_input.py" and paste your code in there and then go back to the main folder and run the CLI or the GUI version to obfuscate the code into "sample_output." Now you can open "sample_output" to view your obfuscated code!

## Install Locally

```bash
pip install .
```

## CLI Usage

```bash
python obfuscator.py --input examples/sample_input.py --output examples/sample_output.py --encrypt-strings --inject-dummy
```

## GUI

Run the GUI (Main way to use program):

```bash
python gui.py
```

Choose input/output, toggle features, and click Obfuscate!

MIT License © Fahad Majidi
