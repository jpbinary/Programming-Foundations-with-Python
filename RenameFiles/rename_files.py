import os

def rename_files():
    files = os.listdir("files/prank") # files/ is a reference to a folder in the cwd
    print files
    saved_path = os.getcwd()
    print("Current working directory is: " + saved_path)
    os.chdir("files/prank")
    current_path = os.getcwd()
    print("Current working directory is: " + current_path)

    for file_name in files:
        print("Old File Name: " + file_name)
        # remove numbers from each file_name
        os.rename(file_name, file_name.translate(None, "0123456789"))
        print("New File Name: " + file_name.translate(None, "0123456789"))
              
    os.chdir(saved_path)


rename_files()
