#Python processSurvillience.py 2 MarvellousLog
#Python processSurvillience.py time_interval MarvellousLog
#               0                   1               2
#len(sys.argv) = 3

import psutil
import sys
import os

def main():
    Border = "-" * 50
    print(Border)
    print("----Marvellous Platform Survillience system----")
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
        pass

    else:
        print("Invalid Number of Arguments")
        print("Unable to proceed as arguments are not matching")
        print("Please use --h or --u flag for getting more details")

    print(Border)
    print("----Thank you for using our Automatin System----")
    print(Border)

if __name__ == "__main__":
    main()