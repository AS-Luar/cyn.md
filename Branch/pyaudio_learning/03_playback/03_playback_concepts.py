# PyAudio Playback - Core Concepts
'''
This file explains the core concepts of audio playback with PyAudio.
Each section covers important information about playback techniques.

For hands-on practice with these concepts, open the companion file:
-> 03_playback_practice.py
'''

import pyaudio
import wave
import time
import os

# --------------------------------------------------
# SECTION 1: Audio Playback Fundamentals
# --------------------------------------------------

'''
AUDIO PLAYBACK FUNDAMENTALS:

Playing audio with PyAudio follows this general process:
1. Initialize PyAudio
2. Open the audio file (usually a WAV file)
3. Configure and open an output stream
4. Read audio data from the file in chunks
5. Write chunks to the output stream
6. Close everything when done

Key considerations for playback:
- Match stream parameters with the audio file
- Process chunks in a loop until end of file
- Handle resource cleanup properly

To practice playback fundamentals: See EXERCISE 1 in the practice file.
'''

# --------------------------------------------------
# SECTION 2: Reading WAV File Properties
# --------------------------------------------------

'''
READING WAV FILE PROPERTIES:

Before playback, we need to read the WAV file's properties to configure
the output stream correctly:

1. Open the WAV file in read binary mode ('rb')
2. Use wave methods to get:
   - Number of channels (getnchannels())
   - Sample width (getsampwidth())
   - Framerate (getframerate())
   - Number of frames (getnframes())

This ensures our playback matches how the audio was recorded.

To practice reading WAV properties: See EXERCISE 2 in the practice file.
'''

# --------------------------------------------------
# SECTION 3: Basic Audio Playback
# --------------------------------------------------

'''
BASIC AUDIO PLAYBACK:

Simple audio playback works as follows:

1. Read the WAV file properties
2. Configure the output stream to match
3. Open an output stream
4. In a loop:
   - Read a chunk of data from the WAV file
   - Write it to the output stream
   - Continue until no more data
5. Clean up resources when done

The playback is synchronized - your program waits for audio to finish.

To practice basic playback: See EXERCISE 3 in the practice file.
'''

# --------------------------------------------------
# SECTION 4: Non-blocking Playback
# --------------------------------------------------

'''
NON-BLOCKING PLAYBACK:

For more responsive applications, you may want playback to happen
in the background while your program continues other tasks:

1. Use callback-based streams instead of read/write loops
2. Set up a function that PyAudio calls to get more audio
3. The callback returns audio data and a status flag
4. Your main program can continue execution while audio plays

This is useful for GUI applications, games, or any time you need to
perform other tasks during playback.

To practice non-blocking playback: See EXERCISE 4 in the practice file.
'''

# --------------------------------------------------
# SECTION 5: Playback Controls
# --------------------------------------------------

'''
PLAYBACK CONTROLS:

Creating a media player requires implementing playback controls:

1. Play/Pause: Start and temporarily stop playback
2. Stop: End playback completely
3. Seek: Jump to a specific position in the audio
4. Volume: Adjust the audio amplitude

These controls require managing both the audio stream and
keeping track of the current position in the audio file.

To practice playback controls: See EXERCISE 5 in the practice file.
'''

# --------------------------------------------------
# SECTION 6: Playlist and Multiple Files
# --------------------------------------------------

'''
PLAYLIST AND MULTIPLE FILES:

For playback of multiple files in sequence:

1. Create a queue or list of audio files
2. Play each file in succession
3. Properly close and reopen streams between files
4. Provide controls to navigate the playlist

Challenges include seamless transitions, proper resource management,
and maintaining a consistent volume across different files.

To practice playlist functionality: See EXERCISE 6 in the practice file.
'''

# --------------------------------------------------
# SECTION 7: Audio Visualizations
# --------------------------------------------------

'''
AUDIO VISUALIZATIONS:

Visual feedback during playback enhances the user experience:

1. Track the current playback position
2. Display a progress bar or timer
3. Show waveform or spectrum visualizations
4. Implement level meters

These visualizations require analyzing the audio data
while it's being played.

To practice audio visualizations: See EXERCISE 7 in the practice file.
'''

# --------------------------------------------------
# PRACTICE REMINDER
# --------------------------------------------------

print("\nREMINDER:")
print("To practice these playback concepts, open the companion file:")
print("-> 03_playback_practice.py")
print("It contains guided exercises where you write code yourself.")

# =================================================
# END OF FILE
# =================================================
