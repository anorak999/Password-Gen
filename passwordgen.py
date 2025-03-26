import tkinter as tk
from tkinter import ttk
import random
import string

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x400")  # Made window taller to accommodate new options
        
        # Style
        self.root.configure(bg='#f0f0f0')
        style = ttk.Style()
        style.configure('TButton', padding=5)
        
        # Mode selection
        self.mode_label = tk.Label(root, text="Select Mode:", bg='#f0f0f0')
        self.mode_label.pack(pady=10)
        
        self.mode_var = tk.StringVar(value="random")
        self.random_mode = ttk.Radiobutton(root, text="Random Password", variable=self.mode_var, 
                                         value="random", command=self.toggle_mode)
        self.random_mode.pack()
        
        self.convert_mode = ttk.Radiobutton(root, text="Convert Text", variable=self.mode_var, 
                                          value="convert", command=self.toggle_mode)
        self.convert_mode.pack()
        
        # Length input for random mode
        self.length_frame = tk.Frame(root, bg='#f0f0f0')
        self.length_frame.pack(pady=10)
        self.length_label = tk.Label(self.length_frame, text="Password Length:", bg='#f0f0f0')
        self.length_label.pack(side=tk.LEFT)
        self.length_entry = ttk.Entry(self.length_frame, width=5)
        self.length_entry.insert(0, "12")
        self.length_entry.pack(side=tk.LEFT, padx=5)
        
        # Text input for convert mode
        self.text_frame = tk.Frame(root, bg='#f0f0f0')
        self.text_frame.pack(pady=10)
        self.text_label = tk.Label(self.text_frame, text="Enter Text:", bg='#f0f0f0')
        self.text_label.pack()
        self.text_entry = ttk.Entry(self.text_frame, width=30)
        self.text_entry.pack(pady=5)
        self.text_frame.pack_forget()
        
        # Add checkbox frame for random password options
        self.random_options_frame = tk.Frame(root, bg='#f0f0f0')
        self.random_options_frame.pack(pady=5)
        
        # Checkbox variables
        self.use_uppercase = tk.BooleanVar(value=True)
        self.use_lowercase = tk.BooleanVar(value=True)
        self.use_numbers = tk.BooleanVar(value=True)
        self.use_symbols = tk.BooleanVar(value=True)
        
        # Checkboxes
        self.uppercase_check = ttk.Checkbutton(self.random_options_frame, 
            text="Uppercase (A-Z)", variable=self.use_uppercase)
        self.lowercase_check = ttk.Checkbutton(self.random_options_frame, 
            text="Lowercase (a-z)", variable=self.use_lowercase)
        self.numbers_check = ttk.Checkbutton(self.random_options_frame, 
            text="Numbers (0-9)", variable=self.use_numbers)
        self.symbols_check = ttk.Checkbutton(self.random_options_frame, 
            text="Symbols (!@#$%)", variable=self.use_symbols)
        
        self.uppercase_check.pack(anchor='w')
        self.lowercase_check.pack(anchor='w')
        self.numbers_check.pack(anchor='w')
        self.symbols_check.pack(anchor='w')
        
        # Generate button
        self.generate_btn = ttk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_btn.pack(pady=10)
        
        # Result
        self.result_label = tk.Label(root, text="Generated Password:", bg='#f0f0f0')
        self.result_label.pack(pady=5)
        self.result_text = tk.Text(root, height=1, width=30)
        self.result_text.pack()

    def toggle_mode(self):
        if self.mode_var.get() == "random":
            self.text_frame.pack_forget()
            self.length_frame.pack(pady=10)
            self.random_options_frame.pack(pady=5)
        else:
            self.length_frame.pack_forget()
            self.random_options_frame.pack_forget()
            self.text_frame.pack(pady=10)

    def generate_random_password(self, length):
        # Build character set based on selected options
        characters = ''
        if self.use_uppercase.get():
            characters += string.ascii_uppercase
        if self.use_lowercase.get():
            characters += string.ascii_lowercase
        if self.use_numbers.get():
            characters += string.digits
        if self.use_symbols.get():
            characters += string.punctuation
            
        # If no options selected, default to lowercase
        if not characters:
            characters = string.ascii_lowercase
            
        return ''.join(random.choice(characters) for _ in range(length))

    def convert_to_password(self, text):
        replacements = {
            'a': '@', 'e': '3', 'i': '1', 'o': '0',
            's': '$', 't': '7', 'b': '8', 'l': '1'
        }
        result = ''
        for char in text.lower():
            result += replacements.get(char, char)
        return result

    def generate_password(self):
        self.result_text.delete(1.0, tk.END)
        
        if self.mode_var.get() == "random":
            try:
                length = int(self.length_entry.get())
                if length < 1:
                    raise ValueError
                password = self.generate_random_password(length)
            except ValueError:
                password = "Please enter a valid length"
        else:
            text = self.text_entry.get()
            if text:
                password = self.convert_to_password(text)
            else:
                password = "Please enter some text"
                
        self.result_text.insert(tk.END, password)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
