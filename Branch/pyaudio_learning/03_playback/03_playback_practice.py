# PyAudio Playback - Practice Exercises
'''
This file contains hands-on practice exercises for audio playback with PyAudio.
Work through each exercise and write the code yourself to learn by doing.

First read the corresponding section in the concepts file:
-> 03_playback_concepts.py

Then complete the exercises here to practice what you've learned.
'''

# -----------------------------------------------------
# EXERCISE 1: Audio Playback Fundamentals
# -----------------------------------------------------

'''
EXERCISE 1: Basic WAV File Playback

In this exercise, you'll create a simple audio player that:
1. Opens a WAV file
2. Configures and opens an output stream
3. Plays the audio from the file

STEPS:
- Import required modules
- Open a WAV file and read its properties
- Create a PyAudio instance
- Configure and open an output stream
- Play the audio data
- Clean up resources when done

Write your code below and uncomment to run:
'''

# Your code for Exercise 1:
import pyaudio
import wave
import time
import os
#

"""Play a WAV file using PyAudio"""

# Check if file exists

filename = input("Enter WAV file to play (or press Enter for test.wav): ")

if not os.path.exists(filename):
    print(f"Error: File '{filename}' not found")


    # Open the WAV file
#     try:
#         wf = wave.open(filename, 'rb')
#     except wave.Error:
#         print(f"Error: '{filename}' is not a valid WAV file")
#         return
#     
#     # Get file properties
#     channels = wf.getnchannels()
#     sample_width = wf.getsampwidth()
#     framerate = wf.getframerate()
#     frames = wf.getnframes()
#     
#     # Calculate duration
#     duration = frames / framerate
#     
#     # Display file information
#     print(f"Playing: {filename}")
#     print(f"Channels: {channels}")
#     print(f"Sample Width: {sample_width} bytes")
#     print(f"Sample Rate: {framerate} Hz")
#     print(f"Duration: {duration:.2f} seconds")
#     
#     # Initialize PyAudio
#     p = pyaudio.PyAudio()
#     
#     # Open stream
#     stream = p.open(
#         format=p.get_format_from_width(sample_width),
#         channels=channels,
#         rate=framerate,
#         output=True
#     )
#     
#     # Define chunk size
#     chunk = 1024
#     
#     # Play audio
#     print("Playing audio...")
#     data = wf.readframes(chunk)
#     
#     while data:
#         stream.write(data)
#         data = wf.readframes(chunk)
#     
#     print("Playback complete")
#     
#     # Clean up
#     stream.stop_stream()
#     stream.close()
#     wf.close()
#     p.terminate()
#





#     # Example usage
#     # If you don't have a WAV file, you can create one with the recording exercises
#     filename = input("Enter WAV file to play (or press Enter for test.wav): ")
#     if not filename:
#         filename = "test.wav"
#     
#     basic_audio_player(filename)


# -----------------------------------------------------
# EXERCISE 2: Working with WAV File Properties
# -----------------------------------------------------

'''
EXERCISE 2: WAV File Analyzer

In this exercise, you'll:
1. Create a utility to analyze WAV files
2. Extract and display detailed file properties
3. Calculate additional information from the properties

STEPS:
- Import required modules
- Open a WAV file and read its properties
- Calculate additional information (duration, bit rate, etc.)
- Display the information in a user-friendly format

Write your code below and uncomment to run:
'''

