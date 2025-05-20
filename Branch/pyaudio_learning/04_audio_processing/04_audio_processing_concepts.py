# Audio Processing with PyAudio - Concepts
'''
This file explains core concepts for processing audio data using PyAudio.
These concepts include understanding raw audio data, applying transformations,
and implementing real-time audio processing techniques.

For practical exercises, see 04_audio_processing_practice.py
'''

import pyaudio
import wave
import os
import struct
import time

# --------------------------------------------------
# SECTION 1: Understanding Audio Data
# --------------------------------------------------

'''
CONCEPT: Digital Audio Representation

Audio in computer systems is represented as a series of samples.
Each sample is a numeric value representing the amplitude of the sound wave
at a specific point in time.

Key properties of digital audio:
1. Sample Rate: Number of samples per second (e.g., 44100 Hz)
2. Sample Width/Bit Depth: Number of bits per sample (e.g., 16-bit)
3. Channels: Number of audio channels (1 for mono, 2 for stereo)

See Exercise 1 in the practice file to explore audio data.
'''

def explain_audio_data():
    '''
    Explains how audio is stored digitally and the meaning of different properties.
    '''
    print("\nDigital Audio Fundamentals:")
    print("--------------------------")
    print("1. Sample Rate (e.g., 44100 Hz)")
    print("   - Number of samples captured per second")
    print("   - Higher rates capture higher frequencies")
    print("   - Common rates: 8000 Hz (telephone), 44100 Hz (CD), 48000 Hz (professional)")
    
    print("\n2. Sample Width/Bit Depth (e.g., 16-bit)")
    print("   - Number of bits used to represent each sample")
    print("   - Determines dynamic range (quietest to loudest sounds)")
    print("   - Common widths: 8-bit (0-255), 16-bit (-32768 to 32767), 32-bit (floating point)")
    
    print("\n3. Channels")
    print("   - Number of simultaneous audio streams")
    print("   - 1 = mono, 2 = stereo, >2 = multi-channel audio")
    
    print("\nTo understand audio data structure in practice, try Exercise 1 in 04_audio_processing_practice.py")


# --------------------------------------------------
# SECTION 2: Basic Audio Transformations
# --------------------------------------------------

'''
CONCEPT: Audio Transformations

Audio transformations involve modifying the digital audio data to create 
different effects or convert between formats. Common transformations include:

1. Volume Adjustment: Multiplying sample values to change amplitude
2. Speed/Pitch Change: Changing playback rate or resampling
3. Channel Conversion: Converting between mono and stereo
4. Format Conversion: Changing bit depth or sample rate

Practice these transformations in Exercise 2 in the practice file.
'''

def explain_audio_transformations():
    '''
    Explains common types of audio transformations and how they work
    '''
    print("\nAudio Transformation Concepts:")
    print("-----------------------------")
    print("1. Volume Adjustment")
    print("   - Multiply each sample by a factor")
    print("   - Factors > 1 increase volume, < 1 decrease volume")
    print("   - Must prevent clipping by limiting maximum values")
    
    print("\n2. Speed/Pitch Change")
    print("   - Simple approach: Change sample rate during playback")
    print("   - This changes both speed AND pitch together")
    print("   - Professional time-stretching separates speed from pitch")
    
    print("\n3. Channel Conversion")
    print("   - Mono to Stereo: Duplicate samples to both channels")
    print("   - Stereo to Mono: Average samples from both channels")
    
    print("\n4. Format Conversion")
    print("   - Sample Rate: Resample audio (interpolation)")
    print("   - Bit Depth: Rescale values to new range")
    
    print("\nTo practice implementing these transformations, try Exercise 2 in 04_audio_processing_practice.py")


# --------------------------------------------------
# SECTION 3: Real-time Voice Detection
# --------------------------------------------------

'''
CONCEPT: Voice Activity Detection

Voice Activity Detection (VAD) is the process of determining when 
someone is speaking in an audio stream.

Basic approaches:
1. Energy-based detection: Compare audio energy to a threshold
2. Zero-crossing rate: Frequency of signal crossing the zero level
3. Machine learning approaches: More sophisticated pattern recognition

This is fundamental for applications like voice assistants, speech recognition,
and audio filtering.

Try implementing a simple voice detector in Exercise 3 in the practice file.
'''

