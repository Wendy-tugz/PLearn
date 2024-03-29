# import os
#
# path = "/Users/wendy/Documents/WEBMASTERS/PYTHON"
#
# if os.path.exists(path):
#     print("That location exits.")
#     if os.path.isfile(path):
#         print("That is a file.")
#     elif os.path.isdir(path):
#         print("That is a directory.")
# else:
#     print("That location doesn't exist.")

# Read a file

# try:
#     with open('test.tx') as file:
#         print(file.read())
# except FileNotFoundError:
#     print("File not found")

# write a file

# text = "Have a nice day! See yah!"
# with open('test.txt', 'a') as file:
#     file.write(text)

# copy a file
# copyfile(), copy() copy2()

# import shutil
#
# shutil.copyfile('test.txt', 'copy.txt') #scr, dst

# move files

# import os
# source = "mover.txt"
# destination = "/Users/wendy/Documents/mover.txt"
#
# try:
#     if os.path.exists(destination):
#         print("There is already a file there.")
#     else:
#         os.replace(source, destination)
#         print(source + " was moved")
#
# except FileNotFoundError:
#     print(source + "was not found")

# delete a file

import os
import shutil
path = "folder"

try:
    #os.remove(path)    #delete a file
    #os.rmdir(path)     #delete an empty directory
    shutil.rmtree(path) #delete a directory containing files
except FileNotFoundError:
    print("File was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print(" You can not delete that using that function")
else:
    print(path + " was deleted")
