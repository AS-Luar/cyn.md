# PyAudio Recording - Practice Exercises
'''
This file contains hands-on practice exercises for audio recording with PyAudio.
Work through each exercise and write the code yourself to learn by doing.

First read the corresponding section in the concepts file:
-> 02_recording_concepts.py

Then complete the exercises here to practice what you've learned.
'''

# -----------------------------------------------------
# EXERCISE 1: Basic Audio Recording
# -----------------------------------------------------

'''
EXERCISE 1: Basic Audio Recording

In this exercise, you'll create a simple audio recorder that:
1. Opens an input stream
2. Records audio for a fixed duration
3. Saves it to a WAV file

STEPS:
- Import required modules
- Set up audio parameters
- Create a PyAudio instance
- Open an input stream
- Read audio data in chunks for a specific duration
- Save the recorded data to a WAV file

DETAILED EXPLANATION OF READING CHUNKS:
1. A "chunk" is like a single frame of audio (e.g., 1024 samples)
2. stream.read(CHUNK) returns bytes containing audio data
3. Each call captures one small piece of the recording
4. We collect these chunks in a list for later processing

DETAILED EXPLANATION OF DATA STORAGE:
1. We store chunks in a list named "frames" as we record
2. Each chunk is binary audio data in the format we specified
3. To save to WAV, we join all frames with b''.join(frames)
4. This combines all chunks into a single continuous byte stream

DETAILED EXPLANATION OF CLEANUP:
1. Stop the stream with stream.stop_stream()
2. Close the stream with stream.close()
3. Terminate PyAudio with p.terminate() to free resources
4. Close the WAV file with wf.close() after saving

Write your code below:
'''


# -----------------------------------------------------
# EXERCISE 2: Recording to Memory with Post-Processing
# -----------------------------------------------------

'''
EXERCISE 2: Recording to Memory with Post-Processing

In this exercise, you'll:
1. Record audio to memory (list of frames)
2. Implement a simple volume adjustment as post-processing
3. Save the processed audio to a WAV file

STEPS:
- Record audio as in Exercise 1, but don't save immediately
- Implement a simple amplification function to adjust volume
- Process the recorded frames to adjust volume
- Save the processed audio to a WAV file

DETAILED EXPLANATION OF MEMORY RECORDING:
1. When we record to memory, we're storing audio chunks in a list (frames)
2. This gives us the entire recording as in-memory data before saving
3. Memory recording allows us to manipulate the audio before saving
4. The downside is that large recordings can consume a lot of memory

DETAILED EXPLANATION OF AUDIO PROCESSING:
1. Each chunk contains binary audio data that needs to be unpacked first
2. We use struct.unpack() to convert bytes to actual sample values
3. We modify these values (e.g., multiply by a factor to change volume)
4. We pack them back to bytes with struct.pack() to store or save

DETAILED EXPLANATION OF CLEANUP IN POST-PROCESSING:
1. Close streams and terminate PyAudio as in Exercise 1
2. After processing, close the wave file with wf.close()
3. Proper memory management: let Python garbage collect temp variables

Write your code below:
'''

# Your code for Exercise 2:
# # import pyaudio
# # import wave
# # import array
# # import struct
# # import math
# # p = pyaudio.PyAudio()
# # print('\n\n\n\n\n\n\n----------------------------------------\n')
# # #memory_recording_with_processing():
# #     # """Record audio to memory, apply processing, then save"""
#     # Audio parameters
    
# try:    
#     FORMAT = pyaudio.paInt16
#     CHANNELS = 1
#     RATE = 44000
#     CHUNK = 1024
#     RECORD_SECONDS = 5
#     WAVE_OUTPUT_FILENAME = "exercise2_processed.wav"
#     VOLUME_FACTOR = 2.0  # Double the volume


#     # Open input stream
#     stream = p.open(
#         format=FORMAT,
#         channels=CHANNELS,
#         rate=RATE,
#         input=True,
#         frames_per_buffer=CHUNK
#     )

