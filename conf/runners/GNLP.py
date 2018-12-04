#!/usr/bin/env python
import sys

import os


print("Start running your script....\n")
os.system("ls")
os.chdir("../../../../SmartApp.GNLP")
os.system("ls")

os.system("python fc.py &")

#for windos
os.system("start /b python fc.py &")

print("Your script is running! ")