# Your code for Exercise 2:
# import wave
# import os
# import datetime
#
# def wav_file_analyzer(filename):
#     """Analyze and display detailed information about a WAV file"""
#     # Check if file exists
#     if not os.path.exists(filename):
#         print(f"Error: File '{filename}' not found")
#         return
#     
#     # Open the WAV file
#     try:
#         wf = wave.open(filename, 'rb')
#     except wave.Error:
#         print(f"Error: '{filename}' is not a valid WAV file")
#         return
#     
#     # Basic properties
#     channels = wf.getnchannels()
#     sample_width = wf.getsampwidth()
#     framerate = wf.getframerate()
#     n_frames = wf.getnframes()
#     comp_type = wf.getcomptype()
#     comp_name = wf.getcompname()
#     
#     # Calculate derived properties
#     duration_seconds = n_frames / framerate
#     duration = str(datetime.timedelta(seconds=duration_seconds))
#     bits_per_sample = sample_width * 8
#     bitrate = framerate * channels * bits_per_sample
#     file_size = os.path.getsize(filename)
#     
#     # Display file information
#     print("\n" + "=" * 50)
#     print(f"WAV FILE ANALYSIS: {filename}")
#     print("=" * 50)
#     print(f"File Size: {file_size} bytes ({file_size/1024/1024:.2f} MB)")
#     print(f"Last Modified: {datetime.datetime.fromtimestamp(os.path.getmtime(filename))}")
#     print("\nAudio Properties:")
#     print(f"  Channels: {channels} ({'Mono' if channels == 1 else 'Stereo' if channels == 2 else f'{channels} channels'})")
#     print(f"  Sample Width: {sample_width} bytes ({bits_per_sample} bits)")
#     print(f"  Sample Rate: {framerate} Hz")
#     print(f"  Frames: {n_frames}")
#     print(f"  Duration: {duration} ({duration_seconds:.2f} seconds)")
#     print(f"  Bitrate: {bitrate/1000:.1f} kbps")
#     
#     if comp_type != 'NONE':
#         print(f"  Compression: {comp_type} ({comp_name})")
#     else:
#         print("  Compression: None (uncompressed PCM)")
#     
#     # Additional information
#     print("\nTechnical Details:")
#     print(f"  Data Chunk Size: {n_frames * channels * sample_width} bytes")
#     print(f"  Header Size: {file_size - (n_frames * channels * sample_width)} bytes")
#     print(f"  Samples: {n_frames * channels}")
#     print(f"  Bytes per Second: {framerate * channels * sample_width}")
#     
#     # Close the file
#     wf.close()
#     
#     print("=" * 50)
#
# if __name__ == "__main__":
#     # Example usage
#     filename = input("Enter WAV file to analyze (or press Enter for test.wav): ")
#     if not filename:
#         filename = "test.wav"
#     
#     wav_file_analyzer(filename)


# -----------------------------------------------------
# EXERCISE 3: Audio Playback with Progress Display
# -----------------------------------------------------

'''
EXERCISE 3: Audio Player with Progress Bar

In this exercise, you'll:
1. Create an audio player that shows playback progress
2. Display a text-based progress bar and time information
3. Show audio level during playback

STEPS:
- Open and configure playback as in Exercise 1
- Add code to track and display the current position
- Create a text-based progress bar
- Update it in real-time during playback

Write your code below and uncomment to run:
'''

# Your code for Exercise 3:
# import pyaudio
# import wave
# import time
# import os
# import struct
#
# def player_with_progress(filename):
#     """Play a WAV file with progress bar and level meter"""
#     # Check if file exists
#     if not os.path.exists(filename):
#         print(f"Error: File '{filename}' not found")
#         return
#     
#     # Open the WAV file
#     try:
#         wf = wave.open(filename, 'rb')
#     except wave.Error:
#         print(f"Error: '{filename}' is not a valid WAV file")
#         return
#     
#     # Get file properties
#     channels = wf.getnchannels()
#     sample_width = wf.getsampwidth()
#     framerate = wf.getframerate()
#     n_frames = wf.getnframes()
#     duration = n_frames / framerate
#     
#     # Initialize PyAudio
#     p = pyaudio.PyAudio()
#     
#     # Open stream
#     stream = p.open(
#         format=p.get_format_from_width(sample_width),
#         channels=channels,
#         rate=framerate,
#         output=True
#     )
#     
#     # Define chunk size and terminal width for progress bar
#     chunk = 1024
#     try:
#         term_width = os.get_terminal_size().columns - 30
#     except:
#         term_width = 40
#     
#     # Play audio with progress
#     print(f"Playing: {filename}")
#     print(f"Duration: {duration:.2f} seconds")
#     print()
#     
#     # Variables to track progress
#     frames_played = 0
#     start_time = time.time()
#     
#     # Read and play
#     data = wf.readframes(chunk)
#     
#     while data:
#         # Write data to stream
#         stream.write(data)
#         
#         # Update frame count
#         frames_played += chunk
#         if frames_played > n_frames:
#             frames_played = n_frames
#         
#         # Calculate progress
#         progress = frames_played / n_frames
#         elapsed = time.time() - start_time
#         remaining = duration - elapsed
#         
#         # Calculate audio level (simple amplitude)
#         if sample_width == 2:  # 16-bit audio
#             format_str = f"{min(chunk, len(data)//2)}h"
#             try:
#                 values = struct.unpack(format_str, data[:len(data)//2*2])
#                 amplitude = sum(abs(v) for v in values) / len(values)
#                 level = min(1.0, amplitude / 10000)  # Normalize
#             except:
#                 level = 0
#         else:
#             level = 0
#         
#         # Create progress bar
#         bar_length = int(term_width * progress)
#         bar = "█" * bar_length + "▒" * (term_width - bar_length)
#         
#         # Create level meter
#         level_bar = "▮" * int(level * 20)
#         
#         # Print progress and level
#         print(f"[{bar}] {progress*100:5.1f}% | {elapsed:.1f}s / {duration:.1f}s | Level: {level_bar}", 
#               end="\r", flush=True)
#         
#         # Read next chunk
#         data = wf.readframes(chunk)
#     
#     print("\nPlayback complete")
#     
#     # Clean up
#     stream.stop_stream()
#     stream.close()
#     wf.close()
#     p.terminate()
#
# if __name__ == "__main__":
#     # Example usage
#     filename = input("Enter WAV file to play (or press Enter for test.wav): ")
#     if not filename:
#         filename = "test.wav"
#     
#     player_with_progress(filename)