#     print(f"Recording for {RECORD_SECONDS} seconds...")

#     # Record audio in chunks
#     frames = []
#     for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
#         data = stream.read(CHUNK)
#         frames.append(data)
        
#         # Show recording progress
#         if i % 10 == 0:
#             print(".", end="", flush=True)

#     print("\nRecording complete!")
# finally:
#     # Stop and close the stream
#     stream.stop_stream()
#     stream.close()
#     p.terminate()

#     # print("Processing audio (adjusting volume)...")

#     # Process the audio (adjust volume)
#     processed_frames = []

#     for frame in frames:
#         # Convert bytes to samples
#         # Assuming FORMAT is paInt16, which is 2 bytes per sample
#         samples = struct.unpack(f"{CHUNK}h", frame)
        
    #     # Apply volume adjustment
    #     adjusted = []
    #     for sample in samples:
    #         # Apply volume factor and clip if necessary
    #         new_sample = int(sample * VOLUME_FACTOR)
    #         # Ensure we don't exceed the range for 16-bit audio
    #         new_sample = max(min(new_sample, 32767), -32768)
    #         adjusted.append(new_sample)
        
    #     # Pack back to bytes
    #     processed_frame = struct.pack(f"{CHUNK}h", *adjusted)
    #     processed_frames.append(processed_frame)

    # # Save the processed audio to WAV file
    # wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    # wf.setnchannels(CHANNELS)
    # wf.setsampwidth(p.get_sample_size(FORMAT))
    # wf.setframerate(RATE)
    # wf.writeframes(b''.join(processed_frames))
    # wf.close()

    # print(f"Processed audio saved to {WAVE_OUTPUT_FILENAME}")
    # print(f"Volume increased by factor of {VOLUME_FACTOR}")
    #




# -----------------------------------------------------
# EXERCISE 3: Recording Directly to WAV File
# -----------------------------------------------------

'''
EXERCISE 3: Recording Directly to WAV File

In this exercise, you'll:
1. Set up a WAV file before recording starts
2. Write audio chunks directly to the file during recording
3. Properly finalize the file when done

STEPS:
- Set up audio parameters
- Create and initialize a WAV file with the correct parameters
- Record audio and write chunks directly to the file
- Finalize the file when recording is complete

Write your code below and uncomment to run:
'''

# Your code for Exercise 3:

# -----------------------------------------------------
# EXERCISE 4: Recording with Input Monitoring
# -----------------------------------------------------

'''
EXERCISE 4: Recording with Input Monitoring

In this exercise, you'll:
1. Set up a duplex stream (both input and output)
2. Pass audio from input to output for real-time monitoring
3. Save the audio at the same time

STEPS:
- Set up a duplex stream with both input and output
- Read audio data from the input
- Write the same data to the output for real-time monitoring
- Save the data to a file

Write your code below and uncomment to run:
'''

