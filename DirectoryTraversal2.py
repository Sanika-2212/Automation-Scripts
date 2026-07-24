import os

def main():
    for FolderName, SubFolder, FileName in os.walk("Marvellous"):
        print("FolderName:",FolderName)

        for subf in SubFolder:
            print("SubFolder Name:",subf)

if __name__ =="__main__":
    main()