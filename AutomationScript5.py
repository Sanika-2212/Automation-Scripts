import sys

def main():

    print("--------------------------------------------------------------------------")
    print("Marvellous Automation Script")
    print("--------------------------------------------------------------------------")

    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This Automation Script is used to travel the directory.")
            print("For Better Usage please check --u flag...")
        
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Please Execute the script as ")
            print("Python FileName.py DirectoryName")
            print("Directory name should be absolute path...")

        else:
            DirectoryName = sys.argv[1]
            print("Directory Name is:",DirectoryName)


    else:
        print("Invalid Number of Arguments")
        print("Please use --h or --u for more information...")

    print("--------------------------------------------------------------------------")
    print("Thank You For Using Marvellous Automation Script")
    print("--------------------------------------------------------------------------")

    
if __name__ == "__main__":
    main()