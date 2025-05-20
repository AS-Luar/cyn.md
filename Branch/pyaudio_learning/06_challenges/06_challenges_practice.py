# PyAudio Challenges: Practice
'''
This file contains challenging exercises to test and extend your PyAudio skills.
Each challenge builds on concepts from previous modules and requires you to
combine multiple skills to create functional audio applications.

Before starting, you may want to review the concepts in 06_challenges_concepts.py
'''

import pyaudio
import wave
import time
import os
import struct
import datetime
import sys
import math

# --------------------------------------------------
# Challenge 1: Voice-Activated Recorder
# --------------------------------------------------

def challenge_1():
    '''
    CHALLENGE 1: Voice-Activated Recorder
    
    Create a voice memo recorder that automatically starts recording when
    it detects someone speaking and stops after detecting silence.
    
    Requirements:
    1. Monitor audio levels to detect when speech starts
    2. Begin recording when speech is detected
    3. Automatically stop recording after a period of silence
    4. Save the recording with a timestamp filename
    
    Bonus:
    - Include a short pre-buffer to capture the very beginning of speech
    - Implement a visualization of audio levels during monitoring
    '''
    print("\nCHALLENGE 1: Voice-Activated Recorder")
    print("====================================")
    print("This challenge is to create a recorder that automatically")
    print("activates when you begin speaking and stops when you're done.")
    
    def voice_activated_recorder():
        '''
        TODO: Implement a voice-activated recorder
        
        Your implementation should:
        1. Monitor audio levels from the microphone
        2. Start recording when the level exceeds a threshold
        3. Stop recording after a period of silence
        4. Save the recording with a timestamp
        '''
        # Audio parameters
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 16000
        CHUNK = 1024
        
        # Detection parameters
        THRESHOLD = 1000  # Adjust this for your microphone
        SILENCE_LIMIT = 2  # Seconds of silence before stopping
        
        # TODO: Initialize PyAudio
        
        # TODO: Set up audio stream to monitor levels
        
        # TODO: Implement the detection and recording logic
        # - Monitor audio levels
        # - Start recording when level exceeds threshold
        # - Keep recording until silence is detected
        # - Save the recording
        
        print("Voice-activated recorder not yet implemented!")
        
        '''
        # SOLUTION (uncomment to see it work)
        # Initialize PyAudio
        p = pyaudio.PyAudio()
        
        try:
            # Open stream for monitoring
            stream = p.open(
                format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK
            )
            
            print("Listening for speech... (Press Ctrl+C to stop)")
            print("Speak to activate recording")
            
            # State variables
            recording = False
            frames = []
            silent_chunks = 0
            energy_threshold = THRESHOLD
            
            # Optional: short buffer for pre-recording
            pre_buffer = []
            PRE_BUFFER_SIZE = 3  # chunks
            
            while True:
                # Read audio chunk
                data = stream.read(CHUNK, exception_on_overflow=False)
                
                # Calculate energy
                values = struct.unpack(f"{CHUNK}h", data)
                energy = sum(abs(val) for val in values) / CHUNK
                
                # Optional: Add to pre-buffer
                pre_buffer.append(data)
                if len(pre_buffer) > PRE_BUFFER_SIZE:
                    pre_buffer.pop(0)
                
                # Visual indicator
                meter = "*" * int(energy / 200)
                print(f"\rEnergy: {energy:.0f} {meter}", end="")
                
                # State management
                if not recording:
                    # Not recording yet - check if we should start
                    if energy > energy_threshold:
                        # Start recording!
                        recording = True
                        
                        # Include pre-buffer to catch the beginning
                        frames.extend(pre_buffer)
                        
                        # Reset silent chunks counter
                        silent_chunks = 0
                        
                        print("\nRecording started...")
                else:
                    # Already recording - add the chunk to frames
                    frames.append(data)
                    
                    # Check if this is silence
                    if energy < energy_threshold:
                        silent_chunks += 1
                        # Check if we've had enough silence to stop
                        if silent_chunks > SILENCE_LIMIT * RATE / CHUNK:
                            # Stop recording
                            print("\nSilence detected - recording stopped")
                            recording = False
                            
                            # Save the recording with timestamp
                            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                            filename = f"voice_memo_{timestamp}.wav"
                            
                            with wave.open(filename, 'wb') as wf:
                                wf.setnchannels(CHANNELS)
                                wf.setsampwidth(p.get_sample_size(FORMAT))
                                wf.setframerate(RATE)
                                wf.writeframes(b''.join(frames))
                            
                            print(f"Recording saved as {filename}")
                            
                            # Reset for next recording
                            frames = []
                            pre_buffer = []
                    else:
                        # Reset silent chunks counter
                        silent_chunks = 0
                
                time.sleep(0.01)
        
        except KeyboardInterrupt:
            print("\nRecording stopped by user")
        except Exception as e:
            print(f"\nError in voice-activated recording: {e}")
        finally:
            # Clean up
            if 'stream' in locals():
                stream.stop_stream()
                stream.close()
            p.terminate()
        '''
    
    # Run the voice-activated recorder
    voice_activated_recorder()


