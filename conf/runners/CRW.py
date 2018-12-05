#!/usr/bin/env python
import sys

import os


print("Start running your script....\n")
os.system("ls")
os.chdir("../../../../SmartApp.CRW")
os.system("ls")

os.system("git pull")

print("Your script is running! ")
