import pyaudio
import wave
import time
p = pyaudio.PyAudio()


# Audio parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 24000
CHUNK = 2048
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "exercise3_direct.wav"



# Set up the WAV file
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
    


# Open input stream
stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=CHUNK
)


print(f"Recording for {RECORD_SECONDS} seconds directly to {WAVE_OUTPUT_FILENAME}...")



# Record audio and write directly to file
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    wf.writeframes(data)
    
    # Show recording progress
    elapsed = i * CHUNK / RATE
    remaining = RECORD_SECONDS - elapsed
    print(f"Recording: {elapsed:.1f}s / {RECORD_SECONDS}s (Remaining: {remaining:.1f}s)", end="\r", flush=True)

print("\nRecording complete!")


    # Clean up
    

stream.stop_stream()
stream.close()
p.terminate()
wf.close()
#     
print(f"Audio saved to {WAVE_OUTPUT_FILENAME}")

#     print("Note: Direct-to-file recording uses less memory but doesn't allow post-processing")