# --------------------------------------------------
# Challenge 2: Audio Format Converter
# --------------------------------------------------

def challenge_2():
    '''
    CHALLENGE 2: Audio Format Converter
    
    Create a utility that converts WAV files between different formats,
    including sample rates, bit depths, and channel configurations.
    
    Requirements:
    1. Allow conversion between different sample rates
    2. Support conversion between different bit depths
    3. Enable conversion between mono and stereo
    4. Provide a user-friendly interface
    
    Bonus:
    - Add batch processing for multiple files
    - Implement file format conversion beyond WAV
    '''
    print("\nCHALLENGE 2: Audio Format Converter")
    print("=================================")
    print("This challenge is to create a utility that can convert")
    print("WAV files between different formats.")
    
    def audio_format_converter():
        '''
        TODO: Implement an audio format converter
        
        Your implementation should:
        1. Allow the user to select a WAV file
        2. Provide options for different conversions
        3. Perform the selected conversion
        4. Save the result as a new file
        '''
        # TODO: Find and list available WAV files
        
        # TODO: Get user selection of file and conversion type
        
        # TODO: Implement conversion functions:
        # - Sample rate conversion
        # - Bit depth conversion
        # - Mono/stereo conversion
        
        # TODO: Perform the selected conversion
        
        # TODO: Save the converted file
        
        print("Audio format converter not yet implemented!")
        
        '''
        # SOLUTION (uncomment to see it work)
        # Find WAV files in current directory
        wav_files = [f for f in os.listdir('.') if f.endswith('.wav')]
        
        if not wav_files:
            print("No WAV files found. Please record or create a WAV file first.")
            return
        
        print("\nFound WAV files:")
        for i, file in enumerate(wav_files):
            print(f"{i+1}. {file}")
        
        # Get input file
        file_choice = input("\nEnter file number to convert: ")
        
        try:
            idx = int(file_choice) - 1
            if 0 <= idx < len(wav_files):
                input_file = wav_files[idx]
            else:
                print("Invalid file number")
                return
        except ValueError:
            print("Invalid input")
            return
        
        # Display file properties
        try:
            with wave.open(input_file, 'rb') as wf:
                channels = wf.getnchannels()
                sample_width = wf.getsampwidth()
                framerate = wf.getframerate()
                n_frames = wf.getnframes()
                
                print(f"\nFile: {input_file}")
                print(f"Channels: {channels} ({'Stereo' if channels == 2 else 'Mono'})")
                print(f"Sample Width: {sample_width * 8} bits")
                print(f"Sample Rate: {framerate} Hz")
                print(f"Duration: {n_frames / framerate:.2f} seconds")
        except Exception as e:
            print(f"Error reading file: {e}")
            return
        
        # Conversion options
        print("\nConversion Options:")
        print("1. Change sample rate")
        print("2. Change bit depth")
        print("3. Convert stereo to mono")
        print("4. Convert mono to stereo")
        
        option = input("Enter conversion option (1-4): ")
        
        # Get output filename
        output_file = input("Enter output filename: ")
        if not output_file.endswith('.wav'):
            output_file += '.wav'
        
        # Perform the conversion
        if option == "1":  # Sample rate
            try:
                new_rate = int(input("Enter new sample rate (e.g., 8000, 16000, 44100, 48000): "))
                if new_rate <= 0:
                    print("Sample rate must be positive")
                    return
                
                # Sample rate conversion (simple version)
                with wave.open(input_file, 'rb') as wf:
                    # Get original parameters
                    channels = wf.getnchannels()
                    sample_width = wf.getsampwidth()
                    old_rate = wf.getframerate()
                    
                    # Read all frames
                    frames = wf.readframes(wf.getnframes())
                    
                    # Create output file with new rate
                    with wave.open(output_file, 'wb') as out_wf:
                        out_wf.setnchannels(channels)
                        out_wf.setsampwidth(sample_width)
                        out_wf.setframerate(new_rate)
                        out_wf.writeframes(frames)
                    
                    print(f"\nSample rate conversion complete")
                    print(f"Original: {old_rate} Hz, New: {new_rate} Hz")
                    print(f"Output saved as {output_file}")
                    print(f"Note: This simple conversion changes playback speed AND pitch.")
                    print(f"For professional resampling, use a library like librosa.")
            
            except ValueError:
                print("Invalid sample rate")
            except Exception as e:
                print(f"Error in sample rate conversion: {e}")
        
        elif option == "2":  # Bit depth
            try:
                new_width = int(input("Enter new bit depth (8 or 16): ")) // 8
                if new_width not in [1, 2]:
                    print("Only 8-bit (1) or 16-bit (2) supported")
                    return
                
                # Bit depth conversion
                with wave.open(input_file, 'rb') as wf:
                    # Get original parameters
                    channels = wf.getnchannels()
                    old_width = wf.getsampwidth()
                    framerate = wf.getframerate()
                    
                    # Create output file with new bit depth
                    with wave.open(output_file, 'wb') as out_wf:
                        out_wf.setnchannels(channels)
                        out_wf.setsampwidth(new_width)
                        out_wf.setframerate(framerate)
                        
                        # Process in chunks
                        CHUNK = 1024
                        while True:
                            data = wf.readframes(CHUNK)
                            if not data:
                                break
                            
                            # Convert between bit depths
                            if old_width == 1 and new_width == 2:
                                # 8-bit to 16-bit
                                samples = struct.unpack(f"{len(data)}B", data)
                                new_samples = []
                                for s in samples:
                                    # Convert 0-255 to -32768-32767
                                    new_samples.append(((s - 128) * 256))
                                data = struct.pack(f"{len(new_samples)}h", *new_samples)
                            
                            elif old_width == 2 and new_width == 1:
                                # 16-bit to 8-bit
                                samples = struct.unpack(f"{len(data)//2}h", data)
                                new_samples = []
                                for s in samples:
                                    # Convert -32768-32767 to 0-255
                                    new_samples.append(int(s / 256) + 128)
                                data = struct.pack(f"{len(new_samples)}B", *new_samples)
                            
                            out_wf.writeframes(data)
                    
                    print(f"\nBit depth conversion complete")
                    print(f"Original: {old_width * 8} bits, New: {new_width * 8} bits")
                    print(f"Output saved as {output_file}")
            
            except ValueError:
                print("Invalid bit depth")
            except Exception as e:
                print(f"Error in bit depth conversion: {e}")
        
        elif option == "3" and channels == 2:  # Stereo to mono
            try:
                # Stereo to mono conversion
                with wave.open(input_file, 'rb') as wf:
                    # Get original parameters
                    sample_width = wf.getsampwidth()
                    framerate = wf.getframerate()
                    
                    # Create mono output file
                    with wave.open(output_file, 'wb') as out_wf:
                        out_wf.setnchannels(1)  # Mono
                        out_wf.setsampwidth(sample_width)
                        out_wf.setframerate(framerate)
                        
                        # Process in chunks
                        CHUNK = 1024
                        while True:
                            data = wf.readframes(CHUNK)
                            if not data:
                                break
                            
                            # Convert stereo to mono
                            if sample_width == 1:
                                # 8-bit samples
                                samples = struct.unpack(f"{len(data)}B", data)
                                mono_samples = []
                                for i in range(0, len(samples), 2):
                                    if i+1 < len(samples):
                                        mono_samples.append((samples[i] + samples[i+1]) // 2)
                                data = struct.pack(f"{len(mono_samples)}B", *mono_samples)
                            
                            elif sample_width == 2:
                                # 16-bit samples
                                samples = struct.unpack(f"{len(data)//2}h", data)
                                mono_samples = []
                                for i in range(0, len(samples), 2):
                                    if i+1 < len(samples):
                                        mono_samples.append((samples[i] + samples[i+1]) // 2)
                                data = struct.pack(f"{len(mono_samples)}h", *mono_samples)
                            
                            out_wf.writeframes(data)
                    
                    print(f"\nStereo to mono conversion complete")
                    print(f"Output saved as {output_file}")
            
            except Exception as e:
                print(f"Error in stereo to mono conversion: {e}")
        
        elif option == "4" and channels == 1:  # Mono to stereo
            try:
                # Mono to stereo conversion
                with wave.open(input_file, 'rb') as wf:
                    # Get original parameters
                    sample_width = wf.getsampwidth()
                    framerate = wf.getframerate()
                    
                    # Create stereo output file
                    with wave.open(output_file, 'wb') as out_wf:
                        out_wf.setnchannels(2)  # Stereo
                        out_wf.setsampwidth(sample_width)
                        out_wf.setframerate(framerate)
                        
                        # Process in chunks
                        CHUNK = 1024
                        while True:
                            data = wf.readframes(CHUNK)
                            if not data:
                                break
                            
                            # Convert mono to stereo
                            if sample_width == 1:
                                # 8-bit samples
                                samples = struct.unpack(f"{len(data)}B", data)
                                stereo_samples = []
                                for s in samples:
                                    stereo_samples.append(s)  # Left
                                    stereo_samples.append(s)  # Right
                                data = struct.pack(f"{len(stereo_samples)}B", *stereo_samples)
                            
                            elif sample_width == 2:
                                # 16-bit samples
                                samples = struct.unpack(f"{len(data)//2}h", data)
                                stereo_samples = []
                                for s in samples:
                                    stereo_samples.append(s)  # Left
                                    stereo_samples.append(s)  # Right
                                data = struct.pack(f"{len(stereo_samples)}h", *stereo_samples)
                            
                            out_wf.writeframes(data)
                    
                    print(f"\nMono to stereo conversion complete")
                    print(f"Output saved as {output_file}")
            
            except Exception as e:
                print(f"Error in mono to stereo conversion: {e}")
        
        else:
            print("Invalid option or incompatible conversion")
        '''
    
    # Run the audio format converter
    audio_format_converter()


