# Audio Processing with PyAudio - Practice
'''
This file provides hands-on practice exercises for audio processing with PyAudio.
Complete each exercise to gain practical experience with audio data manipulation.

Before starting, review the concepts in 04_audio_processing_concepts.py
'''

import pyaudio
import wave
import os
import struct
import time
import math

# --------------------------------------------------
# Exercise 1: Exploring Audio Data
# --------------------------------------------------

def exercise_1():
    '''
    EXERCISE 1: Audio Data Explorer
    
    In this exercise, you'll create a function that explores and 
    displays the properties of a WAV file and shows its raw data.
    
    Your task:
    1. Complete the explore_audio_data function below
    2. Display file properties (channels, sample width, etc.)
    3. Read and display raw samples to understand the data format
    4. Calculate and display some basic statistics about the audio
    '''
    print("\nEXERCISE 1: Audio Data Explorer")
    print("==============================")
    print("This exercise will help you understand how audio data is structured.")
    
    def explore_audio_data(filename):
        '''
        Opens a WAV file and explores its raw data content.
        '''
        # Verify file exists
        if not os.path.exists(filename):
            print(f"Error: File {filename} does not exist")
            return
        
        try:
            # TODO: Open the WAV file and extract its properties
            # Hint: Use wave.open() and methods like getnchannels(), getsampwidth(), etc.
            
            # TODO: Display file properties like:
            # - Number of channels
            # - Sample width in bits
            # - Sample rate (framerate)
            # - Number of frames
            # - Duration in seconds
            
            # TODO: Read a small sample of frames (e.g., 10 frames)
            # and display their raw values
            
            # TODO: Calculate and display statistics like:
            # - Maximum sample value
            # - Minimum sample value
            # - Average amplitude
            
            pass  # Remove this line when you add your code
            
            '''
            # SOLUTION (uncomment to see it work)
            # Open the WAV file
            wf = wave.open(filename, 'rb')
            
            # Get file properties
            channels = wf.getnchannels()
            sample_width = wf.getsampwidth()
            framerate = wf.getframerate()
            n_frames = wf.getnframes()
            
            print(f"\nAudio File: {filename}")
            print(f"Channels: {channels}")
            print(f"Sample Width: {sample_width * 8} bits")
            print(f"Sample Rate: {framerate} Hz")
            print(f"Number of Frames: {n_frames}")
            print(f"Duration: {n_frames / framerate:.2f} seconds")
            
            # Read a small sample of frames for analysis
            sample_frames = 10
            wf.setpos(0)  # Go to beginning of file
            sample_data = wf.readframes(sample_frames)
            
            print(f"\nRaw bytes of first {sample_frames} frames:")
            print(sample_data[:30])  # Print first 30 bytes
            
            print("\nDecoded sample values:")
            
            # The format string depends on the sample width
            if sample_width == 1:
                # 8-bit is unsigned
                fmt = f"{sample_frames * channels}B"
            elif sample_width == 2:
                # 16-bit is signed little-endian
                fmt = f"{sample_frames * channels}h"
            elif sample_width == 4:
                # 32-bit is signed little-endian
                fmt = f"{sample_frames * channels}i"
            else:
                print(f"Unsupported sample width: {sample_width}")
                return
            
            # Decode the binary data to numbers
            values = struct.unpack(fmt, sample_data[:struct.calcsize(fmt)])
            
            # Display the values
            for i, value in enumerate(values):
                channel = i % channels + 1
                frame = i // channels + 1
                print(f"Frame {frame}, Channel {channel}: {value}")
            
            # Get statistics from the whole file
            wf.setpos(0)
            all_data = wf.readframes(min(n_frames, 1000))  # Read up to 1000 frames
            
            if sample_width == 1:
                fmt = f"{min(n_frames, 1000) * channels}B"
            elif sample_width == 2:
                fmt = f"{min(n_frames, 1000) * channels}h"
            elif sample_width == 4:
                fmt = f"{min(n_frames, 1000) * channels}i"
            
            all_values = struct.unpack(fmt, all_data[:struct.calcsize(fmt)])
            
            print("\nAudio Statistics (from first 1000 frames):")
            print(f"Max value: {max(all_values)}")
            print(f"Min value: {min(all_values)}")
            print(f"Average absolute amplitude: {sum(abs(v) for v in all_values) / len(all_values):.1f}")
            
            wf.close()
            '''
        
        except Exception as e:
            print(f"Error exploring audio data: {e}")
    
    # Find WAV files in current directory
    wav_files = [f for f in os.listdir('.') if f.endswith('.wav')]
    
    if not wav_files:
        print("No WAV files found in current directory.")
        print("You need a WAV file to complete this exercise.")
        print("You can create one using the recording functions from previous modules.")
        return
    
    print("\nAvailable WAV files:")
    for i, file in enumerate(wav_files):
        print(f"{i+1}. {file}")
    
    choice = input("\nEnter file number or full path to WAV file: ")
    
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(wav_files):
            filename = wav_files[idx]
        else:
            print("Invalid file number")
            return
    except ValueError:
        filename = choice
    
    explore_audio_data(filename)


