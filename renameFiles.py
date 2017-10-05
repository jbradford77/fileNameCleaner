import os

def renameFiles():
    #1 get file names from folder
    fileList = os.listdir(r"C:\path\path")
    #2 print(fileList)
    saved_path = os.getcwd()
    print("Current working directory is "+saved_path)
    os.chdir(r"C:\path\path")
    #for each file, rename file
    for file_name in fileList:
        os.rename(file_name, file_name.translate(None, " _-1234567890"))
    os.chdir(saved_path)
    
renameFiles()