# --------------------------------------------------
# Challenge 3: Terminal Audio Visualizer
# --------------------------------------------------

def challenge_3():
    '''
    CHALLENGE 3: Terminal Audio Visualizer
    
    Create a terminal-based audio visualizer that displays real-time
    visualizations of microphone input.
    
    Requirements:
    1. Display a visual representation of audio levels in the terminal
    2. Update the visualization in real-time
    3. Include peak indicators
    4. Work with both mono and stereo input
    
    Bonus:
    - Add color to the visualization (ANSI color codes)
    - Implement a simple frequency analyzer display
    '''
    print("\nCHALLENGE 3: Terminal Audio Visualizer")
    print("====================================")
    print("This challenge is to create a real-time audio visualizer")
    print("that displays audio levels in the terminal.")
    
    def terminal_visualizer():
        '''
        TODO: Implement a terminal-based audio visualizer
        
        Your implementation should:
        1. Capture audio from the microphone
        2. Calculate energy/volume levels
        3. Display a visual representation in the terminal
        4. Update in real-time
        '''
        # Audio parameters
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 16000
        CHUNK = 1024
        
        # TODO: Initialize PyAudio and open stream
        
        # TODO: Set up visualization parameters
        
        # TODO: Implement the visualization loop
        # - Read audio data
        # - Calculate volume/energy
        # - Create and display the visualization
        # - Update in real-time
        
        print("Terminal audio visualizer not yet implemented!")
        
        '''
        # SOLUTION (uncomment to see it work)
        # Initialize PyAudio
        p = pyaudio.PyAudio()
        
        try:
            # Open stream
            stream = p.open(
                format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK
            )
            
            print("Terminal Audio Visualizer")
            print("Press Ctrl+C to stop\n")
            
            # Visualization parameters
            BAR_WIDTH = 50  # Max width of volume bar
            peak_value = 0
            peak_decay = 0.9  # How fast the peak indicator falls
            
            # Main visualization loop
            while True:
                # Read audio data
                data = stream.read(CHUNK, exception_on_overflow=False)
                
                # Convert to samples
                samples = struct.unpack(f"{CHUNK}h", data)
                
                # Calculate volume (RMS - root mean square)
                rms = math.sqrt(sum(sample * sample for sample in samples) / CHUNK)
                
                # Scale to 0-1 range for visualization
                # Adjust the divisor based on your microphone sensitivity
                volume = min(1.0, rms / 10000)
                
                # Update peak value with decay
                peak_value = max(volume, peak_value * peak_decay)
                
                # Create visualization
                bar_length = int(volume * BAR_WIDTH)
                peak_position = int(peak_value * BAR_WIDTH)
                
                # Build the bar with peak indicator
                bar = ""
                for i in range(BAR_WIDTH):
                    if i < bar_length:
                        bar += "█"
                    elif i == peak_position:
                        bar += "▓"
                    else:
                        bar += " "
                
                # Display level meter with numerical value
                db_value = 20 * math.log10(max(volume, 0.0001))  # Convert to dB
                print(f"\rLevel: [{bar}] {db_value:.1f} dB", end="")
                
                # Small delay to control refresh rate
                time.sleep(0.05)
        
        except KeyboardInterrupt:
            print("\n\nVisualizer stopped by user")
        except Exception as e:
            print(f"\nError in audio visualization: {e}")
        finally:
            # Clean up
            if 'stream' in locals():
                stream.stop_stream()
                stream.close()
            p.terminate()
        '''
    
    # Run the terminal visualizer
    terminal_visualizer()


