# Advanced PyAudio: Practice
'''
This file provides hands-on practice exercises for advanced PyAudio concepts.
Complete each exercise to gain practical experience with advanced audio processing techniques.

Before starting, review the concepts in 05_advanced_concepts.py
'''

import pyaudio
import wave
import time
import struct
import math
import sys
import os

# --------------------------------------------------
# Exercise 1: Non-blocking Audio Streams
# --------------------------------------------------

def exercise_1():
    '''
    EXERCISE 1: Non-blocking Audio Playback
    
    In this exercise, you'll implement non-blocking audio playback
    that allows your program to continue running while audio plays.
    
    Your task:
    1. Complete the function to play audio in a non-blocking way
    2. Implement a simple animation or counter that runs during playback
    3. Add user controls to pause/resume playback
    '''
    print("\nEXERCISE 1: Non-blocking Audio Playback")
    print("====================================")
    print("This exercise will help you implement non-blocking audio streams.")
    
    def non_blocking_playback(filename):
        '''
        TODO: Implement non-blocking audio playback
        
        Your implementation should:
        1. Open the audio file using wave
        2. Create a callback function that provides audio data
        3. Use the callback with a PyAudio stream
        4. Show some visual indication that the program is still running
        5. Allow the user to control playback (optional)
        '''
        if not os.path.exists(filename):
            print(f"Error: File {filename} does not exist")
            return
        
        # TODO: Open the WAV file
        
        # TODO: Define a callback function that:
        # - Reads frames from the WAV file
        # - Returns (data, pyaudio.paContinue) when there's more data
        # - Returns (data, pyaudio.paComplete) when the file ends
        
        # TODO: Set up PyAudio and create a non-blocking stream
        
        # TODO: Implement some animation or processing to show non-blocking nature
        
        print("Non-blocking playback not yet implemented!")
        
        '''
        # SOLUTION (uncomment to see it work)
        try:
            # Open the WAV file
            wf = wave.open(filename, 'rb')
            
            # Initialize PyAudio
            p = pyaudio.PyAudio()
            
            # Get file properties
            channels = wf.getnchannels()
            sample_width = wf.getsampwidth()
            framerate = wf.getframerate()
            
            # Create callback function
            def callback(in_data, frame_count, time_info, status):
                data = wf.readframes(frame_count)
                
                # When we run out of data, return empty bytes and pyaudio.paComplete
                if len(data) < 2 * frame_count:
                    # End of file
                    return (data, pyaudio.paComplete)
                
                return (data, pyaudio.paContinue)
            
            # Open a stream with the callback
            stream = p.open(
                format=p.get_format_from_width(sample_width),
                channels=channels,
                rate=framerate,
                output=True,
                stream_callback=callback
            )
            
            # Start the stream - returns immediately
            stream.start_stream()
            
            print(f"\nPlaying {filename} non-blocking...")
            print("The audio is playing in the background.")
            print("Press Ctrl+C to stop or 'p' to pause/resume")
            
            # Keep the stream active until it's finished playing
            animation = "-\\|/-"
            idx = 0
            paused = False
            
            try:
                while stream.is_active() or paused:
                    # Display an animation to show we're active
                    print(f"\rStatus: {'Paused' if paused else 'Playing'} {animation[idx % len(animation)]}", end="")
                    idx += 1
                    
                    # Check for keyboard input (non-blocking)
                    if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
                        key = sys.stdin.read(1)
                        if key == 'p':  # Toggle pause/resume
                            if paused:
                                stream.start_stream()
                                paused = False
                            else:
                                stream.stop_stream()
                                paused = True
                    
                    time.sleep(0.1)
                
                print("\nPlayback finished!")
            
            except KeyboardInterrupt:
                print("\nPlayback stopped by user")
            
            # Clean up
            stream.stop_stream()
            stream.close()
            wf.close()
            p.terminate()
        
        except Exception as e:
            print(f"Error in non-blocking playback: {e}")
        '''
    
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
    
    non_blocking_playback(filename)


