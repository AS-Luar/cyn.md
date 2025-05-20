import pyaudio
import wave
import time
import json
import vosk
import soundfile as sf
import numpy as np

start_time = time.time()
p = pyaudio.PyAudio()
model = vosk.Model('/home/luar/AI/voice_assistant/vosk-model-small-en-us-0.15')
recognizer = vosk.KaldiRecognizer(model, 16000)


# Audio parameters
FORMAT = pyaudio.paInt16
CHANs = 1
RATE = 16000
ChNKsz = 1024
Xsec = int(input('Time asshole\n\n'))
 
try:
    # Open input stream
    stream = p.open(
        format=FORMAT,
        channels=CHANs,
        rate=RATE,
        input=True,
        frames_per_buffer=ChNKsz
    )


    print(f"\nRecording for {Xsec} seconds...\n\n")


    # Chunk collector    Total chunks times time
    for i in range(0, int(RATE / ChNKsz * Xsec)):
        data = stream.read(ChNKsz)
        
        accept = recognizer.AcceptWaveform(data)
        if not accept:
            p_result = json.loads(recognizer.PartialResult()).get('partial', '')
            print(f"\r\"{p_result}{''*30}\"", end="", flush=True)

            
    f_result = json.loads(recognizer.FinalResult()).get('text', '')
    print(f"\r\"{f_result}\"{' ' * 20}\n\n\n", end="", flush=True)
    
      
    # print("\nRecording complete!")


    # Clean up
    
finally:
    stream.stop_stream()
    stream.close()
    p.terminate()
#     



#     print("Note: Direct-to-file recording uses less memory but doesn't allow post-processing")