#Automation script which accept directory name from user and display all names of duplicate files from that directory

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

def FindDuplicate(path):
    flag = os.path.isabs(path)

    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    dups = {}    # This is dictionary to store duplicate files (checksum will be key and file name will be values)

    if exists:
        for foldername, subfoldername, fileslist in os.walk(path):
            for filen in fileslist:
                path = os.path.join(foldername,filen)
                file_hash = hashfile(path)
                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]
            
            return dups
    else:
        print("Invalid path")

def PrintDuplicate(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))

    if len(results) > 0:
        print("Duplicates Found : ")

        print("The following files are identical : ")

        icnt = 0
        for result in results:
            for subresult in result:
                icnt+=1
                if icnt >= 2:
                    print("\t\t%s"% subresult)
    else:
        print("No duplicate files found")

def main():
    print("---------------- File Duplicate found-------------------")

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
        arr ={}
        arr = FindDuplicate(sys.argv[1])
        PrintDuplicate(arr)

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
# C:\Users\Priyanka\Desktop\Python_2024\01-06-2024>python FileDuplicate.py test
# ---------------- File Duplicate found-------------------
# Error : Invalid number of arguments
# Duplicates Found :
# The following files are identical :
#                 C:\Users\Priyanka\Desktop\Python_2024\01-06-2024\test\program161 - Copy (2).c
#                 C:\Users\Priyanka\Desktop\Python_2024\01-06-2024\test\program161 - Copy.c
#                 C:\Users\Priyanka\Desktop\Python_2024\01-06-2024\test\program161.c
#                 C:\Users\Priyanka\Desktop\Python_2024\01-06-2024\test\program163.c
#                 C:\Users\Priyanka\Desktop\Python_2024\01-06-2024\test\program163.pdf
# --------- Thank you for using our script -------------
# ------------- Marvellous Infosystems -----------------