# -----------------------------------------------------
# EXERCISE 4: Non-blocking Playback with Callbacks
# -----------------------------------------------------

'''
EXERCISE 4: Non-blocking Audio Player

In this exercise, you'll:
1. Create an audio player that uses callbacks for non-blocking playback
2. Allow the program to perform other tasks while audio plays
3. Implement simple commands during playback

STEPS:
- Set up a callback function to provide audio data
- Configure the stream to use this callback
- Implement a simple command processor during playback

Write your code below and uncomment to run:
'''

# Your code for Exercise 4:
# import pyaudio
# import wave
# import time
# import sys
# import os
#
# def non_blocking_player(filename):
#     """Play a WAV file using callbacks for non-blocking playback"""
#     # Check if file exists
#     if not os.path.exists(filename):
#         print(f"Error: File '{filename}' not found")
#         return
#     
#     # Open the WAV file
#     try:
#         wf = wave.open(filename, 'rb')
#     except wave.Error:
#         print(f"Error: '{filename}' is not a valid WAV file")
#         return
#     
#     # Get file properties
#     channels = wf.getnchannels()
#     sample_width = wf.getsampwidth()
#     framerate = wf.getframerate()
#     
#     # Initialize PyAudio
#     p = pyaudio.PyAudio()
#     
#     # Variable to track if audio is still playing
#     playing = True
#     paused = False
#     start_time = None
#     
#     # Callback function for audio data
#     def callback(in_data, frame_count, time_info, status):
#         nonlocal playing
#         
#         if paused:
#             # If paused, return empty data and continue status
#             data = b'\x00' * (frame_count * channels * sample_width)
#             return (data, pyaudio.paContinue)
#         
#         data = wf.readframes(frame_count)
#         
#         if len(data) < frame_count * channels * sample_width:
#             # End of file, pad with silence as needed
#             data += b'\x00' * (frame_count * channels * sample_width - len(data))
#             playing = False
#             return (data, pyaudio.paComplete)
#         
#         return (data, pyaudio.paContinue)
#     
#     # Open stream using callback
#     stream = p.open(
#         format=p.get_format_from_width(sample_width),
#         channels=channels,
#         rate=framerate,
#         output=True,
#         stream_callback=callback
#     )
#     
#     # Start the stream
#     stream.start_stream()
#     start_time = time.time()
#     
#     print(f"Now playing: {filename}")
#     print("The audio is playing in the background.")
#     print("You can type these commands while it plays:")
#     print("  p - Pause/resume playback")
#     print("  i - Show file information")
#     print("  q - Quit playback")
#     
#     # Process user input while audio plays
#     try:
#         command = None
#         while stream.is_active() or paused:
#             # Check for commands
#             if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
#                 command = sys.stdin.readline().strip().lower()
#                 
#                 if command == 'p':
#                     paused = not paused
#                     print("Playback PAUSED" if paused else "Playback RESUMED")
#                 elif command == 'i':
#                     duration = wf.getnframes() / framerate
#                     elapsed = time.time() - start_time
#                     print(f"\nFile: {filename}")
#                     print(f"Duration: {duration:.2f} seconds")
#                     print(f"Elapsed: {elapsed:.2f} seconds")
#                     print(f"Remaining: {max(0, duration - elapsed):.2f} seconds")
#                 elif command == 'q':
#                     print("Stopping playback...")
#                     break
#             
#             # Print a period every second to show we're still running
#             print(".", end="", flush=True)
#             time.sleep(1)
#     
#     except KeyboardInterrupt:
#         print("\nPlayback interrupted")
#     
#     # Clean up
#     stream.stop_stream()
#     stream.close()
#     wf.close()
#     p.terminate()
#     
#     print("\nPlayback ended")
#
# # Required for non-blocking input
# import select
#
# if __name__ == "__main__":
#     # Example usage
#     filename = input("Enter WAV file to play (or press Enter for test.wav): ")
#     if not filename:
#         filename = "test.wav"
#     
#     non_blocking_player(filename)


