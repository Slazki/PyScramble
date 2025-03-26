# PyScramble - Advanced Python Code Obfuscator

PyScramble is a Python code obfuscator with:

- Function & variable renaming
- String encryption (XOR + base64)
- Dummy code injection (to confuse analyzers)
- GUI frontend
- CLI support
- Local pip install option

## Install Locally

```bash
pip install .
```

## CLI Usage

```bash
pyscramble --input script.py --output script_obf.py --encrypt-strings --inject-dummy
```

## GUI

Run the GUI (Main way to use program):

```bash
python gui.py
```

Choose input/output, toggle features, and click Obfuscate!

MIT License © Fahad Majidi
