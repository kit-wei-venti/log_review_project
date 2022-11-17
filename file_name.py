import os
import glob

keyword = "event_log"
list_file = []

directory = os.getcwd()
#print(directory) 

list_file = os.listdir(directory)
#print(list_file)

for filename in list_file:
    if keyword in filename:
        print(filename)