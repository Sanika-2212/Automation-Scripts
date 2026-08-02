#Python processSurvillience.py 2 MarvellousLog
#Python processSurvillience.py time_interval MarvellousLog
#               0                   1               2
#len(sys.argv) = 3

import psutil
import sys
import os
import time
import schedule

def PlatformSurvillance(FolderName):
    Border = "-" * 50

    Ret = False

    Ret = os.path.exists(FolderName)

    if(Ret == True):
        Ret = os.path.isdir(FolderName)
        if(Ret == False):
            print("Unable to proceed as directory name is existing but is not a directory")

    else:
        os.mkdir(FolderName)
        print("Directory for the Log File gets created successfully...")

    timestamp =time.strftime("%Y-%m-%d_%H-%M-%S")

    FileName = os.path.join(FolderName, "Marvellous_%s.log"%timestamp)

    fobj = open(FileName,"w")

    print(f"Log File Gets Successfully created with name{FileName}")

    fobj.write(Border + "\n")
    fobj.write("----Marvellous Platform Survillience System----\n")
    fobj.write("Log File gets created at:"+ timestamp +"\n")
    fobj.write(Border + "\n")

    fobj.write("----System Report----\n")
    fobj.write("\n\n\n\n\n\n\n\n\n\n")

    fobj.write(Border + "\n")
    fobj.write("----End of Log File----\n")
    fobj.write(Border + "\n")

    fobj.close()

def main():
    Border = "-" * 50
    print(Border)
    print("----Marvellous Platform Survillience System----")
    print(Border)

    # --h & --u handling
    if(len(sys.argv)== 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This Automation Script is used to perform:-")
            print("1: It fetches the information of running processes")
            print("2. It fetches the information about the primary storage as RAM")
            print("3. It fetches the information about the secondary storage as HDD")
            print("4. It fetches the information about the microprocessor")
            print("5. It gets auto scheduled periodically")
            print("6. It maintains all records into log file")
            print("7. It send the log files through mail periodically")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the Automation Scripts as :")
            print(f"python{sys.argv[0]} Time_Interval_ Folder_Name")
            print("Time_Interval : Time in Minutes for periodic execution")
            print("Folder_Name : Name of Folder for the log file creation")

        else:
            print("Unable to proceed as there is not matching arguments...")
            print("Please use --h or --u flag for getting more details")

    #Actual project code
    elif(len(sys.argv) == 3):
        print("Scheduler Started Successfully")
        print("Press Ctrl + C to abort the automation script...")
        schedule.every(int(sys.argv[1])).minutes.do(PlatformSurvillance,sys.argv[2])

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid Number of Arguments")
        print("Unable to proceed as arguments are not matching")
        print("Please use --h or --u flag for getting more details")

    print(Border)
    print("----Thank you for using our Automatin System----")
    print(Border)

if __name__ == "__main__":
    main()