# PyAudio Basics - Practice Exercises
'''
This file contains hands-on practice exercises for PyAudio basics.
Work through each exercise and write the code yourself to learn by doing.

First read the corresponding section in the concepts file:
-> 01_basics_concepts.py

Then complete the exercises here to practice what you've learned.
'''

# -----------------------------------------------------
# EXERCISE 1: Understanding Audio Concepts
# -----------------------------------------------------

'''
EXERCISE 1: Audio Concepts in Practice

In this exercise, you'll write code to visualize audio concepts.

STEPS:
1. Import the pyaudio module
2. Print the available audio format constants
3. Calculate how many bytes different audio formats require
4. Calculate duration based on file size and audio parameters

Write your code below and uncomment to run:
'''




# Your code for Exercise 1:
# import pyaudio
#
# print("AUDIO FORMAT CONSTANTS:")
# print(f"16-bit: {pyaudio.paInt16}")
# print(f"32-bit float: {pyaudio.paFloat32}")
# print(f"8-bit: {pyaudio.paInt8}")
# 
# # Calculate bytes per second for different formats
# def calculate_bytes_per_second(sample_rate, channels, sample_width):
#     return sample_rate * channels * sample_width
#
# # Example calculations
# cd_quality_bytes = calculate_bytes_per_second(44100, 2, 2)  # CD quality (44.1kHz, stereo, 16-bit)
# speech_bytes = calculate_bytes_per_second(16000, 1, 2)      # Speech quality (16kHz, mono, 16-bit)
#
# print(f"CD quality audio uses {cd_quality_bytes} bytes per second")
# print(f"Speech quality audio uses {speech_bytes} bytes per second")
#
# # Calculate duration of an audio file
# file_size_bytes = 1024 * 1024  # 1MB file
# cd_duration = file_size_bytes / cd_quality_bytes
# speech_duration = file_size_bytes / speech_bytes
#
# print(f"A 1MB audio file would contain {cd_duration:.2f} seconds of CD quality audio")
# print(f"A 1MB audio file would contain {speech_duration:.2f} seconds of speech quality audio")


# -----------------------------------------------------
# EXERCISE 2: PyAudio Initialization
# -----------------------------------------------------

'''
EXERCISE 2: PyAudio Initialization and Cleanup

In this exercise, you'll practice:
1. Creating a PyAudio instance
2. Getting version information
3. Properly terminating the PyAudio instance
4. Using try/finally for resource management

Write your code below and uncomment to run:
'''

# Your code for Exercise 2:
# import pyaudio
#
# # Create a PyAudio instance
import pyaudio
import time
p = pyaudio.PyAudio()
# p = pyaudio.PyAudio()
for i in range(2, 0, -1):
    print('\n\n\n\n')
    time.sleep(1)
    

#
# # Get version information
# print(f"Using PyAudio version: {pyaudio.get_portaudio_version_text()}")
# print(pyaudio.get_portaudio_version_text())

# input('You wanna die?\n')


# for i in range(5, 0, -1):
#     print(i)
#     time.sleep(1)


# p.terminate()
# print("You are dead now")
#
# # Try/finally pattern for resource management
# try:
#     # Perform audio operations here
#     print("PyAudio instance created successfully")
#     print("Performing audio operations...")
#     # We'll add real operations in later exercises
# finally:
#     # Always terminate PyAudio to release resources
#     p.terminate()
#     print("PyAudio resources released")


# -----------------------------------------------------
# EXERCISE 3: Device Discovery
# -----------------------------------------------------

'''
EXERCISE 3: Finding and Examining Audio Devices

In this exercise, you'll:
1. List all audio devices on your system
2. Find devices that support input (microphones)
3. Find devices that support output (speakers)
4. Get and print detailed information about default devices

Write your code below and uncomment to run:
'''