# Your code for Exercise 4:
# import pyaudio
# import wave
# import time
#
# def record_with_monitoring():
#     """Record audio while monitoring the input in real-time"""
#     # Audio parameters
#     FORMAT = pyaudio.paInt16
#     CHANNELS = 1
#     RATE = 16000
#     CHUNK = 1024
#     RECORD_SECONDS = 10
#     WAVE_OUTPUT_FILENAME = "exercise4_monitored.wav"
#     
#     # Initialize PyAudio
#     p = pyaudio.PyAudio()
#     
#     # Open a duplex stream
#     stream = p.open(
#         format=FORMAT,
#         channels=CHANNELS,
#         rate=RATE,
#         input=True,
#         output=True,  # Enable output for monitoring
#         frames_per_buffer=CHUNK
#     )
#     
#     print(f"Recording with monitoring for {RECORD_SECONDS} seconds...")
#     print("You should hear your microphone input through your speakers")
#     print("Speak into your microphone to test...")
#     
#     # Record audio while monitoring
#     frames = []
#     for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
#         # Read from input
#         data = stream.read(CHUNK)
#         
#         # Play through output (monitor)
#         stream.write(data)
#         
#         # Save for recording
#         frames.append(data)
#         
#         # Show recording progress
#         elapsed = i * CHUNK / RATE
#         remaining = RECORD_SECONDS - elapsed
#         print(f"Recording: {elapsed:.1f}s / {RECORD_SECONDS}s", end="\r", flush=True)
#     
#     print("\nRecording complete!")
#     
#     # Clean up
#     stream.stop_stream()
#     stream.close()
#     p.terminate()
#     
#     # Save the recorded audio to WAV file
#     wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
#     wf.setnchannels(CHANNELS)
#     wf.setsampwidth(p.get_sample_size(FORMAT))
#     wf.setframerate(RATE)
#     wf.writeframes(b''.join(frames))
#     wf.close()
#     
#     print(f"Audio saved to {WAVE_OUTPUT_FILENAME}")
#
# if __name__ == "__main__":
#     record_with_monitoring()


# -----------------------------------------------------
# EXERCISE 5: Voice Activity Detection
# -----------------------------------------------------

'''
EXERCISE 5: Voice Activity Detection

In this exercise, you'll:
1. Create a voice-activated recorder
2. Detect when someone starts speaking
3. Record until silence is detected again
4. Save the audio containing only the speaking portions

STEPS:
- Monitor audio levels continuously
- When the level exceeds a threshold, start recording
- Keep recording until the level stays below the threshold for a set time
- Save only the speaking portions

Write your code below and uncomment to run:
'''

# Your code for Exercise 5:
# import pyaudio
# import wave
# import struct
# import math
# import time
# import datetime
#
# def voice_activated_recorder():
#     """Record audio when voice activity is detected"""
#     # Audio parameters
#     FORMAT = pyaudio.paInt16
#     CHANNELS = 1
#     RATE = 16000
#     CHUNK = 1024
#     
#     # Voice detection parameters
#     THRESHOLD = 1500  # Adjust this based on your microphone/environment
#     SILENCE_LIMIT = 2  # Seconds of silence before stopping
#     PREV_AUDIO = 0.5   # Seconds of audio to save before trigger
#     
#     # Initialize PyAudio
#     p = pyaudio.PyAudio()
#     
#     # Open input stream
#     stream = p.open(
#         format=FORMAT,
#         channels=CHANNELS,
#         rate=RATE,
#         input=True,
#         frames_per_buffer=CHUNK
#     )
#     
#     print("Voice-activated recording started")
#     print("Speak to begin recording... (Press Ctrl+C to exit)")
#     print(f"Threshold: {THRESHOLD}, Silence Limit: {SILENCE_LIMIT}s")
#     
#     # Variables for detection
#     frames = []
#     recording = False
#     silent_chunks = 0
#     audio_started = False
#     silent_threshold = int(SILENCE_LIMIT * RATE / CHUNK)
#     prev_audio_chunks = int(PREV_AUDIO * RATE / CHUNK)
#     prev_audio_buffer = []
#     
#     try:
#         while True:
#             # Read current chunk
#             data = stream.read(CHUNK, exception_on_overflow=False)
#             
#             # Calculate audio energy
#             values = struct.unpack(f"{CHUNK}h", data)
#             energy = sum(abs(value) for value in values) / len(values)
#             
#             # Show audio level
#             level_bar = "#" * int(energy / 500)
#             print(f"Level: {energy:.0f} {level_bar}", end="\r", flush=True)
#             
#             # If not recording, add to prev_audio buffer
#             if not recording:
#                 prev_audio_buffer.append(data)
#                 # Keep buffer at correct size
#                 if len(prev_audio_buffer) > prev_audio_chunks:
#                     prev_audio_buffer.pop(0)
#                 
#                 # Check if audio energy is above threshold
#                 if energy > THRESHOLD:
#                     print("\nVoice detected! Recording...")
#                     recording = True
#                     audio_started = True
#                     
#                     # Add previous audio to the recording
#                     frames.extend(prev_audio_buffer)
#                     
#                     # Add current chunk
#                     frames.append(data)
#                     silent_chunks = 0
#             else:
#                 # Already recording
#                 frames.append(data)
#                 
#                 # Check for silence
#                 if energy < THRESHOLD:
#                     silent_chunks += 1
#                     print(f"Silence detected: {silent_chunks}/{silent_threshold}", end="\r", flush=True)
#                     
#                     # If enough silent chunks, stop recording
#                     if silent_chunks >= silent_threshold:
#                         print("\nSilence threshold reached. Stopping recording.")
#                         break
#                 else:
#                     # Reset silent counter if we hear something
#                     silent_chunks = 0
#             
#             # Prevent the loop from consuming 100% CPU
#             time.sleep(0.01)
#     
#     except KeyboardInterrupt:
#         print("\nRecording stopped by user")
#     
#     # Check if we recorded anything
#     if audio_started:
#         timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
#         filename = f"voice_activated_{timestamp}.wav"
#         
#         # Save the recorded audio to WAV file
#         wf = wave.open(filename, 'wb')
#         wf.setnchannels(CHANNELS)
#         wf.setsampwidth(p.get_sample_size(FORMAT))
#         wf.setframerate(RATE)
#         wf.writeframes(b''.join(frames))
#         wf.close()
#         
#         duration = len(frames) * CHUNK / RATE
#         print(f"Audio saved to {filename}")
#         print(f"Recording duration: {duration:.2f} seconds")
#     else:
#         print("No audio was recorded")
#     
#     # Clean up
#     stream.stop_stream()
#     stream.close()
#     p.terminate()
#
# if __name__ == "__main__":
#     voice_activated_recorder()