# -----------------------------------------------------
# EXERCISE 5: Playback Controls
# -----------------------------------------------------

'''
EXERCISE 5: Audio Player with Controls

In this exercise, you'll:
1. Create a more advanced player with play, pause, and seek controls
2. Implement volume adjustment
3. Allow jumping to specific points in the audio

STEPS:
- Enhance the player from Exercise 3 or 4
- Add functions to control playback
- Handle user input to trigger controls
- Implement seeking by calculating frame positions

Write your code below and uncomment to run:
'''

# Your code for Exercise 5:
# import pyaudio
# import wave
# import time
# import sys
# import os
# import select
# import struct
#
# class AudioPlayer:
#     """Audio player with controls for play, pause, seek, and volume"""
#     
#     def __init__(self, filename):
#         # Check if file exists
#         if not os.path.exists(filename):
#             raise FileNotFoundError(f"File '{filename}' not found")
#         
#         # Open the WAV file
#         try:
#             self.wf = wave.open(filename, 'rb')
#         except wave.Error:
#             raise ValueError(f"'{filename}' is not a valid WAV file")
#         
#         # Get file properties
#         self.channels = self.wf.getnchannels()
#         self.sample_width = self.wf.getsampwidth()
#         self.framerate = self.wf.getframerate()
#         self.n_frames = self.wf.getnframes()
#         self.duration = self.n_frames / self.framerate
#         self.filename = filename
#         
#         # Initialize PyAudio
#         self.p = pyaudio.PyAudio()
#         
#         # Playback state
#         self.playing = False
#         self.paused = False
#         self.volume = 1.0
#         self.current_position = 0
#         self.chunk = 1024
#         self.stream = None
#         self.start_time = None
#         self.elapsed_time = 0
#     
#     def __del__(self):
#         """Clean up resources when object is deleted"""
#         self.stop()
#         if hasattr(self, 'p') and self.p:
#             self.p.terminate()
#         if hasattr(self, 'wf') and self.wf:
#             self.wf.close()
#     
#     def start(self):
#         """Start or resume playback"""
#         if not self.playing:
#             # If not currently playing, initialize everything
#             self.stream = self.p.open(
#                 format=self.p.get_format_from_width(self.sample_width),
#                 channels=self.channels,
#                 rate=self.framerate,
#                 output=True
#             )
#             self.playing = True
#             self.start_time = time.time() - self.elapsed_time
#         
#         self.paused = False
#     
#     def stop(self):
#         """Stop playback completely"""
#         if self.stream:
#             self.stream.stop_stream()
#             self.stream.close()
#             self.stream = None
#         
#         self.playing = False
#         self.paused = False
#     
#     def pause(self):
#         """Pause playback"""
#         if self.playing and not self.paused:
#             self.paused = True
#             self.elapsed_time = time.time() - self.start_time
#     
#     def seek(self, position_seconds):
#         """Seek to the specified position in seconds"""
#         position_seconds = max(0, min(position_seconds, self.duration))
#         frame_pos = int(position_seconds * self.framerate)
#         
#         # Update state
#         self.current_position = position_seconds
#         self.elapsed_time = position_seconds
#         
#         # Set file position
#         self.wf.setpos(frame_pos)
#         
#         # Update start time to reflect new position
#         if self.playing and not self.paused:
#             self.start_time = time.time() - position_seconds
#     
#     def set_volume(self, volume):
#         """Set playback volume (0.0 to 1.0)"""
#         self.volume = max(0.0, min(1.0, volume))
#     
#     def adjust_samples(self, data):
#         """Adjust sample volume"""
#         if self.volume == 1.0:
#             return data  # No adjustment needed
#             
#         # Convert to samples
#         if self.sample_width == 2:  # 16-bit
#             format_str = f"{len(data) // 2}h"
#             samples = list(struct.unpack(format_str, data))
#             
#             # Apply volume
#             adjusted = [int(s * self.volume) for s in samples]
#             
#             # Convert back to bytes
#             return struct.pack(format_str, *adjusted)
#         else:
#             # For simplicity, only handling 16-bit audio
#             return data
#     
#     def play(self):
#         """Main playback loop"""
#         if not self.playing:
#             self.start()
#         
#         print(f"Playing: {self.filename}")
#         print(f"Duration: {self.duration:.2f} seconds")
#         print("\nCommands:")
#         print("  p - Pause/resume")
#         print("  s - Seek (followed by seconds)")
#         print("  v - Volume (followed by 0-100)")
#         print("  q - Quit")
#         
#         try:
#             # Terminal width for progress bar
#             try:
#                 term_width = os.get_terminal_size().columns - 30
#             except:
#                 term_width = 40
#             
#             while self.playing:
#                 if not self.paused:
#                     # Read and play a chunk
#                     data = self.wf.readframes(self.chunk)
#                     
#                     if not data:
#                         # End of file reached
#                         print("\nEnd of playback reached")
#                         self.stop()
#                         break
#                     
#                     # Adjust volume if needed
#                     if self.volume != 1.0:
#                         data = self.adjust_samples(data)
#                     
#                     # Play audio
#                     self.stream.write(data)
#                     
#                     # Update current position
#                     self.current_position = self.wf.tell() / self.framerate
#                 
#                 # Update display
#                 if self.playing:  # Check again in case we stopped in the loop
#                     if not self.paused:
#                         self.elapsed_time = time.time() - self.start_time
#                     
#                     remaining = max(0, self.duration - self.elapsed_time)
#                     progress = self.elapsed_time / self.duration if self.duration > 0 else 0
#                     
#                     # Create progress bar
#                     bar_length = int(term_width * progress)
#                     bar = "█" * bar_length + "▒" * (term_width - bar_length)
#                     
#                     status = "PAUSED" if self.paused else "PLAYING"
#                     vol_bar = "▮" * int(self.volume * 10)
#                     
#                     print(f"[{bar}] {progress*100:5.1f}% | {status} | "
#                           f"{self.elapsed_time:.1f}s / {self.duration:.1f}s | "
#                           f"Vol: {vol_bar}", end="\r", flush=True)
#                 
#                 # Check for user input
#                 if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
#                     command = sys.stdin.readline().strip().lower()
#                     
#                     if command == 'p':
#                         if self.paused:
#                             self.start()
#                             print("\nResumed playback")
#                         else:
#                             self.pause()
#                             print("\nPaused playback")
#                     
#                     elif command.startswith('s'):
#                         try:
#                             # Extract seconds from command (e.g., "s 30")
#                             parts = command.split()
#                             if len(parts) > 1:
#                                 seek_pos = float(parts[1])
#                                 self.seek(seek_pos)
#                                 print(f"\nSeeked to {seek_pos:.1f} seconds")
#                         except ValueError:
#                             print("\nInvalid seek position")
#                     
#                     elif command.startswith('v'):
#                         try:
#                             # Extract volume from command (e.g., "v 75")
#                             parts = command.split()
#                             if len(parts) > 1:
#                                 vol = float(parts[1]) / 100.0
#                                 self.set_volume(vol)
#                                 print(f"\nVolume set to {vol*100:.0f}%")
#                         except ValueError:
#                             print("\nInvalid volume level")
#                     
#                     elif command == 'q':
#                         print("\nStopping playback")
#                         self.stop()
#                         break
#                 
#                 # Brief pause to prevent high CPU usage
#                 if self.paused:
#                     time.sleep(0.1)
#         
#         except KeyboardInterrupt:
#             print("\nPlayback interrupted")
#             self.stop()
#
# if __name__ == "__main__":
#     try:
#         # Example usage
#         filename = input("Enter WAV file to play (or press Enter for test.wav): ")
#         if not filename:
#             filename = "test.wav"
#         
#         player = AudioPlayer(filename)
#         player.play()
#     
#     except (FileNotFoundError, ValueError) as e:
#         print(f"Error: {e}")
#     except Exception as e:
#         print(f"Unexpected error: {e}")