# Your code for Exercise 3:
# import pyaudio
#
# # Initialize PyAudio
# p = pyaudio.PyAudio()
#
# try:
#     # Get device count
#     device_count = p.get_device_count()
#     print(f"Found {device_count} audio devices")
#
#     # Lists to store different device types
#     input_devices = []
#     output_devices = []
#     
#     # Examine each device
#     for i in range(device_count):
#         device_info = p.get_device_info_by_index(i)
#         
#         # Check if it's an input device (has input channels)
#         if device_info['maxInputChannels'] > 0:
#             input_devices.append(i)
#             
#         # Check if it's an output device (has output channels)
#         if device_info['maxOutputChannels'] > 0:
#             output_devices.append(i)
#     
#     # Print results
#     print(f"\nFound {len(input_devices)} input devices (microphones):")
#     for idx in input_devices:
#         info = p.get_device_info_by_index(idx)
#         print(f"  Device {idx}: {info['name']}")
#         print(f"    Channels: {info['maxInputChannels']}")
#         print(f"    Sample Rate: {info['defaultSampleRate']}")
#         
#     print(f"\nFound {len(output_devices)} output devices (speakers):")
#     for idx in output_devices:
#         info = p.get_device_info_by_index(idx)
#         print(f"  Device {idx}: {info['name']}")
#         print(f"    Channels: {info['maxOutputChannels']}")
#         print(f"    Sample Rate: {info['defaultSampleRate']}")
#     
#     # Get default devices
#     try:
#         default_input = p.get_default_input_device_info()
#         print(f"\nDefault Input Device: {default_input['name']} (index {default_input['index']})")
#     except IOError:
#         print("\nNo default input device available")
#         
#     try:
#         default_output = p.get_default_output_device_info()
#         print(f"Default Output Device: {default_output['name']} (index {default_output['index']})")
#     except IOError:
#         print("No default output device available")
#         
# finally:
#     # Clean up
#     p.terminate()


# -----------------------------------------------------
# EXERCISE 4: Audio Streams
# -----------------------------------------------------

'''
EXERCISE 4: Creating and Using Audio Streams

In this exercise, you'll:
1. Create an audio input stream (for recording)
2. Read audio data from the stream for a certain duration
3. Properly close the stream
4. Try different stream parameters

Write your code below and uncomment to run:
'''
try:
    stream = p.open(
        format=pyaudio.paInt24,
        channels=1,
        rate=44100,
        input=True,
        frames_per_buffer=1024
    )
finally:   
        
    
    

# try:
#     # Stream parameters
#     FORMAT = pyaudio.paInt16  # 16-bit resolution
#     CHANNELS = 1              # Mono audio
#     RATE = 16000              # 16kHz sample rate
#     CHUNK = 1024              # Process 1024 frames at a time
#     RECORD_SECONDS = 5        # Record for 5 seconds
#     
#     print("Opening audio stream...")
#     
#     # Open the stream
#     stream = p.open(
#         format=FORMAT,
#         channels=CHANNELS,
#         rate=RATE,
#         input=True,           # This is an input (recording) stream
#         frames_per_buffer=CHUNK
#     )
#     
#     print("Stream is now open!")
#     print(f"Recording for {RECORD_SECONDS} seconds...")
#     
#     # Calculate how many chunks we need to read for our duration
#     chunks_to_read = int(RATE / CHUNK * RECORD_SECONDS)
#     
#     # Read audio data in chunks
#     for i in range(chunks_to_read):
#         # Read one chunk of audio data
#         data = stream.read(CHUNK)
#         
#         # Print a dot for each chunk to show progress
#         print(".", end="", flush=True)
#         
#         # Every 10 chunks, print the chunk number
#         if (i + 1) % 10 == 0:
#             print(f" {i+1}/{chunks_to_read}", end="\r", flush=True)
#     
#     print("\nFinished recording!")
#     
#     # Stop and close the stream
#     print("Stopping stream...")
#     stream.stop_stream()
#     print("Stream stopped. Closing...")
#     stream.close()
#     print("Stream closed.")
#     
#     print()
#     print("EXPERIMENT IDEAS:")
#     print("1. Try changing RATE to 44100 and listen again")
#     print("2. Try changing CHUNK to 512 or 2048")
#     print("3. Try changing RECORD_SECONDS to 3 or 10")
#     
# finally:
#     # Terminate PyAudio
#     p.terminate()
#     print("PyAudio terminated. All done!")


# -----------------------------------------------------
# EXERCISE 5: Resource Management
# -----------------------------------------------------

    '''
EXERCISE 5: Proper Resource Management

In this exercise, you'll:
1. Practice proper resource cleanup with try/except/finally
2. Handle errors that might occur during stream operations
3. Create multiple streams and ensure all are properly closed

Write your code below and uncomment to run:
'''

