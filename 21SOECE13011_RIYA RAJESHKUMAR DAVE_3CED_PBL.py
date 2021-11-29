import os
import shutil

source = input("Enter Source path:") + '/'
destination = input("Enter Destination path:") + '/'
for file in os.listdir(source):
    split_tup = os.path.splitext(file)
    extension = split_tup[1]
    extension = extension[1:]

    if extension == "":
        continue
    if not(os.path.isdir(destination+extension)):
        path = os.path.join(destination , extension)

        os.mkdir(path)
    s = source+file
    d = destination+extension+'/'+file

    if os.path.exists(d):
        print(file, "Already Exist")
        continue

    shutil.move(s, d)