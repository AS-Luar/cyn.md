# PyAudio Basics - Core Concepts
'''
This file explains the core concepts of PyAudio and audio programming.
Each section covers important information you need to understand.

For hands-on practice with these concepts, open the companion file:
-> 01_basics_practice.py
'''

import pyaudio
import time

# --------------------------------------------------
# SECTION 1: Understanding Audio Concepts
# --------------------------------------------------

'''
CORE AUDIO CONCEPTS:

1. Sample Rate (Frequency): How many samples per second are recorded/played
   - Common rates: 44100 Hz (CD quality), 48000 Hz (professional audio)
   - Higher rates = better quality but larger files

2. Channels: Number of audio channels
   - 1 = Mono, 2 = Stereo, more for surround sound
   
3. Sample Format: How each audio sample is stored
   - Common formats: 16-bit integers, 32-bit floats
   - PyAudio uses constants like pyaudio.paInt16 for these
   
4. Frames/Chunks: Groups of samples processed together
   - A frame contains one sample for each channel
   - Chunks are groups of frames processed at once

To practice with these concepts: See EXERCISE 1 in the practice file.
'''

# Print out available PyAudio constants to understand available formats
print("AVAILABLE AUDIO FORMATS:")
print(f"16-bit int: {pyaudio.paInt16}  - Standard for most audio applications")
print(f"32-bit float: {pyaudio.paFloat32} - High precision, used in professional audio")
print(f"8-bit int: {pyaudio.paInt8}  - Low quality, small size (rarely used)")
print(f"24-bit int: {pyaudio.paInt24} - High quality audio recording/playback")
print()

# --------------------------------------------------
# SECTION 2: PyAudio Initialization and Basic Methods
# --------------------------------------------------

'''
PYAUDIO INITIALIZATION:

The PyAudio object is the main controller for audio streams.
It manages audio devices and creates input/output streams.

WHAT IS A PYAUDIO INSTANCE?

The PyAudio class is the core interface to the PortAudio system (the underlying cross-platform audio I/O library). When you create a PyAudio object:

1. It initializes the PortAudio system
2. It gives you methods to:
   - Discover audio devices on your system
   - Query device capabilities
   - Create audio streams for recording/playback
   - Convert between audio formats

Think of it like a "audio system manager" - you need exactly one per application,
and it coordinates all audio operations.

ANATOMY:
p = pyaudio.PyAudio()
│   │        │
│   │        └── Class name
│   └── Module name
└── Variable name (your reference to use this object)

LIFECYCLE:
- Create ONE PyAudio instance at the beginning of your program
- Use it to create and manage streams
- Always call terminate() when done to release system resources

To practice with PyAudio initialization: See EXERCISE 2 in the practice file.
'''

# Create a PyAudio instance
p = pyaudio.PyAudio()

# --------------------------------------------------
# SECTION 3: Device Discovery
# --------------------------------------------------

'''
DEVICE DISCOVERY AND INFORMATION:

Audio devices are identified by their index (a simple number).
Each device has properties that tell you:
- Whether it can record (input) or play audio (output)
- How many channels it supports
- What sample rates it works with

COMMON DEVICE PROPERTIES:
- 'name': The name of the device (e.g., "Built-in Microphone")
- 'maxInputChannels': How many input channels (0 = not a recording device)
- 'maxOutputChannels': How many output channels (0 = not a playback device)
- 'defaultSampleRate': The default sample rate the device prefers

Why is this important? You need to know which device to use for recording/playback,
and what capabilities it has so you can set up your audio streams correctly.

To practice with device discovery: See EXERCISE 3 in the practice file.
'''

# Check how many audio devices are available
device_count = p.get_device_count()  # Method that returns the number of audio devices
print(f"Found {device_count} audio devices on your system:")
print()

# List all audio devices - this is very useful for selecting the right device
for i in range(device_count):
    device_info = p.get_device_info_by_index(i)  # Returns a dictionary of device properties
    print(f"Device {i}:")
    print(f"  Name: {device_info['name']}")
    print(f"  Max Input Channels: {device_info['maxInputChannels']}")
    print(f"  Max Output Channels: {device_info['maxOutputChannels']}")
    print(f"  Default Sample Rate: {device_info['defaultSampleRate']}")
    print()

