from operator import truediv
import time,os,shutil

def clearFiles() :

    path = input("enter the folder with files :- ")
    pathExists =os.path.exists(path)
    print(pathExists)

    print("please enter the date from which the older files will be deleted :- ")
    day = int(input("Day :- "))
    month = int(input("month :- "))
    year = int(input("year :- "))
    numD = (year, month, day,0, 0, 0,  3, 361, 10)

    # returns seconds from struct_time
    s = time.mktime(numD)
    print("\s:", s)

    #print(numD.tm_mday)

    if pathExists == True :
        files = os.listdir(path)
        for file in files :
            filepath =os.path.join(path,file)
            filestatus = os.stat(filepath)
         #   print(filestatus.st_ctime)
            if(filestatus.st_ctime>s):
                os.remove(filepath)
                print("file removed")
            else:
                print("file saved")
                continue
    else :
        print("please re-check the path")
clearFiles()