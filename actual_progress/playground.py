import toolbox as tb
import soundfile as sf

path = '/home/luar/AI/voice_assistant/Branch/recordings/'
filename = input("\nfilename asshole \n")
new_filename = input("\nnew filename asshole \n\n") 

numpaudio, sample_rate = tb.numpinator(path+filename+'.wav')

normalized_audio = tb.norm_音(numpaudio)

sf.write(path+new_filename+'.wav', normalized_audio, sample_rate)