# --------------------------------------------------
# Exercise 2: Audio Transformations
# --------------------------------------------------

def exercise_2():
    '''
    EXERCISE 2: Audio Transformations
    
    In this exercise, you'll implement functions to transform audio in various ways.
    
    Your task:
    1. Implement volume adjustment function
    2. Implement a basic speed change function
    3. Implement stereo to mono conversion
    '''
    print("\nEXERCISE 2: Audio Transformations")
    print("===============================")
    print("This exercise will help you learn to modify audio data.")
    
    # Find WAV files in current directory
    wav_files = [f for f in os.listdir('.') if f.endswith('.wav')]
    
    if not wav_files:
        print("No WAV files found in current directory.")
        print("You need a WAV file to complete this exercise.")
        return
    
    print("\nAvailable WAV files:")
    for i, file in enumerate(wav_files):
        print(f"{i+1}. {file}")
    
    choice = input("\nEnter file number to transform: ")
    
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(wav_files):
            input_file = wav_files[idx]
        else:
            print("Invalid file number")
            return
    except ValueError:
        print("Invalid input")
        return
    
    # Choose transformation
    print("\nTransformation Options:")
    print("1. Adjust Volume")
    print("2. Change Speed")
    print("3. Convert Stereo to Mono")
    
    option = input("Enter transformation option (1-3): ")
    
    # Get output filename
    output_file = input("Enter output WAV file name: ")
    
    if option == "1":
        try:
            factor = float(input("Enter volume factor (0.1 to 5.0, 1.0 is original): "))
            if factor < 0.1 or factor > 5.0:
                print("Volume factor must be between 0.1 and 5.0")
                return
            
            adjust_volume(input_file, output_file, factor)
        except ValueError:
            print("Invalid volume factor")
    
    elif option == "2":
        try:
            factor = float(input("Enter speed factor (0.5 to 2.0, 1.0 is original): "))
            if factor < 0.5 or factor > 2.0:
                print("Speed factor must be between 0.5 and 2.0")
                return
            
            change_speed(input_file, output_file, factor)
        except ValueError:
            print("Invalid speed factor")
    
    elif option == "3":
        stereo_to_mono(input_file, output_file)
    
    else:
        print("Invalid option")