# --------------------------------------------------
# Exercise 2: Real-time Echo Processing
# --------------------------------------------------

def exercise_2():
    '''
    EXERCISE 2: Real-time Echo Effect
    
    In this exercise, you'll implement a real-time echo effect
    that processes microphone input and plays it back with an echo.
    
    Your task:
    1. Create a callback function that adds an echo effect
    2. Use a circular buffer to store past audio samples
    3. Mix the current input with delayed samples to create echo
    4. Allow the user to adjust echo parameters (optional)
    '''
    print("\nEXERCISE 2: Real-time Echo Effect")
    print("==============================")
    print("This exercise will help you implement real-time audio processing with callbacks.")
    
    def real_time_echo():
        '''
        TODO: Implement a real-time echo effect
        
        Your implementation should:
        1. Set up appropriate audio parameters
        2. Create a buffer to store delayed audio samples
        3. Implement a callback function that adds an echo
        4. Open a duplex (input+output) stream with the callback
        5. Run until the user terminates the program
        '''
        # TODO: Set up audio parameters (format, channels, rate, chunk size)
        
        # TODO: Set up echo parameters (delay time, decay factor)
        
        # TODO: Create a buffer for the echo
        
        # TODO: Implement the callback function to add echo
        
        # TODO: Create and start the duplex stream
        
        print("Real-time echo processing not yet implemented!")
        
        '''
        # SOLUTION (uncomment to see it work)
        # Audio parameters
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 16000
        CHUNK = 1024
        
        # Echo parameters
        DELAY_SEC = 0.3
        DELAY_SAMPLES = int(RATE * DELAY_SEC)
        DECAY = 0.5  # Echo volume factor
        
        # Initialize PyAudio
        p = pyaudio.PyAudio()
        
        # Create a circular buffer for the echo
        buffer = [0] * DELAY_SAMPLES
        buffer_index = 0
        
        # Callback function for real-time processing
        def process_audio(in_data, frame_count, time_info, status):
            nonlocal buffer_index
            
            # Convert input data to samples
            samples = struct.unpack(f"{frame_count}h", in_data)
            
            # Process each sample
            output_samples = []
            for i in range(frame_count):
                # Get the delayed sample from the buffer
                echo_sample = buffer[buffer_index]
                
                # Current sample + echo (with decay)
                output_sample = samples[i] + int(echo_sample * DECAY)
                
                # Prevent clipping by clamping to valid range
                output_sample = max(min(output_sample, 32767), -32768)
                
                # Store current sample in buffer (for future echo)
                buffer[buffer_index] = samples[i]
                
                # Move buffer index
                buffer_index = (buffer_index + 1) % DELAY_SAMPLES
                
                # Add processed sample to output
                output_samples.append(output_sample)
            
            # Convert samples back to bytes
            out_data = struct.pack(f"{frame_count}h", *output_samples)
            
            return (out_data, pyaudio.paContinue)
        
        try:
            # Open a full-duplex stream (both input and output)
            stream = p.open(
                format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK,
                stream_callback=process_audio
            )
            
            # Start the stream - returns immediately
            stream.start_stream()
            
            print("\nProcessing audio with echo effect...")
            print("Speak into your microphone to hear the echo.")
            print("(Press Ctrl+C to stop)")
            
            # Keep the stream active
            animation = "-\\|/-"
            idx = 0
            while stream.is_active():
                print(f"\rActive {animation[idx % len(animation)]}", end="")
                idx += 1
                time.sleep(0.1)
        
        except KeyboardInterrupt:
            print("\nAudio processing stopped by user")
        except Exception as e:
            print(f"Error in audio processing: {e}")
        finally:
            # Clean up
            if 'stream' in locals():
                stream.stop_stream()
                stream.close()
            p.terminate()
        '''
    
    # Run the real-time echo processor
    real_time_echo()


# --------------------------------------------------
# Exercise 3: Multi-effect Audio Processor
# --------------------------------------------------

