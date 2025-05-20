# Advanced PyAudio: Concepts
'''
This file explains advanced PyAudio concepts including callbacks,
non-blocking streams, real-time processing, audio effects, and robust error handling.

For practical exercises, see 05_advanced_practice.py
'''

import pyaudio
import wave
import time
import sys
import os

# --------------------------------------------------
# SECTION 1: Non-blocking Audio Streams
# --------------------------------------------------

'''
CONCEPT: Non-blocking Audio Streams

In basic PyAudio usage, audio playback and recording operations block the program 
execution until they complete. Non-blocking streams allow your program to continue 
executing other code while audio is playing or recording.

Key concepts:
1. Stream callbacks: Functions called when PyAudio needs more data or has new data
2. Asynchronous processing: Handling audio in the background
3. Stream management: Starting, stopping, and checking stream status

Practice implementing non-blocking audio in Exercise 1 in the practice file.
'''

def explain_non_blocking():
    '''
    Explains the concept of non-blocking audio streams
    '''
    print("\nNon-blocking Audio Streams:")
    print("==========================")
    print("In basic PyAudio usage, audio playback blocks program execution until it finishes.")
    print("Non-blocking streams solve this by using callbacks, allowing your program to")
    print("continue executing other code while audio is processing.")
    
    print("\nKey components:")
    print("1. Stream callback function:")
    print("   - Called automatically when PyAudio needs more data")
    print("   - Returns audio data and a flag (paContinue or paComplete)")
    
    print("\n2. Stream management methods:")
    print("   - start_stream(): Begins non-blocking audio processing")
    print("   - is_active(): Checks if the stream is still processing audio")
    print("   - stop_stream(): Stops a stream (can be restarted)")
    print("   - close(): Closes the stream permanently")
    
    print("\n3. Common applications:")
    print("   - Background music in games")
    print("   - Audio interfaces that remain responsive during playback")
    print("   - Processing other inputs while audio plays")
    
    print("\nTo practice working with non-blocking audio, try Exercise 1 in 05_advanced_practice.py")


# --------------------------------------------------
# SECTION 2: Real-time Processing with Callbacks
# --------------------------------------------------

'''
CONCEPT: Real-time Processing with Callbacks

Audio callbacks are functions that PyAudio calls when it needs audio data 
(for playback) or when it has audio data (from recording). They enable 
real-time audio processing by letting you modify audio data on-the-fly.

Key concepts:
1. Callback function structure and parameters
2. Processing audio data within time constraints
3. Maintaining state between callback invocations

Try implementing real-time audio processing in Exercise 2 in the practice file.
'''

def explain_callbacks():
    '''
    Explains the concept of callback-based audio processing
    '''
    print("\nReal-time Processing with Callbacks:")
    print("==================================")
    print("Callbacks are functions that PyAudio calls automatically during audio processing.")
    print("They allow you to create real-time audio effects and transformations.")
    
    print("\nCallback function structure:")
    print("def callback(in_data, frame_count, time_info, status):")
    print("    # Process audio data here")
    print("    return (output_data, paContinue)")
    
    print("\nCallback parameters:")
    print("- in_data: Raw audio input (bytes)")
    print("- frame_count: Number of frames to process")
    print("- time_info: Dictionary with timing information")
    print("- status: Error/status flags")
    
    print("\nReturn value:")
    print("- Tuple containing (output_data, flag)")
    print("- flag can be pyaudio.paContinue or pyaudio.paComplete")
    
    print("\nCallback processing requirements:")
    print("- Must be fast (complete within the time of one buffer)")
    print("- Should avoid blocking operations (disk I/O, network, etc.)")
    print("- Can use nonlocal/global variables to maintain state")
    
    print("\nTo practice implementing audio callbacks, try Exercise 2 in 05_advanced_practice.py")


# --------------------------------------------------
# SECTION 3: Real-time Audio Effects
# --------------------------------------------------

'''
CONCEPT: Real-time Audio Effects

Audio effects modify sound as it's being processed. With PyAudio callbacks,
you can create real-time effects like echo, distortion, tremolo, and more.

Key concepts:
1. Effect algorithms and parameters
2. Managing effect state (buffers, counters, etc.)
3. Signal processing techniques
4. Performance considerations

Try implementing multiple audio effects in Exercise 3 in the practice file.
'''

def explain_audio_effects():
    '''
    Explains the concept of real-time audio effects
    '''
    print("\nReal-time Audio Effects:")
    print("======================")
    print("Audio effects modify sound characteristics in real-time.")
    print("Using PyAudio callbacks, you can create various effects.")
    
    print("\nCommon real-time audio effects:")
    
    print("\n1. Echo/Delay:")
    print("   - Stores audio in a buffer and mixes delayed samples with current input")
    print("   - Parameters: delay time, feedback/decay amount")
    print("   - Key challenge: Managing the delay buffer")
    
    print("\n2. Distortion:")
    print("   - Alters the waveform by applying non-linear transformations")
    print("   - Parameters: drive/intensity, tone")
    print("   - Common functions: tanh, clipping, waveshaping")
    
    print("\n3. Tremolo/Modulation:")
    print("   - Varies amplitude or other parameters over time using an LFO")
    print("   - Parameters: rate, depth, waveform")
    print("   - Requires tracking phase/time to create cyclic changes")
    
    print("\n4. Filters:")
    print("   - Emphasize or reduce specific frequencies")
    print("   - Types: low-pass, high-pass, band-pass, etc.")
    print("   - Implementation: Simple (averaging) or advanced (biquad/IIR filters)")
    
    print("\nTo practice creating audio effects, try Exercise 3 in 05_advanced_practice.py")