def adjust_volume(input_file, output_file, volume_factor):
    '''
    TODO: Implement a function that adjusts the volume of a WAV file
    
    Steps:
    1. Open the input WAV file
    2. Create an output WAV file with the same properties
    3. Read chunks of audio data
    4. Multiply each sample by the volume factor
    5. Make sure to handle clipping (values out of range)
    6. Write the modified chunks to the output file
    '''
    print(f"Adjusting volume of {input_file} by factor {volume_factor}...")
    # Your code here
    
    '''
    # SOLUTION (uncomment to see it work)
    try:
        # Open the input WAV file
        with wave.open(input_file, 'rb') as wf:
            # Get file properties
            channels = wf.getnchannels()
            sample_width = wf.getsampwidth()
            framerate = wf.getframerate()
            n_frames = wf.getnframes()
            
            # Create output WAV file with same properties
            with wave.open(output_file, 'wb') as out_wf:
                out_wf.setnchannels(channels)
                out_wf.setsampwidth(sample_width)
                out_wf.setframerate(framerate)
                
                # Process in chunks
                CHUNK = 1024
                for _ in range(0, n_frames, CHUNK):
                    # Read a chunk of frames
                    data = wf.readframes(CHUNK)
                    if not data:
                        break
                    
                    # Convert to samples we can modify
                    if sample_width == 1:
                        # 8-bit samples (unsigned)
                        fmt = f"{len(data)}B"
                        samples = list(struct.unpack(fmt, data))
                        
                        # Adjust volume (being careful not to exceed the range)
                        for j in range(len(samples)):
                            # Convert 0-255 to -128-127 range first
                            value = samples[j] - 128
                            value = int(value * volume_factor)
                            # Clamp to -128,127 range and convert back to 0-255
                            value = max(min(value, 127), -128) + 128
                            samples[j] = value
                        
                        # Convert back to bytes
                        data = struct.pack(fmt, *samples)
                        
                    elif sample_width == 2:
                        # 16-bit samples (signed)
                        fmt = f"{len(data)//2}h"
                        samples = list(struct.unpack(fmt, data))
                        
                        # Adjust volume
                        for j in range(len(samples)):
                            value = int(samples[j] * volume_factor)
                            # Clamp to 16-bit range
                            value = max(min(value, 32767), -32768)
                            samples[j] = value
                        
                        # Convert back to bytes
                        data = struct.pack(fmt, *samples)
                    
                    # Write the modified chunk
                    out_wf.writeframes(data)
            
            print(f"Volume adjustment complete. Output saved to {output_file}")
    
    except Exception as e:
        print(f"Error adjusting volume: {e}")
    '''


def change_speed(input_file, output_file, speed_factor):
    '''
    TODO: Implement a function that changes the speed of a WAV file
    
    Note: This simple approach changes both speed AND pitch together.
    
    Steps:
    1. Open the input WAV file
    2. Create an output WAV file with modified sample rate
    3. Copy all frames directly to the output
    '''
    print(f"Changing speed of {input_file} by factor {speed_factor}...")
    # Your code here
    
    '''
    # SOLUTION (uncomment to see it work)
    try:
        # Open the input WAV file
        with wave.open(input_file, 'rb') as wf:
            # Get file properties
            channels = wf.getnchannels()
            sample_width = wf.getsampwidth()
            framerate = wf.getframerate()
            n_frames = wf.getnframes()
            
            # Create output WAV file with modified framerate
            with wave.open(output_file, 'wb') as out_wf:
                out_wf.setnchannels(channels)
                out_wf.setsampwidth(sample_width)
                out_wf.setframerate(int(framerate * speed_factor))
                
                # Copy all frames directly (the new sample rate will change playback speed)
                data = wf.readframes(n_frames)
                out_wf.writeframes(data)
            
            print(f"Speed change complete. Output saved to {output_file}")
            print("Note: This simple approach changes both speed AND pitch.")
    
    except Exception as e:
        print(f"Error changing speed: {e}")
    '''