def explain_voice_detection():
    '''
    Explains the concept of voice activity detection
    '''
    print("\nVoice Activity Detection (VAD) Concepts:")
    print("--------------------------------------")
    print("Voice detection is about detecting when someone is speaking vs. silence or noise.")
    
    print("\nApproaches to Voice Detection:")
    print("1. Energy-based Detection")
    print("   - Calculate energy/amplitude of audio signal")
    print("   - Compare to a threshold value")
    print("   - Simple but affected by background noise")
    
    print("\n2. Zero-crossing Rate")
    print("   - Count how often the signal crosses the zero amplitude line")
    print("   - Speech has different patterns than noise")
    print("   - Can be combined with energy for better accuracy")
    
    print("\n3. Advanced Methods")
    print("   - Frequency analysis (speech has specific frequency patterns)")
    print("   - Machine learning models trained on speech data")
    print("   - Commercial systems like WebRTC VAD or cloud-based services")
    
    print("\nTo implement a simple voice detector, try Exercise 3 in 04_audio_processing_practice.py")


# --------------------------------------------------
# SECTION 4: Signal Processing Concepts
# --------------------------------------------------

'''
CONCEPT: Digital Signal Processing Basics

Digital Signal Processing (DSP) is a field that focuses on the analysis and 
manipulation of signals, such as audio signals. Core concepts include:

1. Filters: Removing or emphasizing certain frequencies
2. Frequency Analysis: Breaking down a signal into its frequencies
3. Effects: Reverb, echo, distortion, etc.

For audio applications, DSP allows us to clean up recordings, create effects,
analyze sound properties, and more.

Try implementing basic DSP in Exercise 4 in the practice file.
'''

def explain_signal_processing():
    '''
    Introduces basic concepts of digital signal processing for audio
    '''
    print("\nDigital Signal Processing (DSP) Concepts:")
    print("---------------------------------------")
    print("DSP allows us to analyze and manipulate audio signals.")
    
    print("\nCore DSP Concepts for Audio:")
    print("1. Filters")
    print("   - Low-pass: Allow low frequencies, reduce high frequencies (makes sound muffled)")
    print("   - High-pass: Allow high frequencies, reduce low frequencies (removes rumble)")
    print("   - Band-pass: Allow a specific range of frequencies")
    
    print("\n2. Frequency Analysis")
    print("   - Fast Fourier Transform (FFT): Convert time-domain to frequency-domain")
    print("   - Identifies which frequencies are present and their amplitudes")
    print("   - Used for visualizations (spectrograms) and advanced processing")
    
    print("\n3. Audio Effects")
    print("   - Echo/Delay: Mixing delayed copies of the signal")
    print("   - Reverb: Simulating sound reflections in a space")
    print("   - Distortion: Deliberately altering the signal to add harmonics")
    
    print("\nTo implement basic audio effects, try Exercise 4 in 04_audio_processing_practice.py")


# --------------------------------------------------
# MAIN MENU
# --------------------------------------------------

def show_concepts_menu():
    '''
    Display the main menu for audio processing concepts
    '''
    print("\nAUDIO PROCESSING CONCEPTS")
    print("=======================")
    print("1. Digital Audio Representation")
    print("2. Audio Transformations")
    print("3. Voice Activity Detection")
    print("4. Signal Processing Concepts")
    print("5. Go to Practice Exercises (04_audio_processing_practice.py)")
    print("6. Exit")
    
    choice = input("\nEnter your choice (1-6): ")
    
    if choice == "1":
        explain_audio_data()
        return True
    elif choice == "2":
        explain_audio_transformations()
        return True
    elif choice == "3":
        explain_voice_detection()
        return True
    elif choice == "4":
        explain_signal_processing()
        return True
    elif choice == "5":
        print("\nNavigate to 04_audio_processing_practice.py to try the hands-on exercises")
        return True
    elif choice == "6":
        return False
    else:
        print("Invalid choice, please try again.")
        return True


# --------------------------------------------------
# MAIN EXECUTION
# --------------------------------------------------

if __name__ == "__main__":
    print("\nWelcome to the Audio Processing Concepts Module!")
    print("This file explains key concepts related to audio processing with PyAudio.")
    print("For hands-on practice, please open 04_audio_processing_practice.py after reviewing these concepts.")
    
    running = True
    while running:
        running = show_concepts_menu()
    
    print("\nThank you for exploring audio processing concepts!")
