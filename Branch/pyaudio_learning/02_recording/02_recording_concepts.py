# PyAudio Recording - Core Concepts
'''
This file explains the core concepts of audio recording with PyAudio.
Each section covers important information about recording techniques.

For hands-on practice with these concepts, open the companion file:
-> 02_recording_practice.py
'''

import pyaudio
import wave
import time
import os

# --------------------------------------------------
# SECTION 1: Audio Recording Fundamentals
# --------------------------------------------------

'''
AUDIO RECORDING FUNDAMENTALS:

Recording audio with PyAudio follows this general process:
1. Initialize PyAudio
2. Configure and open an input stream
3. Read audio data in chunks
4. Store the data (usually in memory or directly to a file)
5. Close the stream and clean up

Key considerations for recording:
- Sample rate: Higher = better quality but larger files
- Bit depth: Higher = more dynamic range but larger files
- Channels: Mono (1) or stereo (2) depending on your needs
- Chunk size: Affects latency and CPU usage

READING AUDIO DATA IN CHUNKS:
- A "chunk" is a fixed-size block of audio samples (e.g., 1024 samples)
- stream.read(CHUNK) captures one chunk of audio data as bytes
- Higher chunk sizes reduce CPU usage but increase latency
- Lower chunk sizes improve responsiveness but require more processing
- Typical chunk sizes: 512, 1024, 2048, or 4096 samples

STORING AUDIO DATA:
- In-memory storage: Keep chunks in a list with frames.append(data)
- Direct-to-file: Write each chunk to a WAV file as it's captured
- Combined approach: Buffer in memory, periodically write to file

CLEANING UP RESOURCES:
- Always stop and close streams when done: stream.stop_stream(), stream.close()
- Always terminate PyAudio when done: p.terminate()
- For WAV files: Call wf.close() after writing all frames
- Proper cleanup prevents resource leaks and audio device lockups

To practice recording fundamentals: See EXERCISE 1 in the practice file.
'''

# --------------------------------------------------
# SECTION 2: Recording to Memory
# --------------------------------------------------

'''
RECORDING TO MEMORY:

For short recordings or when post-processing is needed, you'll want
to record audio data to memory first before saving:

1. Create an empty list to store audio frames
2. Read chunks from the audio stream
3. Append each chunk to your list
4. When done, concatenate all chunks for processing or saving

Benefits of recording to memory:
- Can apply effects or processing before saving
- Can analyze the audio before deciding to save
- Can save in multiple formats from the same recording

To practice recording to memory: See EXERCISE 2 in the practice file.
'''

# --------------------------------------------------
# SECTION 3: Saving to WAV Files
# --------------------------------------------------

'''
SAVING TO WAV FILES:

The wave module is used to save audio data to WAV format:

1. Open a wave file in write mode ('wb')
2. Set audio parameters (channels, sample width, framerate)
3. Write audio frames to the file
4. Close the file

Essential wave file parameters:
- Channels: How many audio channels (1=mono, 2=stereo)
- Sample width: Bytes per sample (2 bytes for 16-bit audio)
- Framerate: Samples per second (e.g., 44100, 16000)

To practice saving to WAV files: See EXERCISE 3 in the practice file.
'''

# --------------------------------------------------
# SECTION 4: Recording with Input Monitoring
# --------------------------------------------------

'''
RECORDING WITH INPUT MONITORING:

Input monitoring allows you to hear what's being recorded in real-time:

1. Open both input and output streams (or one duplex stream)
2. Read audio data from the input stream
3. Immediately write that data to the output stream
4. Optionally save the data for later use

This technique is useful for:
- Audio testing and troubleshooting
- Confirming the audio quality during recording
- Applying real-time effects while recording

To practice input monitoring: See EXERCISE 4 in the practice file.
'''

# --------------------------------------------------
# SECTION 5: Voice Activity Detection
# --------------------------------------------------

'''
VOICE ACTIVITY DETECTION:

Voice Activity Detection (VAD) automatically detects when someone
is speaking versus when there is silence:

1. Calculate the audio energy/volume of each chunk
2. Compare against a threshold to determine if speech is present
3. Use state machines to track transitions (silence→speech→silence)
4. Record only during speech, or trigger actions when speech starts

Applications:
- Voice-activated recording
- Automatic silence removal
- Wake word detection for voice assistants

To practice voice activity detection: See EXERCISE 5 in the practice file.
'''

# --------------------------------------------------
# SECTION 6: Recording with Progress Feedback
# --------------------------------------------------

'''
RECORDING WITH PROGRESS FEEDBACK:

For good user experience, provide visual/audio feedback during recording:

1. Calculate expected recording duration in chunks
2. Track progress as chunks are recorded
3. Update a progress indicator (text, bar, etc.)
4. Optionally provide level meters showing audio volume

Implementation options:
- Simple text progress (dots, percentage)
- Terminal-based level meters using ASCII characters
- Integration with GUIs for visual meters

To practice recording with feedback: See EXERCISE 6 in the practice file.
'''

# --------------------------------------------------
# SECTION 7: Timed Recordings
# --------------------------------------------------

'''
TIMED RECORDINGS:

Creating recordings of specific durations is common:

1. Calculate how many chunks to read based on:
   - Desired duration (seconds)
   - Sample rate (samples/second)
   - Chunk size (samples/chunk)
2. Use a loop to read exactly that many chunks
3. Provide countdown/timing information to the user

Variations:
- Fixed duration recording (exact time)
- Maximum duration recording (up to a limit)
- Minimum duration with silence extension

To practice timed recordings: See EXERCISE 7 in the practice file.
'''

# --------------------------------------------------
# PRACTICE REMINDER
# --------------------------------------------------

print("\nREMINDER:")
print("To practice these recording concepts, open the companion file:")
print("-> 02_recording_practice.py")
print("It contains guided exercises where you write code yourself.")

# =================================================
# END OF FILE
# =================================================
