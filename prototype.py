import datetime
import time
import os                     #used for interacting with directory



#functions

def timeconverter():                                  #timeconverter function

    global time                                       #declare it as a global variable, if not local variable error
    a = input("press a to continue, x to exit: \n")

    if a == 'a':
        timestamp_bag = float(input("\nInsert the timestamp you wanna convert: "))
            
    
        #epoch_time = timestamp_bag
        
        
        date_time = datetime.datetime.fromtimestamp( timestamp_bag )  
        
    
        print("Given rosbag timestamp: ", timestamp_bag)  
        print("Converted Datetime: ", date_time )  
        

        time = date_time.time()

        hour = time.hour
        print("Hour : {}".format(hour))
        
        minute = time.minute
        print("Minute : {}".format(minute))

        


        when = date_time.date()

        year = when.year
        print("Year : {}".format(year))

        month = when.month
        print("Month : {}".format(month))

        day = when.day
        print("Day : {}".format(day))


        print(hour)
        print(minute)
        
    

        #if (minute > 32):
        #    print("choose bagfile with 9:32 ")

        
        #keyword = input("what bag files you wanna find?\n")
        
        find_hr = str(hour)
        find_year = str(year)
        find_month = str(month)
        find_day  = str(day)
        find_min = str(minute)
        print(find_year + "-" + find_month + "-" + find_day + "-" + find_hr)
        print(find_year + "-" + "0" + find_month + "-" + "0" + find_day + "-" + "0" + find_hr)

        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")

        for fname in os.listdir('/home/kitwei/Desktop/rosbag-project2'):
        #if '.bag' and find_year and find_month and find_day in fname:
        #if find_year + "-" + find_month + "-" + find_day + "-" + find_hr and '.bag' in fname or find_year + "-" + "0" + find_month + "-" + "0" + find_day + "-" + "0" + find_hr and '.bag' in fname :
        #if date_time in fname:
        #if fname[14] == 9 in fname:
            if ".bag" in fname:
                #if fname[14] == 9:
                #print(fname, "has the keyword")
                #print(fname)
                #print(fname)

                #if fname[20]==find_hr or fname[19]==find_hr:
                if fname[20]=="9" or fname[19]=="9":
                    given_minute = int(fname[22] + fname[23])
                    choose_minute = int(find_min)
                    if given_minute < choose_minute:
                        print(fname)
                        


                    
        

    elif a == 'x':
        print("exciting .......................")
        time.sleep(0.2)
        print("exciting  .....................")
        time.sleep(0.2)
        print("exciting   ...................")
        time.sleep(0.2)
        print("exciting    .................")
        time.sleep(0.2)
        print("exciting     ...............")
        time.sleep(0.2)
        print("exciting      .............")
        time.sleep(0.2)
        print("exciting       ...........")
        time.sleep(0.2)
        print("exciting        .........")
        time.sleep(0.2)
        print("exciting         .......")
        time.sleep(0.2)
        print("exciting          .....")
        time.sleep(0.2)
        print("exciting           ...")
        time.sleep(0.2)
        print("exciting            .")
        time.sleep(0.2)
     

    else:
        print("error")


#code starts here

choose_file = input("What file do you wanna use? \n")
#choose_file, keyword= input("What file do you wanna use? Enter the keyword you wanna find! \n").split()

full_dir = "/home/kitwei/Desktop/rosbag-project2/" + choose_file


x = open(full_dir,"r")      #set it to a variable ######
 
keyword = input("Enter keyword: ")
#keyword = input("Enter keyword: ")



for line in x:                                   #search line by line
    if keyword in line:
        print(line)




timeconverter()



x.close()

print("")
print("")
print("end")







    