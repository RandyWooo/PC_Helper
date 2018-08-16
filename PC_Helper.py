import os
import psutil
import sys
import shutil

print("Hi!")
name = input("Your name is: ")

print(name, ", hello.")

answer = ''
while answer != 'Q':
    answer = input("go work, bitch (Y/N/Q)")
    if answer == 'Y': 
        print("profit")
        print("I can:")
        print(" [1] - information list")
        print(" [2] - information about system")
        print(" [3] - list of PIDs")
        print(" [4] - duplicate files in current directory")
        do = int(input("number of action: "))
        
        if do  == 1:
            print(os.listdir())
        elif do == 2:
            print("What i know about system:")
            print("Count of CPU: ", psutil.cpu_count())
            print("Platform: ", sys.platform)
            print("Encoding FS: ", sys.getfilesystemencoding())
            print("Current directory: ", os.getcwd())
            print("Current user: ", os.getlogin())
        elif do == 3:
            print(psutil.pids())   
        elif do == 4:
            print("Duplicate files in current directory")
            file_list = os.listdir()
            i = 0
            while i < len(file_list):
                newfile = file_list[i] + '.dupl'
                shutil.copy(file_list[i], newfile)
                i += 1
        else:
            pass
    elif answer == 'N':
        print("goodbye")
    else:
        print("don't worry, BRO")
