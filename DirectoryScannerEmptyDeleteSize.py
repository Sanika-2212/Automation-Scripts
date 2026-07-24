import sys
import os
import time
import schedule

def DirectoryScanner(DirectoryPath = "Marvellous"):

    Border = "-"*50

    timestamp = time.ctime()        #To Create Unique Files
    
    LogFileName = "Marvellous%s.log"%(timestamp)

    LogFileName = LogFileName.replace(" ","_")
    LogFileName = LogFileName.replace(":","_")  

    Ret = False

    Ret = os.path.exists(DirectoryPath)

    if(Ret == False):
        print("Marvellous Automation Error: There is No such Directory with Name",DirectoryPath)
        return
    
    Ret = os.path.isdir(DirectoryPath)

    if(Ret == False):
        print("Marvellous Automation Error: It is not A Directory With Name",DirectoryPath)
        return
    
    

    print("Log File Gets Created With Name: ",LogFileName)

    fobj = open(LogFileName,"w")

    fobj.write(Border+"\n")

    fobj.write("Marvellous Automation Script\n")

    fobj.write(Border+"\n\n")
    
    fobj.write("Files from the directory are:\n\n")

    fobj.write(Border+"\n")

    for FolderName, SubFolder, FileName in os.walk(DirectoryPath):
        for fname in FileName:
            fname = os.path.join(FolderName,fname)
            fobj.write(fname+"\n")

            print(f"FileName{fname}:{os.path.getsize(fname)}bytes")

    fobj.write(Border+"\n")

    fobj.write("LogFile Gets Created at :"+timestamp)

    fobj.write("\n"+Border+"\n")

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
            # schedule.every(1).minute.do(DirectoryScanner,sys.argv[1])

            DirectoryScanner(sys.argv[1])

            #while True:
               #schedule.run_pending()
               #time.sleep(1)



    else:
        print("Invalid Number of Arguments")
        print("Please use --h or --u for more information...")

    print(Border)
    print("Thank You For Using Marvellous Automation Script")
    print(Border)

    
if __name__ == "__main__":
    main()