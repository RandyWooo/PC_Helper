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
        print(" [5] - duplicate specified file")
        print(" [6] - delete duplicate files")
        
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
                if os.path.isfile(file_list[i]):
                    newfile = file_list[i] + '.dupl'
                    shutil.copy(file_list[i], newfile)
                i += 1
        elif do == 5:
             print("duplicate specified file: ")
             filename = input("Write file name: ")
             if os.path.isfile(filename):
                    newfile = filename + '.dupl'
                    shutil.copy(filename, newfile)           
        
        elif do == 6:
             print("delete duplicate files: ")
             dirname = input("Write directory name: ")
             file_list = os.listdir(dirname)
             i = 0
             while i < len(file_list):
                 fullname = os.path.join(dirname, file_list[i])
                 if fullname.endswith('.dupl'):
                     os.remove(fullname)
                 i += 1    
        else:
            pass
    elif answer == 'N':
        print("goodbye")
    else:
        print("don't worry, BRO")
