import os

def main():
    ret = os.path.exists("Demo.txt")

    if(ret == True):
        print("File is Present in Current Directory")

    else:
        print("There is no such file")

if __name__ == "__main__":
    main()