from sys import *
import os
import hashlib
import sys

def hashfile(path,blocksize=1024):  #1024kb We can given any blocksize. path is like bucket and blocksize is like mug
    afile =open(path,'rb')   # to calculate the checksum we have  open file in binary mode
    hasher = hashlib.md5()
    
    buf = afile.read(blocksize)
    
    while len(buf) > 0:
        hasher.update(buf)  # updating data as we are getting  
        buf = afile.read(blocksize)
    
    afile.close()
    
    return hasher.hexdigest() # actual checksum gets calculated here after getting all data

def DisplayChecksum(path):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)
    
    exists = os.path.isdir(path)

    if exists:
        for dirName, subdirs,fileList in os.walk(path):
            print("Current folder is : ",dirName)
            for filen in fileList:
                path = os.path.join(dirName,filen)
                file_hash = hashfile(path)
                print(path)
                print(file_hash)
                print(' ')
    else:
        print("Invalid path")
def main():
    print("---------------- Directory Watcher -------------------")

    if(len(sys.argv) == 2):
         print("Error : Invalid number of arguments")
         
    if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
        print("This script is used to perform Directory traversal")
        exit()

    if(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
        print("Usage of the script : ")
        print("Usage : ApplicationName AbsolutePath_of_Direcrory")
        exit()

    try:
            
        arr = DisplayChecksum(sys.argv[1])
    
    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception as E:
        print("Error : Invalid input ", E)
            
    
    
    print("--------- Thank you for using our script -------------")
    print("------------- Marvellous Infosystems -----------------")

if __name__ == "__main__":
    main()

#if you open the file in binary mode then you can open any kind of file to calculate checksum (audio,video,img,nay kind of file)

# Output:
# C:\Users\Priyanka\Desktop\Python_2024\01-06-2024>python DirectoryFileChecksum.py test
# ---------------- Directory Watcher -------------------
# Error : Invalid number of arguments
# Current folder is :  C:\Users\Priyanka\Desktop\Python_2024\01-06-2024\test
# C:\Users\Priyanka\Desktop\Python_2024\01-06-2024\test\duplicate.c
# 38bc92405c17ba12fda1f5ce3124c4f6

# C:\Users\Priyanka\Desktop\Python_2024\01-06-2024\test\program161.c
# 38bc92405c17ba12fda1f5ce3124c4f6

# C:\Users\Priyanka\Desktop\Python_2024\01-06-2024\test\program162.c
# 9cb00a44e52e0390d24fb241c6900eb8

# C:\Users\Priyanka\Desktop\Python_2024\01-06-2024\test\program163.c
# 0315b2dfbda782c7b8d74acee214b169

# C:\Users\Priyanka\Desktop\Python_2024\01-06-2024\test\program164.c
# e2cedc014f44219d33369a52bd965853

# --------- Thank you for using our script -------------
# ------------- Marvellous Infosystems -----------------