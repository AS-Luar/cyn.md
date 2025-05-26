import keyboard

# Register an abbreviation that replaces 'hw' with 'hello, world'
keyboard.add_abbreviation('hw', 'hello, world')

# Keep the program running to detect keystrokes
print("Abbreviation 'hw' registered. Type 'hw' followed by a space to see it in action.")

# This will keep the program running
keyboard.wait()