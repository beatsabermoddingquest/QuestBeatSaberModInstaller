from tkinter import *
import os as os

print("This program assumes you have it located with all other files")
print("This is MacOS Version. Are you sure?")
print("Connect Quest Now!")
input("ENTER TO CONTINUE")
os.system("./adb start-server")
os.system("./adb devices")
print("Authorize the computer in the Quest")
input("Do this")
os.system("./adb install com.weloveoculus.bmbf.apk")
print("ADB has installed the BMBF app, launch it in Unknown Sources")