# -----------------------------------------------------
# EXERCISE 6: Recording with Visual Level Meter
# -----------------------------------------------------

'''
EXERCISE 6: Recording with Visual Level Meter

In this exercise, you'll:
1. Create a recorder with a real-time visual audio level display
2. Show both current level and peak level
3. Display recording progress

STEPS:
- Set up audio parameters and stream
- Calculate and display audio levels in real-time
- Track and show peak levels
- Show recording progress and time remaining

Write your code below and uncomment to run:
'''

# Your code for Exercise 6:
# import pyaudio
# import wave
# import struct
# import math
# import time
# import os
#
# def record_with_level_meter():
#     """Record audio while displaying a real-time level meter"""
#     # Audio parameters
#     FORMAT = pyaudio.paInt16
#     CHANNELS = 1
#     RATE = 16000
#     CHUNK = 1024
#     RECORD_SECONDS = 10
#     WAVE_OUTPUT_FILENAME = "exercise6_level_meter.wav"
#     
#     # Terminal width for meter display
#     try:
#         TERM_WIDTH = os.get_terminal_size().columns - 20
#     except:
#         TERM_WIDTH = 50  # Default if can't get terminal size
#     
#     # Initialize PyAudio
#     p = pyaudio.PyAudio()
#     
#     # Open input stream
#     stream = p.open(
#         format=FORMAT,
#         channels=CHANNELS,
#         rate=RATE,
#         input=True,
#         frames_per_buffer=CHUNK
#     )
#     
#     print(f"Recording for {RECORD_SECONDS} seconds with level meter...")
#     print("Speak into your microphone to see the levels change")
#     print(" " * TERM_WIDTH + "PEAK")
#     print("0" + "-" * (TERM_WIDTH-2) + "100%")
#     
#     # Variables for recording
#     frames = []
#     peak_energy = 0
#     
#     # Calculate total chunks for the recording
#     total_chunks = int(RATE / CHUNK * RECORD_SECONDS)
#     
#     for i in range(total_chunks):
#         # Calculate time information
#         elapsed = i * CHUNK / RATE
#         remaining = RECORD_SECONDS - elapsed
#         progress_pct = (i / total_chunks) * 100
#         
#         # Read audio chunk
#         data = stream.read(CHUNK, exception_on_overflow=False)
#         frames.append(data)
#         
#         # Calculate audio level
#         values = struct.unpack(f"{CHUNK}h", data)
#         energy = sum(abs(value) for value in values) / len(values)
#         
#         # Update peak if needed
#         if energy > peak_energy:
#             peak_energy = energy
#         
#         # Calculate level as percentage of max possible (normalize)
#         # Assuming 16-bit audio, max is 32767
#         level_pct = min(100, energy / 327.67)  # 1% of max possible
#         peak_pct = min(100, peak_energy / 327.67)
#         
#         # Create the level meter display
#         meter_len = int((TERM_WIDTH * level_pct) / 100)
#         peak_pos = int((TERM_WIDTH * peak_pct) / 100)
#         
#         meter = "█" * meter_len
#         if peak_pos > meter_len:
#             meter += " " * (peak_pos - meter_len) + "▲"
#         
#         # Print progress and meter
#         print(f"[{progress_pct:3.0f}%] {elapsed:.1f}s/{RECORD_SECONDS:.1f}s | {meter:<{TERM_WIDTH}} | {level_pct:.1f}%", end="\r", flush=True)
#     
#     print("\nRecording complete!")
#     
#     # Clean up
#     stream.stop_stream()
#     stream.close()
#     p.terminate()
#     
#     # Save the recorded audio to WAV file
#     wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
#     wf.setnchannels(CHANNELS)
#     wf.setsampwidth(p.get_sample_size(FORMAT))
#     wf.setframerate(RATE)
#     wf.writeframes(b''.join(frames))
#     wf.close()
#     
#     print(f"Audio saved to {WAVE_OUTPUT_FILENAME}")
#
# if __name__ == "__main__":
#     record_with_level_meter()