def stereo_to_mono(input_file, output_file):
    '''
    TODO: Implement a function that converts a stereo WAV file to mono
    
    Steps:
    1. Open the input WAV file
    2. Check if it's actually stereo (2 channels)
    3. Create a mono output WAV file
    4. For each pair of samples (left, right), average them to create one mono sample
    5. Write the mono samples to the output file
    '''
    print(f"Converting {input_file} from stereo to mono...")
    # Your code here
    
    '''
    # SOLUTION (uncomment to see it work)
    try:
        # Open the input WAV file
        with wave.open(input_file, 'rb') as wf:
            # Get file properties
            channels = wf.getnchannels()
            sample_width = wf.getsampwidth()
            framerate = wf.getframerate()
            n_frames = wf.getnframes()
            
            if channels == 1:
                print("File is already mono!")
                return
            
            # Create output WAV file
            with wave.open(output_file, 'wb') as out_wf:
                out_wf.setnchannels(1)  # Mono
                out_wf.setsampwidth(sample_width)
                out_wf.setframerate(framerate)
                
                # Process in chunks
                CHUNK = 1024
                for _ in range(0, n_frames, CHUNK):
                    # Read a chunk of frames
                    data = wf.readframes(CHUNK)
                    if not data:
                        break
                    
                    # Convert to samples
                    if sample_width == 1:
                        # 8-bit samples (unsigned)
                        fmt = f"{len(data)}B"
                        samples = list(struct.unpack(fmt, data))
                        
                        # Process stereo to mono (average channels)
                        mono_samples = []
                        for j in range(0, len(samples), channels):
                            if j + channels <= len(samples):
                                avg = sum(samples[j:j+channels]) // channels
                                mono_samples.append(avg)
                        
                        # Convert back to bytes
                        mono_data = struct.pack(f"{len(mono_samples)}B", *mono_samples)
                        
                    elif sample_width == 2:
                        # 16-bit samples (signed)
                        fmt = f"{len(data)//2}h"
                        samples = list(struct.unpack(fmt, data))
                        
                        # Process stereo to mono (average channels)
                        mono_samples = []
                        for j in range(0, len(samples), channels):
                            if j + channels <= len(samples):
                                avg = sum(samples[j:j+channels]) // channels
                                mono_samples.append(avg)
                        
                        # Convert back to bytes
                        mono_data = struct.pack(f"{len(mono_samples)}h", *mono_samples)
                    
                    # Write the mono data
                    out_wf.writeframes(mono_data)
            
            print(f"Stereo to mono conversion complete. Output saved to {output_file}")
    
    except Exception as e:
        print(f"Error converting stereo to mono: {e}")
    '''


# --------------------------------------------------
# Exercise 3: Voice Activity Detection
# --------------------------------------------------

def exercise_3():
    '''
    EXERCISE 3: Voice Activity Detection
    
    In this exercise, you'll implement a simple voice activity detector
    that listens to the microphone and detects when someone is speaking.
    
    Your task:
    1. Implement the voice detection algorithm 
    2. Add visual feedback to show voice/silence detection
    3. Extend with features like recording only when voice is detected
    '''
    print("\nEXERCISE 3: Voice Activity Detection")
    print("=================================")
    print("This exercise will help you implement a voice detection system.")
    print("Speak into your microphone to see the detection in action.")
    print("Press Ctrl+C to stop the program when you're done.")
    
    # TODO: Implement a voice detector function
    def simple_voice_detector():
        '''
        Implement a function that detects voice activity from the microphone.
        The detector should:
        1. Calculate energy/amplitude of the audio
        2. Compare it to a threshold to detect voice
        3. Show a visual indicator when voice is detected
        4. Handle transitions from silence to speech and vice versa
        '''
        # Audio parameters
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 16000
        CHUNK = 512
        
        # TODO: Set a threshold for voice detection
        # You may need to adjust this based on your microphone
        THRESHOLD = 1000  # Starting value, adjust as needed
        
        # TODO: Initialize PyAudio and open an input stream
        
        # TODO: Implement the voice detection loop
        # - Read audio data
        # - Calculate energy/amplitude
        # - Compare to threshold
        # - Update voice state
        # - Provide visual feedback
        
        print("Voice detection not yet implemented!")
        
        # TODO: Clean up when done (close stream, terminate PyAudio)
        
        '''
        # SOLUTION (uncomment to see it work)
        # Initialize PyAudio
        p = pyaudio.PyAudio()
        
        try:
            # Open stream for recording
            stream = p.open(
                format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK
            )
            
            print("Listening... Speak to see voice detection in action.")
            print("(Press Ctrl+C to stop)\n")
            
            # Track voice state
            voice_active = False
            silence_counter = 0
            
            # Listen continuously
            while True:
                # Read audio data
                data = stream.read(CHUNK, exception_on_overflow=False)
                
                # Convert audio data to samples
                samples = struct.unpack(f"{CHUNK}h", data)
                
                # Calculate energy (sum of absolute values)
                energy = sum(abs(sample) for sample in samples) / CHUNK
                
                # Voice detection logic
                if energy > THRESHOLD:
                    if not voice_active:
                        print("Voice detected!")
                        voice_active = True
                    silence_counter = 0
                else:
                    silence_counter += 1
                    # If silence for several chunks, mark as no voice
                    if voice_active and silence_counter > 10:
                        print("Silence detected.")
                        voice_active = False
                
                # Visual energy meter
                meter_length = int(energy / 200)
                meter = "*" * meter_length
                print(f"Energy: {energy:.0f} {meter}", end="\r")
                
                time.sleep(0.01)
        
        except KeyboardInterrupt:
            print("\n\nVoice detection stopped.")
        except Exception as e:
            print(f"Error in voice detection: {e}")
        finally:
            # Clean up
            if 'stream' in locals():
                stream.stop_stream()
                stream.close()
            p.terminate()
        '''
    
    # Run the voice detector
    simple_voice_detector()