def exercise_3():
    '''
    EXERCISE 3: Multi-effect Audio Processor
    
    In this exercise, you'll implement an audio processor that
    can apply multiple effects to microphone input in real-time.
    
    Your task:
    1. Implement multiple audio effects (echo, distortion, tremolo, etc.)
    2. Create a menu system to select effects
    3. Allow real-time parameter adjustments (optional)
    4. Enable chaining multiple effects together (optional advanced)
    '''
    print("\nEXERCISE 3: Multi-effect Audio Processor")
    print("===================================")
    print("This exercise will help you implement multiple real-time audio effects.")
    
    def audio_effects_processor():
        '''
        TODO: Implement a multi-effect audio processor
        
        Your implementation should:
        1. Define several audio effects (at least 2-3)
        2. Allow the user to select which effect to use
        3. Process audio in real-time using the selected effect
        4. (Optional) Allow switching effects or parameters while running
        '''
        # TODO: Set up audio parameters
        
        # TODO: Define multiple effects (echo, distortion, tremolo, etc.)
        
        # TODO: Create a menu for selecting effects
        
        # TODO: Implement the callback function for the selected effect
        
        # TODO: Create and run the audio stream
        
        print("Multi-effect processor not yet implemented!")
        
        '''
        # SOLUTION (uncomment to see it work)
        # Audio parameters
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 16000
        CHUNK = 1024
        MAX_AMPLITUDE = 32767
        
        # Effect parameters
        effects = {
            'none': {
                'name': 'No Effect (Pass-through)',
                'description': 'No processing applied'
            },
            'echo': {
                'name': 'Echo',
                'description': 'Adds echo/delay to the audio',
                'delay_samples': int(RATE * 0.3),  # 300ms delay
                'decay': 0.5,
                'buffer': [0] * (int(RATE * 0.3)),
                'buffer_index': 0
            },
            'distortion': {
                'name': 'Distortion',
                'description': 'Adds distortion/overdrive',
                'drive': 8.0  # Distortion intensity
            },
            'tremolo': {
                'name': 'Tremolo',
                'description': 'Modulates the volume',
                'rate': 5.0,  # Hz
                'depth': 0.5,  # 0-1
                'phase': 0.0
            }
        }
        
        # Display effect options
        print("\nAvailable effects:")
        for i, effect_key in enumerate(effects.keys()):
            print(f"{i+1}. {effects[effect_key]['name']}")
            print(f"   {effects[effect_key]['description']}")
        
        # Choose effect
        choice = input("\nSelect effect number: ")
        try:
            index = int(choice) - 1
            if 0 <= index < len(effects):
                current_effect = list(effects.keys())[index]
            else:
                print("Invalid choice, using no effect")
                current_effect = 'none'
        except ValueError:
            print("Invalid input, using no effect")
            current_effect = 'none'
        
        print(f"\nSelected effect: {effects[current_effect]['name']}")
        
        # Initialize PyAudio
        p = pyaudio.PyAudio()
        
        # Callback function for real-time processing
        def process_audio(in_data, frame_count, time_info, status):
            # Convert input data to samples
            samples = struct.unpack(f"{frame_count}h", in_data)
            
            # Create output samples based on the current effect
            output_samples = [0] * frame_count
            
            if current_effect == 'none':
                # No effect - straight pass-through
                output_samples = samples
            
            elif current_effect == 'echo':
                # Echo effect
                echo_params = effects['echo']
                buffer = echo_params['buffer']
                buffer_index = echo_params['buffer_index']
                decay = echo_params['decay']
                
                for i in range(frame_count):
                    # Get the delayed sample from the buffer
                    echo_sample = buffer[buffer_index]
                    
                    # Current sample + echo (with decay)
                    output_samples[i] = samples[i] + int(echo_sample * decay)
                    
                    # Prevent clipping
                    output_samples[i] = max(min(output_samples[i], MAX_AMPLITUDE), -MAX_AMPLITUDE)
                    
                    # Store current sample in buffer (for future echo)
                    buffer[buffer_index] = samples[i]
                    
                    # Move buffer index
                    buffer_index = (buffer_index + 1) % len(buffer)
                
                # Save the buffer state for next callback
                effects['echo']['buffer'] = buffer
                effects['echo']['buffer_index'] = buffer_index
            
            elif current_effect == 'distortion':
                # Distortion effect
                drive = effects['distortion']['drive']
                
                for i in range(frame_count):
                    # Normalize to -1.0 to 1.0 range
                    normalized = samples[i] / MAX_AMPLITUDE
                    
                    # Apply distortion (tanh is a good distortion curve)
                    # Simulating tanh with a simple formula
                    x = normalized * drive
                    if x > 5.0:
                        distorted = 1.0
                    elif x < -5.0:
                        distorted = -1.0
                    else:
                        distorted = x / (1 + abs(x))
                    
                    # Convert back to int16 range
                    output_samples[i] = int(distorted * MAX_AMPLITUDE)
            
            elif current_effect == 'tremolo':
                # Tremolo effect (amplitude modulation)
                tremolo_params = effects['tremolo']
                rate = tremolo_params['rate']
                depth = tremolo_params['depth']
                phase = tremolo_params['phase']
                
                for i in range(frame_count):
                    # Calculate the LFO value (sine wave) for tremolo
                    # Using simplified sine approximation
                    lfo = 1.0 - depth + depth * math.sin(phase)
                    
                    # Apply tremolo
                    output_samples[i] = int(samples[i] * lfo)
                    
                    # Update phase for next sample
                    phase += 2.0 * math.pi * rate / RATE
                    
                    # Keep phase in sensible range
                    if phase > 2.0 * math.pi:
                        phase -= 2.0 * math.pi
                
                # Save phase for next callback
                effects['tremolo']['phase'] = phase
            
            # Convert samples back to bytes
            out_data = struct.pack(f"{frame_count}h", *output_samples)
            
            return (out_data, pyaudio.paContinue)
        
        try:
            # Open a full-duplex stream
            stream = p.open(
                format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK,
                stream_callback=process_audio
            )
            
            # Start the stream
            stream.start_stream()
            
            print("\nProcessing audio with effect...")
            print("Speak into your microphone to hear the effect.")
            print("(Press Ctrl+C to stop)")
            
            # Simple animation to show processing is active
            animation = "|/-\\"
            animation_index = 0
            
            while stream.is_active():
                print(f"\rActive {animation[animation_index % len(animation)]}", end="")
                animation_index += 1
                time.sleep(0.1)
        
        except KeyboardInterrupt:
            print("\n\nAudio processing stopped by user")
        except Exception as e:
            print(f"\nError in audio processing: {e}")
        finally:
            # Clean up
            if 'stream' in locals():
                stream.stop_stream()
                stream.close()
            p.terminate()
        '''
    
    # Run the multi-effect processor
    audio_effects_processor()