# -----------------------------------------------------
# EXERCISE 7: Timed Multi-Part Recording
# -----------------------------------------------------

'''
EXERCISE 7: Timed Multi-Part Recording

In this exercise, you'll:
1. Create a recorder that breaks recordings into timed segments
2. Allow the user to pause and resume recording
3. Combine the segments into a single file at the end

STEPS:
- Set up audio parameters and stream
- Record in timed segments
- Allow for user interaction to pause/resume
- Combine all segments at the end

Write your code below and uncomment to run:
'''

# Your code for Exercise 7:
# import pyaudio
# import wave
# import time
# import threading
# import os
#
# def timed_multi_part_recorder():
#     """Record audio in segments with pause/resume capability"""
#     # Audio parameters
#     FORMAT = pyaudio.paInt16
#     CHANNELS = 1
#     RATE = 16000
#     CHUNK = 1024
#     SEGMENT_SECONDS = 5  # Length of each segment
#     MAX_SEGMENTS = 10    # Maximum number of segments
#     WAVE_OUTPUT_FILENAME = "exercise7_combined.wav"
#     
#     # Initialize PyAudio
#     p = pyaudio.PyAudio()
#     
#     # Variable to control recording state
#     recording = True
#     paused = False
#     segments = []
#     segment_count = 0
#     
#     def input_thread():
#         """Thread to handle user input during recording"""
#         nonlocal recording, paused
#         print("\nCommands:")
#         print("  p - Pause/resume recording")
#         print("  q - Stop recording and save")
#         
#         while recording:
#             key = input().lower()
#             if key == 'p':
#                 paused = not paused
#                 print("Recording PAUSED" if paused else "Recording RESUMED")
#             elif key == 'q':
#                 recording = False
#                 print("Stopping recording...")
#             # Short sleep to prevent high CPU usage
#             time.sleep(0.1)
#     
#     # Start the input thread
#     input_thread = threading.Thread(target=input_thread)
#     input_thread.daemon = True
#     input_thread.start()
#     
#     print(f"Starting multi-part recording (max {MAX_SEGMENTS} segments of {SEGMENT_SECONDS}s each)")
#     print("Recording will automatically break into segments")
#     
#     # Main recording loop
#     while recording and segment_count < MAX_SEGMENTS:
#         if not paused:
#             # Start a new segment
#             segment_count += 1
#             print(f"\nRecording segment {segment_count}...")
#             
#             # Open input stream
#             stream = p.open(
#                 format=FORMAT,
#                 channels=CHANNELS,
#                 rate=RATE,
#                 input=True,
#                 frames_per_buffer=CHUNK
#             )
#             
#             # Record this segment
#             segment_frames = []
#             for i in range(0, int(RATE / CHUNK * SEGMENT_SECONDS)):
#                 if not recording or paused:
#                     break
#                     
#                 data = stream.read(CHUNK, exception_on_overflow=False)
#                 segment_frames.append(data)
#                 
#                 # Show recording progress
#                 elapsed = i * CHUNK / RATE
#                 remaining = SEGMENT_SECONDS - elapsed
#                 print(f"Segment {segment_count}: {elapsed:.1f}s/{SEGMENT_SECONDS:.1f}s", end="\r", flush=True)
#             
#             # Close this segment's stream
#             stream.stop_stream()
#             stream.close()
#             
#             # Add to segments list if we recorded anything
#             if segment_frames:
#                 segments.append(segment_frames)
#                 print(f"\nSegment {segment_count} complete ({len(segment_frames) * CHUNK / RATE:.1f}s)")
#         else:
#             # If paused, wait briefly then check again
#             print("Recording paused. Press 'p' to resume.", end="\r", flush=True)
#             time.sleep(0.5)
#     
#     # Recording complete
#     print("\nRecording complete!")
#     print(f"Recorded {len(segments)} segments")
#     
#     # Terminate PyAudio
#     p.terminate()
#     
#     # Combine all segments into one file
#     if segments:
#         print(f"Combining segments into {WAVE_OUTPUT_FILENAME}...")
#         
#         # Open the output file
#         wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
#         wf.setnchannels(CHANNELS)
#         wf.setsampwidth(p.get_sample_size(FORMAT))
#         wf.setframerate(RATE)
#         
#         # Write all segments
#         total_frames = 0
#         for i, segment in enumerate(segments):
#             segment_data = b''.join(segment)
#             wf.writeframes(segment_data)
#             total_frames += len(segment)
#             print(f"Added segment {i+1}/{len(segments)}")
#         
#         wf.close()
#         
#         total_duration = total_frames * CHUNK / RATE
#         print(f"Audio saved to {WAVE_OUTPUT_FILENAME}")
#         print(f"Total duration: {total_duration:.2f} seconds")
#     else:
#         print("No audio was recorded")
#
# if __name__ == "__main__":
#     timed_multi_part_recorder()


# -----------------------------------------------------
# BONUS CHALLENGE
# -----------------------------------------------------

'''
BONUS CHALLENGE: Create Your Own Advanced Recorder

Now that you've practiced various recording techniques, create a more
advanced recorder that combines multiple features:

Ideas:
1. Voice-activated recorder with visualization
2. Audio notebook with labeled segments
3. Scheduled recorder that starts/stops at specific times

Design it yourself and implement it below:
'''

# Your bonus challenge code:
# def create_my_advanced_recorder():
#     """
#     Create your own advanced recorder here!
#     """
#     pass  # Replace with your implementation
#
# if __name__ == "__main__":
#     create_my_advanced_recorder()

# =================================================
# END OF FILE
# =================================================
