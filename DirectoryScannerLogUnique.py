import sys
import os
import time

def DirectoryScanner(DirectoryPath):

    timestamp = time.ctime()        #To Create Unique Files
    
    LogFileName = "Marvellous%s.log"%(timestamp)

    LogFileName = LogFileName.replace(" ","_")
    LogFileName = LogFileName.replace(":","_")  

    print("Log File Gets Created With Name: ",LogFileName)

    fobj = open(LogFileName,"w")

    fobj.write("Marvellous Automation Script\n")
    
    fobj.write("Files from the directory are:\n")

    for FolderName, SubFolder, FileName in os.walk(DirectoryPath):
        for fname in FileName:
            fobj.write(fname+"\n")

    fobj.close()

def main():

    Border = "-"*40
    print(Border)
    print("Marvellous Automation Script")
    print(Border)

    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This Automation Script is used to travel the directory.")
            print("For Better Usage please check --u flag...")
        
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Please Execute the script as ")
            print("Python FileName.py DirectoryName")
            print("Directory name should be absolute path...")

        else:
            DirectoryScanner(sys.argv[1])

    else:
        print("Invalid Number of Arguments")
        print("Please use --h or --u for more information...")

    print(Border)
    print("Thank You For Using Marvellous Automation Script")
    print(Border)

    
if __name__ == "__main__":
    main()