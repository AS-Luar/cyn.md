import tkinter as tk

class AbbreviationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Abbreviation Tool")
        
        # Create a text entry widget
        self.text_entry = tk.Text(root, width=50, height=10)
        self.text_entry.pack(padx=10, pady=10)
        
        # Bind the key release event to check for abbreviations
        self.text_entry.bind("<KeyRelease>", self.check_abbreviation)
        
        # Dictionary of abbreviations and their expansions
        self.abbreviations = {
            "hw": "hello, world",
            # Add more abbreviations here
        }
        
        # Instructions label
        instructions = tk.Label(root, text="Type 'hw' followed by a space to see it expand to 'hello, world'")
        instructions.pack(pady=5)
        
    def check_abbreviation(self, event):
        # Only check when space is pressed
        if event.char == " ":
            # Get the current line of text
            current_line = self.text_entry.get("insert linestart", "insert")
            
            # Check if the line ends with any of our abbreviations followed by a space
            for abbr, expansion in self.abbreviations.items():
                if current_line.endswith(abbr + " "):
                    # Delete the abbreviation and space
                    self.text_entry.delete(f"insert-{len(abbr)+1}c", "insert")
                    # Insert the expansion
                    self.text_entry.insert("insert", expansion + " ")
                    return

if __name__ == "__main__":
    root = tk.Tk()
    app = AbbreviationApp(root)
    root.mainloop()