# --------------------------------------------------
# Challenge 4: Interactive Audio Playground
# --------------------------------------------------

def challenge_4():
    '''
    CHALLENGE 4: Interactive Audio Playground
    
    Create an interactive audio playground that lets users experiment
    with sound in real-time.
    
    Requirements:
    1. Implement multiple interactive sound toys/tools
    2. Allow real-time user interaction
    3. Provide clear instructions for users
    
    Ideas for implementation:
    - Musical keyboard using computer keys
    - Beat machine or simple sequencer
    - Voice effect processor
    - Theremin-like instrument using mouse or keyboard
    '''
    print("\nCHALLENGE 4: Interactive Audio Playground")
    print("=======================================")
    print("This challenge is to create an interactive audio playground")
    print("that lets users experiment with sound.")
    print("Be creative - design your own audio toys!")
    
    def audio_playground():
        '''
        TODO: Implement an interactive audio playground
        
        Your implementation should:
        1. Provide multiple ways to interact with audio
        2. Give clear instructions to users
        3. Create an engaging and fun experience
        
        Some ideas:
        - Musical keyboard
        - Simple drum machine
        - Voice transformer
        - Sound patterns creator
        '''
        # Audio parameters
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 16000
        CHUNK = 1024
        
        # TODO: Initialize PyAudio and open stream(s)
        
        # TODO: Create interactive audio toys/tools
        
        # TODO: Implement user interface
        
        print("Audio playground not yet implemented!")
        print("This is an open-ended challenge - be creative!")
        
        '''
        # SOLUTION EXAMPLE (uncomment to see it work)
        # This example implements a simple musical keyboard
        # using computer keys to trigger different tones
        
        # Initialize PyAudio
        p = pyaudio.PyAudio()
        
        try:
            # Set up note frequencies (C major scale)
            notes = {
                'a': 261.63,  # C4
                's': 293.66,  # D4
                'd': 329.63,  # E4
                'f': 349.23,  # F4
                'g': 392.00,  # G4
                'h': 440.00,  # A4
                'j': 493.88,  # B4
                'k': 523.25   # C5
            }
            
            # Open output stream
            stream = p.open(
                format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                output=True,
                frames_per_buffer=CHUNK
            )
            
            print("\nSimple Musical Keyboard")
            print("=====================")
            print("Press keys A S D F G H J K to play notes")
            print("Press 1-4 to change waveform:")
            print("1: Sine, 2: Square, 3: Triangle, 4: Sawtooth")
            print("Press Q to quit")
            
            # Sound generation parameters
            current_note = None
            waveform_type = 1  # 1: sine, 2: square, 3: triangle, 4: sawtooth
            
            def generate_sound(frequency, wave_type):
                """Generate waveform samples for a given frequency and type"""
                samples = []
                for i in range(CHUNK):
                    t = i / RATE  # Time in seconds
                    
                    if wave_type == 1:  # Sine wave
                        sample = math.sin(2 * math.pi * frequency * t)
                    elif wave_type == 2:  # Square wave
                        sample = 1.0 if math.sin(2 * math.pi * frequency * t) > 0 else -1.0
                    elif wave_type == 3:  # Triangle wave
                        sample = 2 * abs(2 * (t * frequency - math.floor(t * frequency + 0.5))) - 1
                    elif wave_type == 4:  # Sawtooth wave
                        sample = 2 * (t * frequency - math.floor(t * frequency + 0.5))
                    else:
                        sample = 0
                    
                    samples.append(sample)
                
                # Convert to int16 format
                int_samples = [int(s * 32767 * 0.3) for s in samples]  # 0.3 to reduce volume
                return struct.pack(f"{CHUNK}h", *int_samples)
            
            # Import the keyboard module for key detection
            try:
                import msvcrt  # Windows
                
                def get_key():
                    if msvcrt.kbhit():
                        return msvcrt.getch().decode('utf-8').lower()
                    return None
                
            except ImportError:
                import termios, fcntl, os, select
                
                def get_key():
                    fd = sys.stdin.fileno()
                    oldterm = termios.tcgetattr(fd)
                    newattr = termios.tcgetattr(fd)
                    newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
                    termios.tcsetattr(fd, termios.TCSANOW, newattr)
                    oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
                    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)
                    try:
                        if select.select([sys.stdin], [], [], 0)[0]:
                            return sys.stdin.read(1)
                        return None
                    finally:
                        termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
                        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
            
            # Main playback loop
            try:
                while True:
                    # Check for key press
                    key = get_key()
                    
                    if key:
                        if key == 'q':
                            raise KeyboardInterrupt  # Exit
                        elif key in notes:
                            current_note = notes[key]
                            print(f"\rPlaying note: {key.upper()} ({current_note:.1f} Hz)", end="")
                        elif key in ['1', '2', '3', '4']:
                            waveform_type = int(key)
                            wave_names = {1: 'Sine', 2: 'Square', 3: 'Triangle', 4: 'Sawtooth'}
                            print(f"\rWaveform: {wave_names[waveform_type]}", end="")
                        else:
                            current_note = None
                    
                    # Generate and play sound
                    if current_note:
                        audio_data = generate_sound(current_note, waveform_type)
                        stream.write(audio_data)
                    else:
                        # Play silence when no key is pressed
                        stream.write(b'\x00' * CHUNK * 2)
                    
                    time.sleep(0.01)
            
            except KeyboardInterrupt:
                print("\n\nKeyboard playback stopped")
        
        except Exception as e:
            print(f"\nError in audio playground: {e}")
        finally:
            # Clean up
            if 'stream' in locals():
                stream.stop_stream()
                stream.close()
            p.terminate()
        '''
    
    # Run the audio playground
    audio_playground()


