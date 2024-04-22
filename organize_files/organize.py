import os
import shutil

path = input("Enter path: ")
files = os.listdir(path)

for file in files:
    filename, extension = os.path.splitext(file)
    extension = extension[1:]
    
    if os.path.exists(os.path.join(path, extension)):
        shutil.move(file, os.path.join(path, extension))
    else:
        os.mkdir(os.path.join(path, extension))
        shutil.move(file, os.path.join(path, extension))