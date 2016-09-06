import sys
import wave #wave module: read & wrtie wave files #WAV files: most basic sound file. uncompressed

def getAudioData(WAV_file):
    openFile = wave.open(WAV_file,'r')

    samplingFrequency = openFile.getframerate()
    #print(samplingFrequency)#44100 HZ(number of samples per second ): this is a commonly used value
    
    #Frame(sample): how loud the sound is at a point. (many frames are played to create sound)
    audioData = openFile.readframes(-1)#Reads and returns at most n frames of audio, as a string of bytes
    #print(audioData) #uncomprehensible data (need to convert)
    audioData_int = map(ord, list(audioData))#convert to readable data(in int)
    #print(audioData_int)

    openFile.close()
    return audioData_int

def createNewAudio(original, audioDataArray):
	"""
	newAudioArray=[]
	for i in audioDataArray:
		if i !=0:
			i=i+1
		newAudioArray.append(i)
	#print(newAudioArray)
	"""

	newSound_outputFile=wave.open('output.wav','w')
	originalFile=wave.open(original,'r')
	nchannels, sampwidth, framerate, nframes, comptype, compname =  originalFile.getparams()
	newSound_outputFile.setparams((2,sampwidth,framerate,nframes,comptype,compname))

	for i in audioDataArray:
		newSound_outputFile.writeframes(str(i))

	newSound_outputFile.close()

#Run Program Here
WAV_file = sys.argv[1]
audioDataArray = getAudioData(WAV_file)
createNewAudio(WAV_file, audioDataArray)

#Debug - take a loot at readframes() or writeframes()
check = getAudioData('output.wav')
print check

#terminal: python m.py 1.wav