# --------------------------------------------------
# Challenge 5: Voice Assistant Foundation
# --------------------------------------------------

def challenge_5():
    '''
    CHALLENGE 5: Voice Assistant Foundation
    
    Create the foundation for a voice assistant that activates on a wake word
    and records commands.
    
    Requirements:
    1. Implement wake word detection
    2. Play a sound when the wake word is detected
    3. Record the command that follows
    4. Play a sound when recording ends
    
    Note: This challenge focuses on the audio handling components,
    not on speech recognition or command processing.
    '''
    print("\nCHALLENGE 5: Voice Assistant Foundation")
    print("====================================")
    print("This challenge is to create the foundation for a voice assistant")
    print("that activates when you say a wake word.")
    print("You'll implement the audio handling components, not speech recognition.")
    
    def voice_assistant_foundation():
        '''
        TODO: Implement a voice assistant foundation
        
        Your implementation should:
        1. Listen for a wake word
        2. Play a sound when wake word is detected
        3. Record the command that follows
        4. Play a sound when recording ends
        '''
        # Audio parameters
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 16000
        CHUNK = 1024
        
        # Wake word parameters
        WAKE_WORD = "computer"  # Or another word of your choice
        
        # TODO: Initialize PyAudio
        
        # TODO: Prepare sound effects for feedback
        
        # TODO: Implement wake word detection
        # (This can be simple or advanced depending on your skills)
        
        # TODO: Implement command recording after wake word
        
        print("Voice assistant foundation not yet implemented!")
        
        '''
        # SOLUTION (uncomment to see it work)
        # This is a simplified solution that detects wake words based on 
        # energy patterns rather than actual speech recognition
        
        # Initialize PyAudio
        p = pyaudio.PyAudio()
        
        try:
            # Create notification sounds
            def generate_beep(frequency, duration, falling=False):
                """Generate a simple beep sound"""
                samples = []
                num_samples = int(RATE * duration)
                for i in range(num_samples):
                    t = i / RATE
                    # Apply envelope
                    if falling:
                        amplitude = 1.0 - (i / num_samples)
                    else:
                        amplitude = i / num_samples if i < num_samples / 2 else 2 - (2 * i / num_samples)
                    
                    sample = amplitude * math.sin(2 * math.pi * frequency * t)
                    samples.append(int(sample * 32767 * 0.5))
                
                return struct.pack(f"{num_samples}h", *samples)
            
            # Create notification sounds
            activation_sound = generate_beep(880, 0.15) + generate_beep(1760, 0.15)
            end_sound = generate_beep(1760, 0.1) + generate_beep(880, 0.2, True)
            
            # Open stream for wake word detection
            stream = p.open(
                format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK
            )
            
            print(f"\nVoice Assistant Foundation")
            print(f"Say '{WAKE_WORD}' to activate")
            print("Press Ctrl+C to exit")
            
            # State variables
            listening_for_wake_word = True
            recording_command = False
            command_frames = []
            energy_history = []
            silence_counter = 0
            
            # Wake word detection parameters
            # (This simple approach looks for an energy pattern characteristic of speech)
            ENERGY_THRESHOLD = 1000  # Adjust based on your microphone
            HISTORY_SIZE = 20  # Number of frames to keep in history
            
            # A very basic pattern detector
            # (In a real system, you'd use a proper wake word detection model)
            def detect_wake_pattern(history):
                """
                Extremely simplified wake word 'detection'.
                This doesn't actually detect speech; it just looks for a
                pattern of energy that might indicate someone said something.
                """
                if len(history) < HISTORY_SIZE:
                    return False
                
                # Check for a rising then falling pattern
                rising_trend = all(history[i] < history[i+1] for i in range(5))
                falling_trend = all(history[i] > history[i+1] for i in range(10, 15))
                
                # Check for energy above threshold
                high_energy = max(history) > ENERGY_THRESHOLD
                
                return rising_trend and falling_trend and high_energy
            
            # Main assistant loop
            while True:
                # Read audio
                data = stream.read(CHUNK, exception_on_overflow=False)
                samples = struct.unpack(f"{CHUNK}h", data)
                
                # Calculate energy
                energy = sum(abs(sample) for sample in samples) / CHUNK
                
                # Visual indicator
                if listening_for_wake_word:
                    meter = "*" * int(energy / 200)
                    print(f"\rListening: {energy:.0f} {meter}", end="")
                    
                    # Update energy history
                    energy_history.append(energy)
                    if len(energy_history) > HISTORY_SIZE:
                        energy_history.pop(0)
                    
                    # Check for wake word pattern
                    if detect_wake_pattern(energy_history):
                        print(f"\nWake word detected! Listening for command...")
                        listening_for_wake_word = False
                        recording_command = True
                        command_frames = []
                        silence_counter = 0
                        
                        # Play activation sound
                        output_stream = p.open(
                            format=FORMAT,
                            channels=CHANNELS,
                            rate=RATE,
                            output=True
                        )
                        output_stream.write(activation_sound)
                        output_stream.close()
                
                elif recording_command:
                    # Record the command
                    command_frames.append(data)
                    
                    # Check for silence to end command recording
                    if energy < ENERGY_THRESHOLD * 0.5:
                        silence_counter += 1
                    else:
                        silence_counter = 0
                    
                    # Visual indicator for recording
                    rec_time = len(command_frames) * CHUNK / RATE
                    bars = min(20, int(rec_time * 4))
                    meter = "■" * bars
                    print(f"\rRecording: {rec_time:.1f}s {meter}", end="")
                    
                    # End recording after silence
                    if silence_counter > int(RATE / CHUNK * 1.5):  # 1.5 seconds of silence
                        print("\nCommand recording complete")
                        recording_command = False
                        listening_for_wake_word = True
                        energy_history = []
                        
                        # Play end sound
                        output_stream = p.open(
                            format=FORMAT,
                            channels=CHANNELS,
                            rate=RATE,
                            output=True
                        )
                        output_stream.write(end_sound)
                        output_stream.close()
                        
                        # Save the command
                        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                        command_file = f"command_{timestamp}.wav"
                        
                        with wave.open(command_file, 'wb') as wf:
                            wf.setnchannels(CHANNELS)
                            wf.setsampwidth(p.get_sample_size(FORMAT))
                            wf.setframerate(RATE)
                            wf.writeframes(b''.join(command_frames))
                        
                        print(f"Command saved to {command_file}")
                        print(f"Say '{WAKE_WORD}' to activate")
        
        except KeyboardInterrupt:
            print("\n\nVoice assistant stopped by user")
        except Exception as e:
            print(f"\nError in voice assistant: {e}")
        finally:
            # Clean up
            if 'stream' in locals():
                stream.stop_stream()
                stream.close()
            p.terminate()
        '''
    
    # Run the voice assistant foundation
    voice_assistant_foundation()


# --------------------------------------------------
# MENU
# --------------------------------------------------

def challenges_menu():
    '''
    Display challenges menu
    '''
    print("\nPYAUDIO CHALLENGES")
    print("=================")
    print("1. Voice-Activated Recorder")
    print("2. Audio Format Converter")
    print("3. Terminal Audio Visualizer")
    print("4. Interactive Audio Playground")
    print("5. Voice Assistant Foundation")
    print("6. Return to main menu")
    
    choice = input("\nEnter challenge number (1-6): ")
    
    if choice == "1":
        challenge_1()
        return True
    elif choice == "2":
        challenge_2()
        return True
    elif choice == "3":
        challenge_3()
        return True
    elif choice == "4":
        challenge_4()
        return True
    elif choice == "5":
        challenge_5()
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
    print("\nWelcome to the PyAudio Challenges!")
    print("These challenges will help you apply and extend your PyAudio skills.")
    print("Review the concepts in 06_challenges_concepts.py if needed.")
    
    running = True
    while running:
        running = challenges_menu()
    
    print("\nThank you for practicing PyAudio challenges!")
