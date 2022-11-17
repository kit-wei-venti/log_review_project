import os 
import glob


keyword = "event_log"
list_file = " "


directory = os.getcwd()
#print(directory) 

list_file = os.listdir(directory)
#print(list_file)

for filename in list_file:
    if keyword in filename:
        #print(filename)                          #filename is in string
        full_directory = directory + "/" + filename
        #print(full_directory)
        open_file = open(full_directory,"r")
        for line in open_file:
            split_space = line.split(" ")
            print(split_space)