# 1. Import any required modules (e.g., time, vosk, wave, json)
# 2. Start timing the processing
# 3. Set up the model path and load the Vosk model
# 4. Open your audio file (WAV format)
# 5. Create a recognizer using the model and audio sample rate

import time
import wave
import json
import vosk
import os

vmod = vosk.Model
vrec = vosk.KaldiRecognizer
# text = "" I am only looking for the json
model = vmod('/home/luar/AI/voice_assistant/vosk-model-small-en-us-0.15') 
wavfile = wave.open('/home/luar/AI/voice_assistant/Branch/recordings/test.wav', 'rb')
recognizer = vrec(model, wavfile.getframerate())

start_time = time.time()

# 6. Process the audio in chunks and collect recognized text


print("\n\n\n\n\n")
while 1:
    binary = wavfile.readframes(4000)
    if len(binary) == 0:
        break
    
    accepted = recognizer.AcceptWaveform(binary)
    if accepted:
        result = json.loads(recognizer.Result())
        #print('\n'+result)
    else:
        partial_result = json.loads(recognizer.PartialResult())
        #print('\r'+partial_result.get('partial', ''), end="", flush=True)


print('\n')

# 7. Get the final recognition result and append to text

# 8. Print the recognized text

# 9. Stop timing and print the total processing time
end_time = time.time()
print(f"Processing time: {end_time - start_time:.2f} seconds")