# Your code for Exercise 5:
# import pyaudio
# import time
#
# # Initialize PyAudio
# p = pyaudio.PyAudio()
#
# # Create empty variables to track our resources
# input_stream = None
# output_stream = None
#
# try:
#     # Stream parameters
#     FORMAT = pyaudio.paInt16
#     CHANNELS = 1
#     RATE = 16000
#     CHUNK = 1024
#     
#     print("Opening input stream...")
#     # Open an input stream
#     input_stream = p.open(
#         format=FORMAT,
#         channels=CHANNELS,
#         rate=RATE,
#         input=True,
#         frames_per_buffer=CHUNK
#     )
#     
#     print("Opening output stream...")
#     # Open an output stream
#     output_stream = p.open(
#         format=FORMAT,
#         channels=CHANNELS,
#         rate=RATE,
#         output=True,
#         frames_per_buffer=CHUNK
#     )
#     
#     print("Both streams are now open")
#     print("Performing audio operations...")
#     
#     # Simulate some operations that might raise errors
#     for i in range(5):
#         print(f"Operation {i+1}...")
#         time.sleep(0.5)
#         
#         # Simulate a potential error on the 3rd operation
#         if i == 2:
#             # Uncomment to test error handling:
#             # print("Simulating an error...")
#             # raise IOError("Simulated audio error")
#             pass
#     
#     print("Operations completed successfully")
#     
# except IOError as e:
#     print(f"Error during audio operations: {e}")
#     
# finally:
#     # Clean up ALL resources, checking if they exist first
#     print("\nCleaning up resources...")
#     
#     if input_stream is not None:
#         print("Closing input stream...")
#         input_stream.stop_stream()
#         input_stream.close()
#         
#     if output_stream is not None:
#         print("Closing output stream...")
#         output_stream.stop_stream()
#         output_stream.close()
#     
#     print("Terminating PyAudio...")
#     p.terminate()
#     
#     print("All resources have been released")


# -----------------------------------------------------
# EXERCISE 6: Audio File Operations
# -----------------------------------------------------

'''
EXERCISE 6: Working with Audio Files

In this exercise, you'll:
1. Record audio to a WAV file
2. Play back the audio from the WAV file
3. Check properties of the audio file

Write your code below and uncomment to run:
'''

# Your code for Exercise 6:
# import pyaudio
# import wave
# import time
# import os
#
# # Initialize PyAudio
# p = pyaudio.PyAudio()
#
# # Define parameters
# FORMAT = pyaudio.paInt16
# CHANNELS = 1
# RATE = 16000
# CHUNK = 1024
# RECORD_SECONDS = 3
# WAVE_OUTPUT_FILENAME = "my_recording.wav"
#
# try:
#     # PART 1: RECORDING
#     print(f"Recording {RECORD_SECONDS} seconds of audio...")
#     
#     # Open recording stream
#     stream = p.open(
#         format=FORMAT,
#         channels=CHANNELS,
#         rate=RATE,
#         input=True,
#         frames_per_buffer=CHUNK
#     )
#     
#     # Record audio in chunks and store in a list
#     frames = []
#     for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
#         data = stream.read(CHUNK, exception_on_overflow=False)
#         frames.append(data)
#         print(".", end="", flush=True)
#     
#     print("\nFinished recording")
#     
#     # Stop and close the recording stream
#     stream.stop_stream()
#     stream.close()
#     
#     # PART 2: SAVING TO FILE
#     print(f"Saving to {WAVE_OUTPUT_FILENAME}...")
#     
#     # Create WAV file
#     wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
#     
#     # Set WAV file parameters
#     wf.setnchannels(CHANNELS)
#     wf.setsampwidth(p.get_sample_size(FORMAT))
#     wf.setframerate(RATE)
#     
#     # Write audio frames to file
#     wf.writeframes(b''.join(frames))
#     
#     # Close file
#     wf.close()
#     
#     print(f"Audio saved to {WAVE_OUTPUT_FILENAME}")
#     
#     # PART 3: PLAYING BACK
#     print(f"\nPlaying back {WAVE_OUTPUT_FILENAME}...")
#     
#     # Open the WAV file for reading
#     wf = wave.open(WAVE_OUTPUT_FILENAME, 'rb')
#     
#     # Get WAV file properties
#     file_channels = wf.getnchannels()
#     file_width = wf.getsampwidth()
#     file_rate = wf.getframerate()
#     file_frames = wf.getnframes()
#     
#     # Print WAV file info
#     duration = file_frames / file_rate
#     print(f"File Info:")
#     print(f"  Channels: {file_channels}")
#     print(f"  Sample Width: {file_width} bytes")
#     print(f"  Sample Rate: {file_rate} Hz")
#     print(f"  Frames: {file_frames}")
#     print(f"  Duration: {duration:.2f} seconds")
#     
#     # Open playback stream
#     stream = p.open(
#         format=p.get_format_from_width(file_width),
#         channels=file_channels,
#         rate=file_rate,
#         output=True
#     )
#     
#     # Read and play
#     data = wf.readframes(CHUNK)
#     while data:
#         stream.write(data)
#         data = wf.readframes(CHUNK)
#     
#     # Cleanup playback
#     stream.stop_stream()
#     stream.close()
#     wf.close()
#     
#     print("Playback finished")
#     
# finally:
#     # Clean up PyAudio
#     p.terminate()
#     print("PyAudio terminated")
#     
#     # Verify file exists
#     if os.path.exists(WAVE_OUTPUT_FILENAME):
#         print(f"File saved successfully: {os.path.getsize(WAVE_OUTPUT_FILENAME)} bytes")


