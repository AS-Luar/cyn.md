# PyAudio Learning Path - Main Entry Point
'''
Welcome to your PyAudio learning journey!

This file serves as the main entry point to navigate through all the learning materials.
Work through each section in order to build your understanding of PyAudio from basics
to advanced concepts.
'''

import os
import sys
import importlib.util
import time

# --------------------------------------------------
# ENTRY POINT FUNCTIONS
# --------------------------------------------------

def clear_screen():
    '''Clear the terminal screen.'''
    os.system('cls' if os.name == 'nt' else 'clear')


def check_env():
    '''Check if we're running in the virtual environment.'''
    try:
        import pyaudio
        print("✓ PyAudio is correctly installed!")
        return True
    except ImportError:
        print("✗ PyAudio is not installed or not available in this environment.")
        print("\nMake sure your virtual environment is activated:")
        print("  source ../.venv/bin/activate")
        return False


def import_module(file_path):
    '''Dynamically import a Python file as a module.'''
    module_name = os.path.basename(file_path).split('.')[0]
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_module(path, filename):
    '''Run a Python module.'''
    full_path = os.path.join(path, filename)
    
    if not os.path.exists(full_path):
        print(f"Error: File {full_path} not found!")
        return False
    
    try:
        # Add the directory to sys.path so modules can import each other
        module_dir = os.path.dirname(full_path)
        if module_dir not in sys.path:
            sys.path.append(module_dir)
        
        # Import and run the module
        module = import_module(full_path)
        if hasattr(module, '__name__'):
            module.__name__ = '__main__'  # Make module think it's the main module
        
        return True
    
    except Exception as e:
        print(f"Error running {filename}: {e}")
        return False


def section_title(title):
    '''Print a formatted section title.'''
    width = 60
    print("\n" + "=" * width)
    print(title.center(width))
    print("=" * width + "\n")


# --------------------------------------------------
# MAIN MENU AND NAVIGATION
# --------------------------------------------------

def display_sections():
    '''Display the available learning sections.'''
    sections = [
        {"name": "01_basics", "title": "PyAudio Basics", "description": "Fundamental concepts and audio theory"},
        {"name": "02_recording", "title": "Audio Recording", "description": "Recording audio from microphones and devices"},
        {"name": "03_playback", "title": "Audio Playback", "description": "Playing audio files and streams"},
        {"name": "04_audio_processing", "title": "Audio Processing", "description": "Working with audio data and transformations"},
        {"name": "05_advanced", "title": "Advanced Topics", "description": "Callbacks, real-time processing, and more"},
        {"name": "06_challenges", "title": "Practice Challenges", "description": "Test your skills with interactive challenges"}
    ]
    
    print("\nLEARNING SECTIONS")
    print("================")
    
    for i, section in enumerate(sections):
        print(f"{i+1}. {section['title']}")
        print(f"   {section['description']}")
        print()
    
    return sections


def display_files_in_section(section_path):
    '''Display the Python files in a section.'''
    if not os.path.exists(section_path):
        print(f"Error: Section path {section_path} not found!")
        return []
    
    # Get all Python files in the section
    files = [f for f in os.listdir(section_path) if f.endswith('.py')]
    files.sort()  # Sort alphabetically
    
    if not files:
        print("No Python files found in this section!")
        return []
    
    print("\nAvailable Topics:")
    print("================")
    
    # Filter to show only the concept and practice files in our new structure
    concept_file = None
    practice_file = None
    
    for file in files:
        if 'concepts' in file.lower():
            concept_file = file
        elif 'practice' in file.lower():
            practice_file = file
    
    # If we found our structured files, just show those
    if concept_file and practice_file:
        files = [concept_file, practice_file]
        print(f"1. Learn Concepts")
        print(f"2. Practice Exercises")
    else:
        # Fall back to showing all files if we don't have our structured files
        for i, file in enumerate(files):
            # Clean up the filename for display
            display_name = file.replace('.py', '')
            display_name = display_name[3:] if display_name[0:2].isdigit() and display_name[2] == '_' else display_name
            display_name = display_name.replace('_', ' ').title()
            
            print(f"{i+1}. {display_name}")
    
    print()
    return files


def welcome_screen():
    '''Display the welcome screen.'''
    clear_screen()
    print("\n" + "=" * 60)
    print("WELCOME TO THE PYAUDIO LEARNING PATH".center(60))
    print("=" * 60)
    print("\nThis interactive guide will help you learn PyAudio through")
    print("examples, explanations, and hands-on practice.")
    print("\nWork through each section in order to build your understanding")
    print("from the basics to advanced audio programming concepts.")
    print("\nLet's get started!\n")


def main_menu():
    '''Main menu for the learning path.'''
    if not check_env():
        print("\nPlease activate your virtual environment and try again.")
        return
    
    while True:
        sections = display_sections()
        
        choice = input("\nSelect a section (1-6) or 'q' to quit: ")
        
        if choice.lower() == 'q':
            print("\nThank you for exploring the PyAudio Learning Path!")
            print("Happy coding!\n")
            break
        
        try:
            section_idx = int(choice) - 1
            if 0 <= section_idx < len(sections):
                section = sections[section_idx]
                section_path = os.path.join(os.path.dirname(__file__), section["name"])
                
                while True:
                    clear_screen()
                    section_title(section["title"])
                    files = display_files_in_section(section_path)
                    
                    if not files:
                        input("\nPress Enter to return to main menu...")
                        break
                    
                    file_choice = input("\nSelect a topic (number) or 'b' to go back: ")
                    
                    if file_choice.lower() == 'b':
                        break
                    
                    try:
                        file_idx = int(file_choice) - 1
                        if 0 <= file_idx < len(files):
                            clear_screen()
                            print(f"\nLoading {files[file_idx]}...")
                            time.sleep(1)
                            
                            # Run the selected module
                            run_module(section_path, files[file_idx])
                            
                            input("\nPress Enter to return to section menu...")
                        else:
                            print("Invalid selection!")
                            time.sleep(1)
                    except ValueError:
                        print("Please enter a valid number or 'b'.")
                        time.sleep(1)
            else:
                print("Invalid section number!")
                time.sleep(1)
        except ValueError:
            print("Please enter a valid number or 'q'.")
            time.sleep(1)


# --------------------------------------------------
# MAIN EXECUTION
# --------------------------------------------------

if __name__ == "__main__":
    welcome_screen()
    main_menu()
