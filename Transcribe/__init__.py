"""
Program Name: transcribe.py
Program Purpose: To transcribe the video footage from Dr.Heldman's class
Programmer: Ruby Goodpasture
Date: 2/27/2024
"""
import speech_recognition as sr
import os
from moviepy.editor import *


def mp4towav(mp4file,wavfile):
    videoclip=VideoFileClip(mp4file)
    audioclip=videoclip.audio
    audioclip.write_audiofile(wavfile)
    audioclip.close()
    videoclip.close()
 


def audio (fileIn):
    AUDIO_FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)), fileIn)
    # use the audio file as the audio source
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file

    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        trans = r.recognize_google(audio)
        print("Google Speech Recognition thinks you said " + trans)
        return(trans)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def fileOut(trans,name):
    pathOut = f'TranscribeOut/{name}.txt'
    fileOut = os.open(pathOut, os.O_RDWR | os.O_CREAT )

    os.write(fileOut, str.encode(trans))

    os.close(fileOut)

file = "happyhalloween"
fileIn = f'testfiles/{file}.mp4'
audioOut = f'audio/{file}.wav'

mp4towav(fileIn,audioOut)
trans = audio(audioOut)
fileOut(trans,file)
