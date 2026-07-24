def main():
    try:
        fobj = open("Demo.txt","r")
        print("File gets opened")

        print("file Offset is:",fobj.tell())        #0

        Data = fobj.read(10)

        print(Data)
        
        print("file Offset is:",fobj.tell())        #10
        
        Data = fobj.read(10)

        print(Data)
        
        print("file Offset is:",fobj.tell())        #20
        
        fobj.close()

    except FileNotFoundError as fobj:
        print("File is not present in current directory")

if __name__ == "__main__":
    main()