# --------------------------------------------------
# Exercise 4: Robust Audio Device Handling
# --------------------------------------------------

def exercise_4():
    '''
    EXERCISE 4: Robust Audio Device Handling
    
    In this exercise, you'll implement robust audio device handling
    with proper error checking and fallback strategies.
    
    Your task:
    1. List all available audio devices
    2. Allow selecting a device for recording
    3. Implement error handling and fallback strategies
    4. Create a short recording to test the selected device
    '''
    print("\nEXERCISE 4: Robust Audio Device Handling")
    print("====================================")
    print("This exercise will help you implement robust audio device handling.")
    
    def robust_audio_handling():
        '''
        TODO: Implement robust audio device handling
        
        Your implementation should:
        1. List available audio devices
        2. Let the user select a device
        3. Try to open a stream with the selected device
        4. Fall back to alternative configurations if that fails
        5. Record a short audio clip as a test
        '''
        # TODO: Initialize PyAudio
        
        # TODO: List all available devices
        
        # TODO: Allow user to select a device
        
        # TODO: Try to open a stream with selected device
        # and handle any errors that occur
        
        # TODO: Record a short test clip
        
        print("Robust audio handling not yet implemented!")
        
        '''
        # SOLUTION (uncomment to see it work)
        try:
            # Initialize PyAudio
            p = pyaudio.PyAudio()
            
            # Get device count
            device_count = p.get_device_count()
            
            if device_count == 0:
                print("Error: No audio devices found")
                return
            
            # List all available devices
            print("\nAvailable audio devices:")
            for i in range(device_count):
                device_info = p.get_device_info_by_index(i)
                name = device_info['name']
                max_input_ch = device_info['maxInputChannels']
                max_output_ch = device_info['maxOutputChannels']
                
                print(f"{i}: {name}")
                print(f"   Input channels: {max_input_ch}, Output channels: {max_output_ch}")
                print(f"   Default sample rate: {device_info['defaultSampleRate']} Hz")
                
            # Ask user to select an input device
            device_choice = input("\nSelect input device number (or press Enter for default): ")
            
            input_device_index = None
            if device_choice.strip():
                try:
                    input_device_index = int(device_choice)
                    if input_device_index < 0 or input_device_index >= device_count:
                        print("Invalid device number, using default")
                        input_device_index = None
                except ValueError:
                    print("Invalid input, using default device")
                    input_device_index = None
            
            # Get the selected device info
            if input_device_index is not None:
                device_info = p.get_device_info_by_index(input_device_index)
            else:
                device_info = p.get_default_input_device_info()
                input_device_index = p.get_default_input_device_info()['index']
                print(f"Using default device: {device_info['name']}")
            
            # Check if it supports input
            if device_info['maxInputChannels'] == 0:
                print("Selected device doesn't support input, looking for alternative...")
                
                # Find a viable input device
                for i in range(device_count):
                    alt_device = p.get_device_info_by_index(i)
                    if alt_device['maxInputChannels'] > 0:
                        input_device_index = i
                        device_info = alt_device
                        print(f"Using alternative input device: {device_info['name']}")
                        break
                else:
                    print("No input devices available!")
                    return
            
            # Audio parameters
            FORMAT = pyaudio.paInt16
            CHANNELS = min(1, device_info['maxInputChannels'])  # Use mono if supported
            RATE = int(device_info['defaultSampleRate'])
            CHUNK = 1024
            RECORD_SECONDS = 5
            
            # Try to open stream with these parameters
            try:
                print(f"\nTrying to open stream with:")
                print(f"- Device: {device_info['name']}")
                print(f"- Sample rate: {RATE} Hz")
                print(f"- Channels: {CHANNELS}")
                
                stream = p.open(
                    format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    input_device_index=input_device_index,
                    frames_per_buffer=CHUNK
                )
            except Exception as e:
                print(f"Error opening stream: {e}")
                print("Trying alternative configuration...")
                
                # Try with lower sample rate
                RATE = 16000
                try:
                    print(f"Trying sample rate: {RATE} Hz")
                    stream = p.open(
                        format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        input_device_index=input_device_index,
                        frames_per_buffer=CHUNK
                    )
                except Exception as e:
                    print(f"Still failed: {e}")
                    print("Audio recording not available with this device.")
                    return
            
            print("\nStream successfully opened!")
            print(f"Recording {RECORD_SECONDS} seconds as a test...")
            
            # Record data
            frames = []
            for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
                try:
                    data = stream.read(CHUNK, exception_on_overflow=False)
                    frames.append(data)
                    
                    # Print progress
                    if i % 5 == 0:
                        progress = (i / (RATE / CHUNK * RECORD_SECONDS)) * 100
                        print(f"\rRecording: {progress:.0f}%", end="")
                except Exception as e:
                    print(f"\nWarning during recording: {e}")
            
            print("\nRecording complete!")
            
            # Close stream
            stream.stop_stream()
            stream.close()
            
            # Save recording
            WAVE_OUTPUT_FILENAME = "robust_test.wav"
            
            try:
                with wave.open(WAVE_OUTPUT_FILENAME, 'wb') as wf:
                    wf.setnchannels(CHANNELS)
                    wf.setsampwidth(p.get_sample_size(FORMAT))
                    wf.setframerate(RATE)
                    wf.writeframes(b''.join(frames))
                
                print(f"Test recording saved to {WAVE_OUTPUT_FILENAME}")
            except Exception as e:
                print(f"Error saving recording: {e}")
            
        except Exception as e:
            print(f"Error in audio device handling: {e}")
        finally:
            if 'p' in locals():
                p.terminate()
        '''
    
    # Run the robust audio handling exercise
    robust_audio_handling()