'''
DEFAULT DEVICES:

Operating systems designate certain audio devices as the "default" for 
input (recording) and output (playback). These are typically the devices
that the OS would use for general audio tasks.

Using these methods saves you from having to:
1. Find which devices are capable of input/output
2. Choose which one to use
3. Track their indices

If you don't specify a device when creating a stream, PyAudio will use 
these default devices automatically.
'''

# Get default input and output devices
default_input = p.get_default_input_device_info()   # Dictionary of properties for default input device
default_output = p.get_default_output_device_info() # Dictionary of properties for default output device

print(f"Default Input Device: {default_input['name']}")
print(f"Default Output Device: {default_output['name']}")
print()

# --------------------------------------------------
# SECTION 4: Audio Streams
# --------------------------------------------------

'''
WHAT IS AN AUDIO STREAM?

An audio stream is a continuous flow of audio data between your program
and an audio device (like a microphone or speakers). 

PyAudio streams enable you to:
1. Record audio from a microphone (input stream)
2. Play audio through speakers (output stream) 
3. Do both simultaneously (duplex stream)

STREAM PARAMETERS:

When opening an audio stream with PyAudio, we specify several parameters:

1. format: Sample format (bit depth and type)
2. channels: Number of audio channels (1=mono, 2=stereo)
3. rate: Sample rate in Hz (samples per second)
4. input: Boolean indicating if this is an input stream
5. output: Boolean indicating if this is an output stream
6. frames_per_buffer: How many frames to process at once
7. input_device_index/output_device_index: Which device to use

To practice creating and using streams: See EXERCISE 4 in the practice file.
'''

print("STREAM CONFIGURATIONS:")
print("CD Quality Audio: 44100 Hz, 16-bit, Stereo")
print("  - Best for music recording/playback")
print("  - Larger file sizes and more processing power")
print("  - Example: stream = p.open(format=pyaudio.paInt16, channels=2, rate=44100, ...)")
print()
print("Speech Recording: 16000 Hz, 16-bit, Mono")
print("  - Perfect for voice recognition and speech applications")
print("  - Smaller file sizes, lower bandwidth requirements")
print("  - Example: stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, ...)")
print()
print("High-Res Audio: 96000 Hz, 24-bit, Stereo")
print("  - Professional audio and music production")
print("  - Very large files, high processing requirements")
print("  - Example: stream = p.open(format=pyaudio.paInt24, channels=2, rate=96000, ...)")
print()

'''
RESOURCE MANAGEMENT:

The PyAudio instance allocates system resources for audio processing.
These resources MUST be released when you're done with them.

If you don't call terminate():
- You might prevent other applications from using audio devices
- You could cause memory leaks
- In severe cases, the system audio might become unstable

Always pair PyAudio() with terminate(), similar to opening and closing files.

To practice resource management: See EXERCISE 5 in the practice file.
'''

# --------------------------------------------------
# SECTION 5: File Operations
# --------------------------------------------------

'''
AUDIO FILE OPERATIONS:

PyAudio itself doesn't have built-in file handling, but it works 
well with Python's wave module for WAV file operations.

Key operations:
1. Saving recorded audio to a WAV file
2. Reading audio data from a WAV file for playback
3. Converting between different audio formats

Working with WAV files involves:
- Setting/reading channels, sample width, and framerate
- Writing/reading frames of audio data
- Properly opening and closing file resources

To practice with audio file operations: See EXERCISE 6 in the practice file.
'''

# --------------------------------------------------
# SECTION 6: Error Handling
# --------------------------------------------------

'''
AUDIO ERROR HANDLING:

Audio programming requires robust error handling because:
1. Audio devices might be busy or unavailable
2. Hardware limitations may prevent certain configurations
3. Resource management is critical

Best practices:
- Use try/finally blocks to ensure resources are released
- Handle exceptions when opening streams
- Provide fallback options when devices aren't available

To practice error handling: See EXERCISE 7 in the practice file.
'''

# Clean up resources
p.terminate()  # This releases all resources allocated by this PyAudio instance

# --------------------------------------------------
# PRACTICE REMINDER
# --------------------------------------------------

print("\nREMINDER:")
print("To practice these concepts, open the companion file:")
print("-> 01_basics_practice.py")
print("It contains guided exercises where you write code yourself.")

# =================================================
# END OF FILE
# =================================================
