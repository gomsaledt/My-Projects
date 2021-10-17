#!/usr/bin/python3

# ------------------------ A program to change text to audio ---------------------------

import pyttsx3

engine = pyttsx3.init()
engine.say("Hello")
engine.runAndWait()