# --------------------------------------------------
# Exercise 4: Audio Effects
# --------------------------------------------------

def exercise_4():
    '''
    EXERCISE 4: Audio Effects
    
    In this exercise, you'll implement an audio effect processor that
    applies effects to audio from the microphone in real-time.
    
    Your task:
    1. Implement a simple effect (e.g., echo)
    2. Process microphone audio in real-time
    3. Play the processed audio back through speakers
    '''
    print("\nEXERCISE 4: Audio Effects")
    print("=====================")
    print("This exercise will help you implement real-time audio effects.")
    
    # Audio effect options
    print("\nAvailable Effects:")
    print("1. Echo")
    print("2. Distortion")
    print("3. Tremolo")
    
    effect = input("\nChoose an effect (1-3): ")
    
    # TODO: Implement the real-time audio effect processor
    def apply_audio_effect(effect_choice):
        '''
        Creates a real-time audio processor that applies effects.
        '''
        # Audio parameters
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 16000
        CHUNK = 1024
        
        # TODO: Initialize effect parameters based on chosen effect
        # For echo: delay buffer, delay time, decay factor
        # For distortion: drive/intensity factor
        # For tremolo: rate, depth, phase
        
        # TODO: Initialize PyAudio
        
        # TODO: Implement the real-time processing callback function
        # The callback should:
        # 1. Convert input data to samples
        # 2. Apply the chosen effect to the samples
        # 3. Convert processed samples back to bytes
        # 4. Return the processed data
        
        # TODO: Open a duplex stream (both input and output)
        # with the processing callback
        
        # TODO: Keep the stream active until user stops it
        
        # TODO: Clean up when done
        
        print("Audio effects processor not yet implemented!")
        
        '''
        # SOLUTION (uncomment to see it work)
        # Audio parameters
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 16000
        CHUNK = 1024
        MAX_AMPLITUDE = 32767
        
        # Initialize PyAudio
        p = pyaudio.PyAudio()
        
        # Set up effect-specific parameters
        if effect_choice == "1":  # Echo
            print("\nApplying echo effect...")
            # Echo parameters
            delay_seconds = 0.3
            delay_samples = int(RATE * delay_seconds)
            decay = 0.5
            
            # Echo buffer
            buffer = [0] * delay_samples
            buffer_index = 0
            
            # Echo processing callback
            def process_callback(in_data, frame_count, time_info, status):
                nonlocal buffer_index
                
                # Convert input data to samples
                samples = struct.unpack(f"{frame_count}h", in_data)
                
                # Process each sample with echo effect
                output = []
                for i in range(frame_count):
                    # Get the delayed sample from the buffer
                    echo_sample = buffer[buffer_index]
                    
                    # Create output sample (input + delayed echo)
                    output_sample = samples[i] + int(echo_sample * decay)
                    
                    # Prevent clipping
                    output_sample = max(min(output_sample, 32767), -32768)
                    
                    # Store current input in buffer for future echo
                    buffer[buffer_index] = samples[i]
                    
                    # Advance buffer index and wrap around
                    buffer_index = (buffer_index + 1) % delay_samples
                    
                    # Add to output
                    output.append(output_sample)
                
                # Convert back to bytes
                out_data = struct.pack(f"{frame_count}h", *output)
                return out_data, pyaudio.paContinue
        
        elif effect_choice == "2":  # Distortion
            print("\nApplying distortion effect...")
            drive = 8.0  # Distortion intensity
            
            def process_callback(in_data, frame_count, time_info, status):
                # Convert input data to samples
                samples = struct.unpack(f"{frame_count}h", in_data)
                
                # Apply distortion effect
                output = []
                for sample in samples:
                    # Normalize to -1.0 to 1.0
                    normalized = sample / MAX_AMPLITUDE
                    
                    # Apply distortion using a simple formula
                    # (approximating tanh)
                    x = normalized * drive
                    if x > 5.0:
                        distorted = 1.0
                    elif x < -5.0:
                        distorted = -1.0
                    else:
                        distorted = x / (1 + abs(x))
                    
                    # Convert back to int16 range
                    output.append(int(distorted * MAX_AMPLITUDE))
                
                # Convert back to bytes
                out_data = struct.pack(f"{frame_count}h", *output)
                return out_data, pyaudio.paContinue
                
        elif effect_choice == "3":  # Tremolo
            print("\nApplying tremolo effect...")
            # Tremolo parameters
            rate = 5.0  # Hz
            depth = 0.5  # 0-1
            phase = 0.0
            
            def process_callback(in_data, frame_count, time_info, status):
                nonlocal phase
                
                # Convert input data to samples
                samples = struct.unpack(f"{frame_count}h", in_data)
                
                # Apply tremolo effect
                output = []
                for i in range(frame_count):
                    # Calculate the tremolo value using sine wave
                    tremolo = 1.0 - depth + depth * math.sin(phase)
                    
                    # Apply to sample
                    output.append(int(samples[i] * tremolo))
                    
                    # Update phase for next sample
                    phase += 2.0 * math.pi * rate / RATE
                    if phase > 2.0 * math.pi:
                        phase -= 2.0 * math.pi
                
                # Convert back to bytes
                out_data = struct.pack(f"{frame_count}h", *output)
                return out_data, pyaudio.paContinue
        
        else:
            print("Invalid effect choice.")
            p.terminate()
            return
        
        try:
            # Open a duplex stream with callback
            stream = p.open(
                format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK,
                stream_callback=process_callback
            )
            
            # Start the stream
            stream.start_stream()
            
            print("\nProcessing audio with effect...")
            print("Speak into your microphone to hear the effect.")
            print("Press Ctrl+C to stop.")
            
            # Keep the stream active
            while stream.is_active():
                time.sleep(0.1)
        
        except KeyboardInterrupt:
            print("\nAudio effect processing stopped by user.")
        except Exception as e:
            print(f"\nError in audio processing: {e}")
        finally:
            # Clean up
            if 'stream' in locals():
                stream.stop_stream()
                stream.close()
            p.terminate()
        '''
    
    apply_audio_effect(effect)


# --------------------------------------------------
# MENU
# --------------------------------------------------

def practice_menu():
    '''
    Display practice exercises menu
    '''
    print("\nAUDIO PROCESSING PRACTICE EXERCISES")
    print("================================")
    print("1. Audio Data Explorer")
    print("2. Audio Transformations")
    print("3. Voice Activity Detection")
    print("4. Audio Effects")
    print("5. Return to main menu")
    
    choice = input("\nEnter exercise number (1-5): ")
    
    if choice == "1":
        exercise_1()
        return True
    elif choice == "2":
        exercise_2()
        return True
    elif choice == "3":
        exercise_3()
        return True
    elif choice == "4":
        exercise_4()
        return True
    elif choice == "5":
        return False
    else:
        print("Invalid choice. Please try again.")
        return True


# --------------------------------------------------
# MAIN EXECUTION
# --------------------------------------------------

if __name__ == "__main__":
    print("\nWelcome to the Audio Processing Practice Exercises!")
    print("These exercises will help you develop practical skills in audio processing.")
    print("Review the concepts in 04_audio_processing_concepts.py if needed.")
    
    running = True
    while running:
        running = practice_menu()
    
    print("\nThank you for practicing audio processing techniques!")
