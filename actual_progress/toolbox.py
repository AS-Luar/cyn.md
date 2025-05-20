import librosa as lb
import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt
import pyaudio

#-------------------------------------------------------------------

#LIST INPUTS:
def list_input(p):
    print("Available audio input devices:")
    for i in range(p.get_device_count()):
        info = p.get_device_info_by_index(i)
        sample_rate = info.get('defaultSampleRate', 'Unknown')
        if info['maxInputChannels'] > 0:
            max = info['maxInputChannels']
            print(f"  [{i}] {info['name']} |{sample_rate}Hz| ({max})Ch\n")

#-------------------------------------------------------------------

#RESAMPLER:
def resample_audio(file_path, output_path):
 
    target_sr = input("\nWhat's the target rate?\n")
    file_name = input("\nNew file name?\n")
    

    numpaudio, original_sr = numpinator(file_path)

    # Resample to target sample rate if different
    
    if original_sr != target_sr:
        resampled_data = lb.resample(numpaudio, original_sr, target_sr)
        print(f"\nResampled from {original_sr}Hz to {target_sr}Hz\n")
    else:
        resampled_data = numpaudio
        print(f"Audio is already at {target_sr}Hz")

    sf.write(output_path+str(file_name+'.wav'), resampled_data, target_sr)

    print("\n\n LOLMAO")
    
#-------------------------------------------------------------------

#NUMP-INATOR:

def numpinator(file_path):
    numpaudio, original_sr = lb.load(file_path, sr=None)
    return numpaudio, original_sr

#-------------------------------------------------------------------

# NORMALIZER
def norm_音(numpaudio):
    target_dB = -3
    
    max_amp = np.max(np.abs(numpaudio))
    print(f"Maximum amplitude before normalization: {max_amp}")

    # Convert the peak amplitude to decibels (dB)
    current_dB = 20 * np.log10(max_amp) if max_amp > 0 else -80
    print(f"\nCurrent peak dB: {current_dB:.2f}\n")

    # Calculate the gain needed to reach the target dB
    gain_dB = target_dB - current_dB
    gain_amp = 10 ** (gain_dB / 20)
    print(f"\nApplying gain (linear): {gain_amp}\n")

    # Apply the gain to the audio
    norm_audio = numpaudio * gain_amp

    # Ensure the audio does not exceed the range [-1, 1] (to avoid distortion)
    if np.max(np.abs(norm_audio)) > 1.0:
        norm_audio = norm_audio / np.max(np.abs(norm_audio))
        print("Audio was clipped; scaled down to fit [-1, 1]")

    print(f"\nFrom {current_dB:.2f}dB to {target_dB:.2f}dB\n")
    
    return norm_audio

#-------------------------------------------------------------------