# --------------------------------------------------
# SECTION 4: Advanced Error Handling
# --------------------------------------------------

'''
CONCEPT: Advanced Error Handling

Audio applications need robust error handling to deal with device availability,
configuration issues, runtime errors, and graceful shutdown.

Key concepts:
1. Audio device discovery and selection
2. Error checking and fallback strategies
3. Resource management and cleanup
4. User-friendly error reporting

Practice implementing robust audio applications in Exercise 4 in the practice file.
'''

def explain_error_handling():
    '''
    Explains advanced error handling concepts for audio applications
    '''
    print("\nAdvanced Error Handling:")
    print("======================")
    print("Audio applications require careful error handling to deal with device issues,")
    print("configuration problems, and unexpected situations.")
    
    print("\nKey areas for robust error handling:")
    
    print("\n1. Device Selection:")
    print("   - Enumerate available devices")
    print("   - Check device capabilities (channels, sample rates)")
    print("   - Provide fallbacks when preferred devices aren't available")
    
    print("\n2. Stream Configuration:")
    print("   - Try alternative formats if preferred settings fail")
    print("   - Handle sample rate, bit depth, and channel compatibility issues")
    print("   - Validate settings before attempting to open streams")
    
    print("\n3. Runtime Error Management:")
    print("   - Handle buffer overruns/underruns")
    print("   - Detect and recover from disconnected devices")
    print("   - Use exception handling for audio operations")
    
    print("\n4. Resource Cleanup:")
    print("   - Ensure streams are properly closed")
    print("   - Terminate PyAudio instances")
    print("   - Use try/finally blocks to guarantee cleanup")
    
    print("\nTo practice implementing robust audio applications, try Exercise 4 in 05_advanced_practice.py")


# --------------------------------------------------
# SECTION 5: Advanced Stream Management
# --------------------------------------------------

'''
CONCEPT: Advanced Stream Management

For complex audio applications, you may need to manage multiple streams,
switch between audio devices, or dynamically adjust stream parameters.

Key concepts:
1. Managing multiple simultaneous streams
2. Dynamic stream creation and destruction
3. Stream parameter modification
4. Coordinating timing between streams

Practice advanced stream management in Exercise 5 in the practice file.
'''

def explain_stream_management():
    '''
    Explains advanced stream management concepts
    '''
    print("\nAdvanced Stream Management:")
    print("=========================")
    print("Complex audio applications often require managing multiple streams")
    print("and dynamically adjusting audio configuration.")
    
    print("\nKey stream management concepts:")
    
    print("\n1. Multiple Stream Handling:")
    print("   - Creating separate streams for different audio roles")
    print("   - Managing priorities between competing streams")
    print("   - Synchronizing multiple streams (if needed)")
    
    print("\n2. Dynamic Stream Reconfiguration:")
    print("   - Closing and reopening streams with new parameters")
    print("   - Smoothly transitioning between configurations")
    print("   - Handling configuration changes without audio glitches")
    
    print("\n3. Device Hotplugging:")
    print("   - Detecting when devices connect/disconnect")
    print("   - Gracefully handling device changes")
    print("   - Rebuilding streams when necessary")
    
    print("\n4. Stream States:")
    print("   - Active: Stream is running and processing audio")
    print("   - Stopped: Stream is paused but can be restarted")
    print("   - Closed: Stream is terminated and must be recreated")
    
    print("\nTo practice advanced stream management, try Exercise 5 in 05_advanced_practice.py")


# --------------------------------------------------
# MAIN MENU
# --------------------------------------------------

def show_concepts_menu():
    '''
    Display the main menu for advanced PyAudio concepts
    '''
    print("\nADVANCED PYAUDIO CONCEPTS")
    print("========================")
    print("1. Non-blocking Audio Streams")
    print("2. Real-time Processing with Callbacks")
    print("3. Real-time Audio Effects")
    print("4. Advanced Error Handling")
    print("5. Advanced Stream Management")
    print("6. Go to Practice Exercises (05_advanced_practice.py)")
    print("7. Exit")
    
    choice = input("\nEnter your choice (1-7): ")
    
    if choice == "1":
        explain_non_blocking()
        return True
    elif choice == "2":
        explain_callbacks()
        return True
    elif choice == "3":
        explain_audio_effects()
        return True
    elif choice == "4":
        explain_error_handling()
        return True
    elif choice == "5":
        explain_stream_management()
        return True
    elif choice == "6":
        print("\nNavigate to 05_advanced_practice.py to try the hands-on exercises")
        return True
    elif choice == "7":
        return False
    else:
        print("Invalid choice, please try again.")
        return True


# --------------------------------------------------
# MAIN EXECUTION
# --------------------------------------------------

if __name__ == "__main__":
    print("\nWelcome to the Advanced PyAudio Concepts Module!")
    print("This file explains advanced topics for working with PyAudio.")
    print("For hands-on practice, please open 05_advanced_practice.py after reviewing these concepts.")
    
    running = True
    while running:
        running = show_concepts_menu()
    
    print("\nThank you for exploring advanced PyAudio concepts!")
