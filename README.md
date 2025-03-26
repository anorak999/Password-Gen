# Password Generator

A simple GUI-based password generator built with Python and tkinter that offers two password generation modes.

## Features

### 1. Random Password Generator
- Customizable password length
- Options to include/exclude:
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Numbers (0-9)
  - Special symbols (!@#$%, etc.)
- All character types enabled by default for maximum security

### 2. Text Converter
- Converts plain text into a password by replacing letters with similar-looking numbers and symbols
- Conversion examples:
  - 'a' → '@'
  - 'e' → '3'
  - 'i' → '1'
  - 'o' → '0'
  - 's' → '$'
  - 't' → '7'
  - 'b' → '8'
  - 'l' → '1'

## Requirements
- Python 3.x
- tkinter (usually comes with Python)

## How to Run
```bash
python passwordgen.py
```

## Usage
1. Select your desired mode using the radio buttons
2. For Random Password:
   - Set desired password length
   - Select character types using checkboxes
   - Click "Generate Password"
3. For Text Converter:
   - Enter your text in the input field
   - Click "Generate Password"
4. The generated password will appear in the text field at the bottom

## Note
If no character types are selected in Random Password mode, the program defaults to lowercase letters to ensure a password can still be generated.