# -----------------------------------------------------
# EXERCISE 7: Error Handling
# -----------------------------------------------------

'''
EXERCISE 7: Robust Error Handling

In this exercise, you'll:
1. Detect and handle device errors
2. Try to open streams with invalid parameters
3. Implement fallback options
4. Practice catching and responding to audio errors

Write your code below and uncomment to run:
'''

# Your code for Exercise 7:
# import pyaudio
# import time
#
# def try_open_stream(p, **kwargs):
#     """Try to open a stream with given parameters, return None if it fails"""
#     try:
#         stream = p.open(**kwargs)
#         return stream
#     except Exception as e:
#         print(f"Failed to open stream: {e}")
#         return None
#
# # Initialize PyAudio
# p = pyaudio.PyAudio()
#
# try:
#     # First try a common configuration
#     print("Trying standard configuration...")
#     stream = try_open_stream(
#         p,
#         format=pyaudio.paInt16,
#         channels=1,
#         rate=16000,
#         input=True,
#         frames_per_buffer=1024
#     )
#     
#     # If that failed, try a fallback configuration
#     if stream is None:
#         print("Trying fallback configuration...")
#         stream = try_open_stream(
#             p,
#             format=pyaudio.paInt16,
#             channels=1,
#             rate=8000,  # Lower sample rate as fallback
#             input=True,
#             frames_per_buffer=512  # Smaller buffer
#         )
#     
#     # If that failed, try to identify available devices
#     if stream is None:
#         print("Looking for available devices...")
#         
#         # Find all input devices
#         input_devices = []
#         for i in range(p.get_device_count()):
#             dev_info = p.get_device_info_by_index(i)
#             if dev_info.get('maxInputChannels', 0) > 0:
#                 input_devices.append(i)
#                 print(f"Found input device: {i}: {dev_info['name']}")
#         
#         # If we found any, try the first one
#         if input_devices:
#             print(f"Trying first available input device ({input_devices[0]})...")
#             stream = try_open_stream(
#                 p,
#                 format=pyaudio.paInt16,
#                 channels=1,
#                 rate=16000,
#                 input=True,
#                 input_device_index=input_devices[0],
#                 frames_per_buffer=1024
#             )
#     
#     # Did we get a stream successfully?
#     if stream:
#         print("Successfully opened audio stream!")
#         print("Reading a few samples...")
#         
#         try:
#             # Try to read some data
#             for _ in range(10):
#                 data = stream.read(1024, exception_on_overflow=False)
#                 print(".", end="", flush=True)
#                 time.sleep(0.1)
#             print("\nRead operation successful")
#         except Exception as e:
#             print(f"\nError reading from stream: {e}")
#         finally:
#             # Clean up the stream
#             stream.stop_stream()
#             stream.close()
#     else:
#         print("Could not open any audio stream")
#         print("Troubleshooting steps:")
#         print("1. Check if your microphone is connected")
#         print("2. Check if it's being used by another application")
#         print("3. Check system permissions for microphone access")
#
# except Exception as e:
#     print(f"Unexpected error: {e}")
#
# finally:
#     # Always clean up
#     p.terminate()
#     print("PyAudio terminated")


# -----------------------------------------------------
# BONUS CHALLENGE
# -----------------------------------------------------

'''
BONUS CHALLENGE: Create Your Own Audio Tool

Now that you've practiced all the core concepts, try creating
a simple but complete audio tool that combines multiple techniques.

Ideas:
1. A voice recorder with silence detection
2. A simple audio effect processor (echo, volume change)
3. An audio format converter

Design it yourself and implement it below:
'''

# Your bonus challenge code:
# def create_my_audio_tool():
#     """
#     Create your own audio tool here!
#     """
#     pass  # Replace with your implementation
#
# if __name__ == "__main__":
#     create_my_audio_tool()

# =================================================
# END OF FILE
# =================================================