# -----------------------------------------------------
# EXERCISE 6: Playlist Management
# -----------------------------------------------------

'''
EXERCISE 6: Playlist Player

In this exercise, you'll:
1. Create a player that handles a playlist of audio files
2. Provide controls to navigate between tracks
3. Display playlist information
4. Allow reordering and saving playlists

STEPS:
- Create a playlist class to manage a list of audio files
- Integrate it with your player to handle multiple files
- Implement controls to navigate the playlist

Write your code below and uncomment to run:
'''

# Your code for Exercise 6:
# import pyaudio
# import wave
# import time
# import sys
# import os
# import select
# import json
#
# class Playlist:
#     """Class to manage a list of audio files for playback"""
#     
#     def __init__(self):
#         self.tracks = []  # List of track filenames
#         self.current_index = -1
#         self.name = "New Playlist"
#     
#     def add_track(self, filename):
#         """Add a track to the playlist"""
#         if os.path.exists(filename) and filename.lower().endswith('.wav'):
#             self.tracks.append(filename)
#             return True
#         return False
#     
#     def remove_track(self, index):
#         """Remove a track from the playlist"""
#         if 0 <= index < len(self.tracks):
#             del self.tracks[index]
#             # Adjust current index if needed
#             if self.current_index >= len(self.tracks) and self.tracks:
#                 self.current_index = len(self.tracks) - 1
#             return True
#         return False
#     
#     def get_current_track(self):
#         """Get the current track filename"""
#         if 0 <= self.current_index < len(self.tracks):
#             return self.tracks[self.current_index]
#         return None
#     
#     def next_track(self):
#         """Move to the next track and return its filename"""
#         if self.tracks:
#             self.current_index = (self.current_index + 1) % len(self.tracks)
#             return self.get_current_track()
#         return None
#     
#     def previous_track(self):
#         """Move to the previous track and return its filename"""
#         if self.tracks:
#             self.current_index = (self.current_index - 1) % len(self.tracks)
#             return self.get_current_track()
#         return None
#     
#     def get_playlist_info(self):
#         """Get information about the playlist"""
#         info = []
#         for i, track in enumerate(self.tracks):
#             marker = "▶" if i == self.current_index else " "
#             info.append(f"{marker} {i+1}. {os.path.basename(track)}")
#         return "\n".join(info)
#     
#     def save_playlist(self, filename):
#         """Save playlist to a file"""
#         data = {
#             "name": self.name,
#             "tracks": self.tracks,
#         }
#         
#         try:
#             with open(filename, 'w') as f:
#                 json.dump(data, f)
#             return True
#         except:
#             return False
#     
#     def load_playlist(self, filename):
#         """Load playlist from a file"""
#         try:
#             with open(filename, 'r') as f:
#                 data = json.load(f)
#                 
#                 self.name = data.get("name", "Loaded Playlist")
#                 self.tracks = []
#                 
#                 # Verify and add each track
#                 for track in data.get("tracks", []):
#                     if os.path.exists(track):
#                         self.tracks.append(track)
#                 
#                 self.current_index = 0 if self.tracks else -1
#                 return True
#         except:
#             return False
#
# class PlaylistPlayer:
#     """Audio player that handles playlists"""
#     
#     def __init__(self):
#         self.playlist = Playlist()
#         self.p = pyaudio.PyAudio()
#         self.stream = None
#         self.wf = None
#         self.playing = False
#         self.paused = False
#         self.current_track = None
#     
#     def __del__(self):
#         """Clean up resources"""
#         self.stop()
#         if hasattr(self, 'p') and self.p:
#             self.p.terminate()
#     
#     def play_current_track(self):
#         """Play the current track in the playlist"""
#         # Stop any current playback
#         self.stop()
#         
#         # Get the current track
#         filename = self.playlist.get_current_track()
#         if not filename:
#             print("No track to play")
#             return False
#         
#         try:
#             # Open the WAV file
#             self.wf = wave.open(filename, 'rb')
#             self.current_track = filename
#             
#             # Get file properties
#             channels = self.wf.getnchannels()
#             sample_width = self.wf.getsampwidth()
#             framerate = self.wf.getframerate()
#             
#             # Open stream
#             self.stream = self.p.open(
#                 format=self.p.get_format_from_width(sample_width),
#                 channels=channels,
#                 rate=framerate,
#                 output=True
#             )
#             
#             self.playing = True
#             self.paused = False
#             return True
#         
#         except Exception as e:
#             print(f"Error playing track: {e}")
#             self.stop()
#             return False
#     
#     def stop(self):
#         """Stop playback"""
#         if self.stream:
#             self.stream.stop_stream()
#             self.stream.close()
#             self.stream = None
#         
#         if self.wf:
#             self.wf.close()
#             self.wf = None
#         
#         self.playing = False
#         self.paused = False
#         self.current_track = None
#     
#     def pause(self):
#         """Pause playback"""
#         self.paused = not self.paused
#     
#     def next_track(self):
#         """Play the next track"""
#         next_track = self.playlist.next_track()
#         if next_track:
#             return self.play_current_track()
#         return False
#     
#     def previous_track(self):
#         """Play the previous track"""
#         prev_track = self.playlist.previous_track()
#         if prev_track:
#             return self.play_current_track()
#         return False
#     
#     def run(self):
#         """Main player loop"""
#         print("Playlist Player")
#         print("==============")
#         
#         # Main command loop
#         running = True
#         while running:
#             print("\nCommands:")
#             print("  add <file> - Add a WAV file to playlist")
#             print("  play - Play current track")
#             print("  next - Play next track")
#             print("  prev - Play previous track")
#             print("  pause - Pause/resume playback")
#             print("  stop - Stop playback")
#             print("  list - Show playlist")
#             print("  save <file> - Save playlist")
#             print("  load <file> - Load playlist")
#             print("  quit - Exit player")
#             
#             command = input("\nEnter command: ").strip().lower()
#             
#             if command.startswith('add '):
#                 filename = command[4:].strip()
#                 if self.playlist.add_track(filename):
#                     print(f"Added track: {os.path.basename(filename)}")
#                 else:
#                     print("Invalid file or not a WAV file")
#             
#             elif command == 'play':
#                 if self.play_current_track():
#                     filename = self.current_track
#                     print(f"Playing: {os.path.basename(filename)}")
#                     
#                     # Simple playback loop
#                     try:
#                         chunk = 1024
#                         while self.playing:
#                             if not self.paused:
#                                 data = self.wf.readframes(chunk)
#                                 if not data:
#                                     # End of track, auto-play next
#                                     print("\nTrack finished")
#                                     if not self.next_track():
#                                         break
#                                 else:
#                                     self.stream.write(data)
#                             
#                             # Check for commands
#                             if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
#                                 cmd = sys.stdin.readline().strip().lower()
#                                 
#                                 if cmd == 'pause':
#                                     self.pause()
#                                     print("PAUSED" if self.paused else "RESUMED")
#                                 elif cmd == 'next':
#                                     self.next_track()
#                                 elif cmd == 'prev':
#                                     self.previous_track()
#                                 elif cmd == 'stop':
#                                     self.stop()
#                                     break
#                                 elif cmd == 'quit':
#                                     self.stop()
#                                     running = False
#                                     break
#                             
#                             # Sleep to prevent high CPU usage
#                             time.sleep(0.01)
#                     
#                     except KeyboardInterrupt:
#                         print("\nPlayback interrupted")
#                         self.stop()
#                 
#             elif command == 'next':
#                 if self.next_track():
#                     print(f"Playing next track: {os.path.basename(self.current_track)}")
#                 else:
#                     print("No next track available")
#             
#             elif command == 'prev':
#                 if self.previous_track():
#                     print(f"Playing previous track: {os.path.basename(self.current_track)}")
#                 else:
#                     print("No previous track available")
#             
#             elif command == 'pause':
#                 if self.playing:
#                     self.pause()
#                     print("PAUSED" if self.paused else "RESUMED")
#                 else:
#                     print("No track is playing")
#             
#             elif command == 'stop':
#                 self.stop()
#                 print("Playback stopped")
#             
#             elif command == 'list':
#                 if self.playlist.tracks:
#                     print(f"\nPlaylist: {self.playlist.name}")
#                     print(self.playlist.get_playlist_info())
#                 else:
#                     print("Playlist is empty")
#             
#             elif command.startswith('save '):
#                 filename = command[5:].strip()
#                 if self.playlist.save_playlist(filename):
#                     print(f"Playlist saved to {filename}")
#                 else:
#                     print("Failed to save playlist")
#             
#             elif command.startswith('load '):
#                 filename = command[5:].strip()
#                 if self.playlist.load_playlist(filename):
#                     print(f"Playlist loaded from {filename}")
#                     print(f"Loaded {len(self.playlist.tracks)} tracks")
#                 else:
#                     print("Failed to load playlist")
#             
#             elif command == 'quit':
#                 running = False
#             
#             else:
#                 print("Unknown command")
#         
#         print("Exiting player")
#
# if __name__ == "__main__":
#     player = PlaylistPlayer()
#     player.run()


