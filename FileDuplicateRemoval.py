# Automation script which accept directory name from user and display all names of duplicate files and remove the duplicate files from that directory
#if you open the file in binary mode then you can open any kind of file to calculate checksum (audio,video,img,nay kind of file)

import sys
import time
import os
import hashlib

def DeleteFiles(dict1):
    results = list(filter(lambda x:len(x) > 1, dict1.values()))

    icnt = 0
    if len(results) > 0:
        for result in results:
            for subresult in result:
                icnt+=1
                if icnt >= 2:
                    os.remove(subresult)
            icnt = 0
    else:
        print("No duplicate files found")

def hashfile(path, blocksize = 1024):   # 1024kb We can given any blocksize. path is like bucket and blocksize is like mug
    afile = open(path,"rb")             # to calculate the checksum we have  open file in binary mode
    hasher = hashlib.md5()

    buf = afile.read(blocksize)

    while len(buf) > 0:
        hasher.update(buf)               # updating data as we are getting  
        buf = afile.read(blocksize)
    
    afile.close()

    return hasher.hexdigest()           # actual checksum gets calculated here after getting all data

def findDuplicate(path):
    flag = os.path.isabs(path)

    if(flag == False):
        path = os.path.abspath(path)
    
    exists = os.path.isdir(path)

    dups = {}                          # This is dictionary to store duplicate files (checksum will be key and file name will be values)

    if exists:
        for foldername, subfoldername, fileslist in os.walk(path):
            print("Current folder is : ",path)
            for filename in fileslist:
                path = os.path.join(foldername,filename)
                file_hash = hashfile(path)

                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]

        return dups
    else:
        print("Invalid Path")
       
def printResults(dict1):
    results = list(filter(lambda x : len(x) > 1, dict1.values()))

    if len(results) > 0:
        print("Duplicates found: ")
        print("The following files are the duplicate")

        for result in results:
            for subresult in result:
                print("\t\t%s" % subresult)
    else:
        print("No duplicate files found")

def main():
    print("--------------Duplicate file removal---------------")

    print("Application name",sys.argv[0])

    if(len(sys.argv) != 2):
        print("Invalis number of arguments")
        exit()

    if(sys.argv[1]=="-h") or (sys.argv[1]=="-H"):
        print("This script is used to traverse specific directory, find duplicate files and delete duplicate files")
        exit()

    if(sys.argv[1]=="-u") or (sys.argv[1]=="-U"):
        print("Usage : ApplicationName AbsolutePath_Of_Directory")
        exit()
        
    try:
        arr = {}
        startTime = time.time()
        arr = findDuplicate(sys.argv[1])
        printResults(arr)
        DeleteFiles(arr)
        endTime = time.time()

        print("Took %s seconds to evaluate." %(endTime - startTime))
    
    except ValueError:
        print("Error : Invalid datatype of input")
    
    except Exception as E:
        print("Error : Invalid input",E)



# if __name__ == "__main__":
#     main()

# Output:
# C:\Users\Priyanka\Desktop\Python_2024\01-06-2024>python FileDuplicateRemoval.py test
# --------------Duplicate file removal---------------
# Application name FileDuplicateRemoval.py
# Current folder is :  C:\Users\Priyanka\Desktop\Python_2024\01-06-2024\test
# Current folder is :  C:\Users\Priyanka\Desktop\Python_2024\01-06-2024\test\program164.c
# Duplicates found:
# The following files are the duplicate
#                 C:\Users\Priyanka\Desktop\Python_2024\01-06-2024\test\duplicate.c
#                 C:\Users\Priyanka\Desktop\Python_2024\01-06-2024\test\program161 - Copy (2).c
#                 C:\Users\Priyanka\Desktop\Python_2024\01-06-2024\test\program161 - Copy.c
#                 C:\Users\Priyanka\Desktop\Python_2024\01-06-2024\test\program161.c
#                 C:\Users\Priyanka\Desktop\Python_2024\01-06-2024\test\demo\program161.c
#                 C:\Users\Priyanka\Desktop\Python_2024\01-06-2024\test\program163.c
#                 C:\Users\Priyanka\Desktop\Python_2024\01-06-2024\test\program163.pdf
# Took 0.01392221450805664 seconds to evaluate.