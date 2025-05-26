import pyaudio
import time
import json
import vosk


start_time = time.time()
p = pyaudio.PyAudio()
model = vosk.Model('/home/luar/AI/voice_assistant/vosk-model-small-en-us-0.15')
recognizer = vosk.KaldiRecognizer(model, 16000)


# 音 parameters
Fmt = pyaudio.paInt16 
Чnl = 1
Rt = 16000
Чnk寸 = 1024
秒 = int(input('Time asshole\n\n'))
 
try:
    # Open input stream
    stream = p.open(
        format=Fmt,
        channels=Чnl,
        rate=Rt,
        input=True,
        frames_per_buffer=Чnk寸
    )


    print(f"\nRecording for {秒} seconds...\n\n")


    # Chunk collector    Total chunks times time
    for i in range(0, int(Rt / Чnk寸 * 秒)):
        data = stream.read(Чnk寸)
        
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