# -----------------------------------------------------
# EXERCISE 7: Audio Visualizer
# -----------------------------------------------------

'''
EXERCISE 7: Simple Audio Visualizer

In this exercise, you'll:
1. Create a basic audio visualizer using terminal graphics
2. Analyze audio data during playback to display visual patterns
3. Show real-time spectrum or waveform visualization

STEPS:
- Set up audio playback
- Implement a simple visualization algorithm
- Display the visualization in real-time during playback

Write your code below and uncomment to run:
'''

# Your code for Exercise 7:
# import pyaudio
# import wave
# import time
# import os
# import struct
# import math
# 
# def terminal_audio_visualizer(filename):
#     """Simple terminal-based audio visualizer for WAV files"""
#     # Check if file exists
#     if not os.path.exists(filename):
#         print(f"Error: File '{filename}' not found")
#         return
#     
#     # Open the WAV file
#     try:
#         wf = wave.open(filename, 'rb')
#     except wave.Error:
#         print(f"Error: '{filename}' is not a valid WAV file")
#         return
#     
#     # Get file properties
#     channels = wf.getnchannels()
#     sample_width = wf.getsampwidth()
#     framerate = wf.getframerate()
#     
#     # Initialize PyAudio
#     p = pyaudio.PyAudio()
#     
#     # Open stream
#     stream = p.open(
#         format=p.get_format_from_width(sample_width),
#         channels=channels,
#         rate=framerate,
#         output=True
#     )
#     
#     # Terminal size
#     try:
#         term_width = os.get_terminal_size().columns
#         term_height = min(20, os.get_terminal_size().lines - 5)
#     except:
#         term_width = 80
#         term_height = 15
#     
#     print(f"Playing: {filename}")
#     print(f"Audio Visualizer - Press Ctrl+C to exit")
#     print()
#     
#     # Define chunk size and buffer for smoothing
#     chunk = 1024
#     viz_buffer = [[0] * term_width for _ in range(term_height)]
#     
#     # Visualization characters from low to high intensity
#     viz_chars = " .-+*#%@"
#     
#     try:
#         # Play audio with visualization
#         data = wf.readframes(chunk)
#         
#         while data:
#             # Write data to stream
#             stream.write(data)
#             
#             # Analyze audio for visualization
#             if sample_width == 2:  # 16-bit audio
#                 format_str = f"{min(chunk, len(data)//2)}h"
#                 values = list(struct.unpack(format_str, data[:len(data)//2*2]))
#                 
#                 # Simplistic visualization approach:
#                 # Divide the chunk into segments and calculate average amplitude
#                 segments = term_width
#                 samples_per_segment = max(1, len(values) // segments)
#                 
#                 amplitudes = []
#                 for i in range(segments):
#                     start = i * samples_per_segment
#                     end = min(start + samples_per_segment, len(values))
#                     if start < end:
#                         avg = sum(abs(values[j]) for j in range(start, end)) / (end - start)
#                         amplitudes.append(avg)
#                     else:
#                         amplitudes.append(0)
#                 
#                 # Normalize to visualization height
#                 max_amplitude = max(amplitudes) if amplitudes else 1
#                 normalized = [min(term_height-1, int((a / max_amplitude) * term_height)) for a in amplitudes]
#                 
#                 # Shift buffer up
#                 viz_buffer.pop(0)
#                 viz_buffer.append([0] * term_width)
#                 
#                 # Update current line in buffer
#                 for i, height in enumerate(normalized):
#                     if i < term_width:
#                         viz_buffer[-1][i] = height
#                 
#                 # Draw the visualization
#                 for y in range(term_height):
#                     line = ""
#                     row = term_height - 1 - y
#                     for x in range(term_width):
#                         value = viz_buffer[row][x]
#                         # Determine visualization character based on value
#                         char_idx = min(len(viz_chars)-1, 
#                                        int((value / term_height) * len(viz_chars)))
#                         line += viz_chars[char_idx]
#                     print(line)
#                 
#                 # Move cursor back up for next update
#                 print(f"\033[{term_height}A", end="")
#             
#             # Read next chunk
#             data = wf.readframes(chunk)
#         
#         # Clear visualization when done
#         print("\n" * term_height)
#         print("Playback complete")
#     
#     except KeyboardInterrupt:
#         print("\n" * term_height)
#         print("Playback interrupted")
#     
#     # Clean up
#     stream.stop_stream()
#     stream.close()
#     wf.close()
#     p.terminate()
#
# if __name__ == "__main__":
#     # Example usage
#     filename = input("Enter WAV file to visualize (or press Enter for test.wav): ")
#     if not filename:
#         filename = "test.wav"
#     
#     terminal_audio_visualizer(filename)


# -----------------------------------------------------
# BONUS CHALLENGE
# -----------------------------------------------------

'''
BONUS CHALLENGE: Create Your Own Advanced Audio Player

Now that you've practiced various playback techniques, create a more
advanced audio player that combines multiple features:

Ideas:
1. Media player with GUI (using a library like tkinter)
2. Audio player with equalizer/effects
3. Multi-format player (WAV, MP3, etc. using additional libraries)

Design it yourself and implement it below:
'''

# Your bonus challenge code:
# def create_my_advanced_player():
#     """
#     Create your own advanced audio player here!
#     """
#     pass  # Replace with your implementation
#
# if __name__ == "__main__":
#     create_my_advanced_player()

# =================================================
# END OF FILE
# =================================================
