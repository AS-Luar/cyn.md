import pyaudio
import soundfile
import time
# Initialize PyAudio
p = pyaudio.PyAudio()

print('\n\n\n----------------------------------------------------\n')

# List available audio input devices
print("Available audio input devices:")
for i in range(p.get_device_count()):
    info = p.get_device_info_by_index(i)
    sample_rate = info.get('defaultSampleRate', 'Unknown')
    if info['maxInputChannels'] > 0:
        max = info['maxInputChannels']
        print(f"  [{i}] {info['name']} |{sample_rate}Hz| ({max})Ch\n")
print('----------------------------------------------------\n')

# Audio parameters
FORMAT = pyaudio.paInt16 #bits
CHANNELS = 1
RATE = 16000
CHUNK = 1024
index =int(input("Pick index (asshole)\n\n"))
RECORD_SECONDS = int(input('How long do you want to record? (seconds)\n\n'))
WAVE_OUTPUT_FILENAME = "/home/luar/AI/voice_assistant/Branch/recordings/"+input("filename asshole \n\n")+".wav"


try:
    # Open input stream
    stream = p.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        input_device_index= index,
        frames_per_buffer=CHUNK
    )
    
    print(f"Recording for {RECORD_SECONDS} seconds...\n--------------------------")
    
    # Record audio in chunks
    frames = []  # This list will store all audio chunks
    
    # Calculate how many chunks to read based on duration
    total_chunks = int(RATE / CHUNK * RECORD_SECONDS)
    
    for i in range(total_chunks):
        
        data = stream.read(CHUNK) # Read one chunk of audio data (returns bytes)
        
        
        
        frames.append(data) # Store the chunk in our list
        
        
        
        
        
        # Calculate audio level for visual feedback
        if i % 10 == 0:
            # Convert bytes to samples for level calculation
            samples = [int.from_bytes(data[j:j+2], byteorder='little', signed=True) for j in range(0, len(data), 2)]
            if samples:  # Ensure we have samples
                level = min(40, int(sum(abs(s) for s in samples) / len(samples) / 328))  # Simple level calculation
                print(f"\rLevel: {'|' * level}{' ' * (40-level)} {level/40*100:3.0f}%", end="", flush=True)
    
    print("\n\nRecording complete!\n\n")
    
finally:
    # Proper cleanup (always executed, even if errors occur)
    if 'stream' in locals():
        # Stop and close the stream
        stream.stop_stream()
        stream.close()
    
    # Terminate PyAudio
    p.terminate()






# Save the recorded audio to WAV file
print("Saving recording to WAV file...")

# Open WAV file for writing binary data
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')

# Set WAV file parameters
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)

# Join all audio chunks and write to file
wf.writeframes(b''.join(frames))

# Close the file (important cleanup step)
wf.close()

print(f"Audio saved to {WAVE_OUTPUT_FILENAME}")