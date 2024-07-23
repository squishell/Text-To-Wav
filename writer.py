# Auto Voice Writer
# Mitchel Anderson
# 2021

import tts.sapi
import os
import time
import sys
#Import Required Dependencies

voice = tts.sapi.Sapi()
voice.set_voice("Heather")
voice.set_rate(0)
#Set Voice for Project /// Default Heather

ffmpeg_executable = "C:/Program Files (x86)/FFmpeg for Audacity/ffmpeg.exe"
#Locate ffmpeg executable


current_directory = os.getcwd()
print("directory name?")
# User Names New Directory

new_directory = input()
final_directory = os.path.join(current_directory,new_directory)
if not os.path.exists(final_directory):
    os.makedirs(final_directory)
# Makes the Directory

droppedFile = sys.argv[1]

os.chdir(final_directory)

linecount = 1
with open(droppedFile, "r") as a_file:
  for line in a_file:
    phrase = line.strip()
    print("Current Line: " + str(linecount))
    print("Working on: " + phrase)
    file = str(os.getcwd()) + "/" + str(linecount) + ".wav"
    voice.create_recording(file, phrase)
    linecount += 1
    time.sleep(2)
# Iterates through the file to parse each line

print("All Done")
wait = input()

# Pauses to show finished