import pyaudio
import time
import json
import vosk
import keyboard as kb



# def record():

p = pyaudio.PyAudio()
model = vosk.Model('/home/luar/Projects/AI/voice_assistant/vosk-model-small-en-us-0.15')
recognizer = vosk.KaldiRecognizer(model, 16000)
key=140


default_index = p.get_default_input_device_info()['index']
default_info = p.get_device_info_by_index(default_index)
print(default_info)

# 音 parameters
Fmt = pyaudio.paInt16 
Чnl = 1
Rt = RATE = int(default_info['defaultSampleRate'])
Чnk寸 = 1024

input('aight, u ready? (hold calc moron)')
stream = None

try:
    print('starting stream')
    # Open input stream
    stream = p.open(
        format=Fmt,
        channels=Чnl,
        rate=Rt,
        input=True,
        frames_per_buffer=Чnk寸
    )



    while 1:
        data = stream.read(Чnk寸)
        recognizer.AcceptWaveform(data)
        print('calcking')
        if not kb.is_pressed(key):
            break
        
        
            
            

            
    f_result = json.loads(recognizer.FinalResult()).get('text', '')

    print(f"{f_result}")
    
    
    # print("\nRecording complete!")


    # Clean up
    
finally:
    if stream:
        print("chora")
    if stream is not None:
        stream.stop_stream()
        stream.close()
    p.terminate()
#     



#     print("Note: Direct-to-file recording uses less memory but doesn't allow post-processing")