# --------------------------------------------------
# Exercise 5: Multi-Stream Management
# --------------------------------------------------

def exercise_5():
    '''
    EXERCISE 5: Multi-Stream Management
    
    In this exercise, you'll work with multiple audio streams simultaneously,
    such as playing background music while recording voice.
    
    Your task:
    1. Create and manage multiple audio streams
    2. Implement proper synchronization between streams
    3. Allow independent control of each stream
    4. Ensure proper resource management and cleanup
    '''
    print("\nEXERCISE 5: Multi-Stream Management")
    print("===============================")
    print("This exercise will help you manage multiple audio streams.")
    
    def multi_stream_manager():
        '''
        TODO: Implement a multi-stream audio manager
        
        Your implementation should:
        1. Create at least two streams (e.g., one for playback, one for recording)
        2. Manage these streams independently
        3. Provide user controls to interact with the streams
        4. Clean up all resources properly
        '''
        # TODO: Initialize PyAudio
        
        # TODO: Set up parameters for multiple streams
        
        # TODO: Create and manage the streams
        
        # TODO: Implement user controls
        
        print("Multi-stream management not yet implemented!")
        
        '''
        # SOLUTION (uncomment to see it work)
        # Initialize PyAudio
        p = pyaudio.PyAudio()
        
        # Find a WAV file for playback
        wav_files = [f for f in os.listdir('.') if f.endswith('.wav')]
        playback_file = None
        
        if wav_files:
            print("\nAvailable WAV files for background playback:")
            for i, file in enumerate(wav_files):
                print(f"{i+1}. {file}")
            
            choice = input("Select a file for background playback (Enter to skip): ")
            
            if choice.strip():
                try:
                    idx = int(choice) - 1
                    if 0 <= idx < len(wav_files):
                        playback_file = wav_files[idx]
                except ValueError:
                    pass
        
        # Audio parameters
        RECORD_FORMAT = pyaudio.paInt16
        RECORD_CHANNELS = 1
        RECORD_RATE = 16000
        RECORD_CHUNK = 1024
        
        # Set up streams
        recording_stream = None
        playback_stream = None
        recording_frames = []
        playback_wf = None
        
        # Recording callback
        def recording_callback(in_data, frame_count, time_info, status):
            recording_frames.append(in_data)
            return (None, pyaudio.paContinue)
        
        # Playback callback (if a file was selected)
        if playback_file:
            try:
                playback_wf = wave.open(playback_file, 'rb')
                playback_channels = playback_wf.getnchannels()
                playback_rate = playback_wf.getframerate()
                playback_format = p.get_format_from_width(playback_wf.getsampwidth())
                
                def playback_callback(in_data, frame_count, time_info, status):
                    data = playback_wf.readframes(frame_count)
                    
                    # If end of file, loop by rewinding
                    if len(data) < frame_count * playback_channels * 2:  # assuming 16-bit
                        playback_wf.rewind()
                        data += playback_wf.readframes(frame_count - len(data)//(playback_channels*2))
                    
                    return (data, pyaudio.paContinue)
            
            except Exception as e:
                print(f"Error opening playback file: {e}")
                playback_wf = None
        
        try:
            # Open recording stream
            print("\nOpening recording stream...")
            recording_stream = p.open(
                format=RECORD_FORMAT,
                channels=RECORD_CHANNELS,
                rate=RECORD_RATE,
                input=True,
                frames_per_buffer=RECORD_CHUNK,
                stream_callback=recording_callback
            )
            
            # Open playback stream if a file was selected
            if playback_wf:
                print("Opening background playback stream...")
                playback_stream = p.open(
                    format=playback_format,
                    channels=playback_channels,
                    rate=playback_rate,
                    output=True,
                    frames_per_buffer=RECORD_CHUNK,
                    stream_callback=playback_callback
                )
            
            # Control interface
            print("\nMULTI-STREAM MANAGER")
            print("===================")
            print("Controls:")
            print("r - Start/stop recording")
            print("p - Play/pause background music")
            print("s - Save current recording")
            print("q - Quit")
            
            recording_active = False
            playback_active = False
            
            if playback_wf:
                playback_stream.start_stream()
                playback_active = True
            
            while True:
                print("\nStatus:")
                print(f"Recording: {'ACTIVE' if recording_active else 'PAUSED'}")
                print(f"Playback : {'ACTIVE' if playback_active else 'PAUSED'}")
                
                cmd = input("\nEnter command (r/p/s/q): ").lower()
                
                if cmd == 'r':
                    if recording_active:
                        print("Pausing recording...")
                        recording_stream.stop_stream()
                        recording_active = False
                    else:
                        print("Starting recording...")
                        recording_stream.start_stream()
                        recording_active = True
                
                elif cmd == 'p' and playback_stream:
                    if playback_active:
                        print("Pausing background playback...")
                        playback_stream.stop_stream()
                        playback_active = False
                    else:
                        print("Resuming background playback...")
                        playback_stream.start_stream()
                        playback_active = True
                
                elif cmd == 's' and recording_frames:
                    filename = input("Enter filename to save recording: ")
                    if not filename.endswith('.wav'):
                        filename += '.wav'
                    
                    try:
                        with wave.open(filename, 'wb') as wf:
                            wf.setnchannels(RECORD_CHANNELS)
                            wf.setsampwidth(p.get_sample_size(RECORD_FORMAT))
                            wf.setframerate(RECORD_RATE)
                            wf.writeframes(b''.join(recording_frames))
                        
                        print(f"Recording saved to {filename}")
                        # Clear frames after saving
                        recording_frames = []
                    except Exception as e:
                        print(f"Error saving recording: {e}")
                
                elif cmd == 'q':
                    print("Quitting...")
                    break
                
                else:
                    print("Unknown command")
        
        except KeyboardInterrupt:
            print("\nProgram interrupted by user")
        except Exception as e:
            print(f"Error in multi-stream manager: {e}")
        finally:
            # Clean up all resources
            if recording_stream:
                recording_stream.stop_stream()
                recording_stream.close()
            
            if playback_stream:
                playback_stream.stop_stream()
                playback_stream.close()
            
            if playback_wf:
                playback_wf.close()
            
            p.terminate()
            print("All audio resources cleaned up")
        '''
    
    # Run the multi-stream manager
    multi_stream_manager()


# --------------------------------------------------
# MENU
# --------------------------------------------------

def practice_menu():
    '''
    Display practice exercises menu
    '''
    print("\nADVANCED PYAUDIO PRACTICE EXERCISES")
    print("=================================")
    print("1. Non-blocking Audio Streams")
    print("2. Real-time Echo Processing")
    print("3. Multi-effect Audio Processor")
    print("4. Robust Audio Device Handling")
    print("5. Multi-Stream Management")
    print("6. Return to main menu")
    
    choice = input("\nEnter exercise number (1-6): ")
    
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
        exercise_5()
        return True
    elif choice == "6":
        return False
    else:
        print("Invalid choice. Please try again.")
        return True


# --------------------------------------------------
# MAIN EXECUTION
# --------------------------------------------------

if __name__ == "__main__":
    print("\nWelcome to the Advanced PyAudio Practice Exercises!")
    print("These exercises will help you develop practical skills in advanced audio processing.")
    print("Review the concepts in 05_advanced_concepts.py if needed.")
    
    running = True
    while running:
        running = practice_menu()
    
    print("\nThank you for practicing advanced PyAudio techniques!")
