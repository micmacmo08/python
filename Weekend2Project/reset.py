from os import listdir, remove
from os.path import isfile, join
from shutil import move

workingDir = 'F:\\Users\\Mike\\OneDrive\\Documents\\GitHub\\Python\\Weekend2Project\\'

archiveFiles = [f for f in listdir(workingDir + "Archive\\") if isfile(join(workingDir + "Archive\\",f)) and f[-5:] == ".xlsx"]
errorFiles = [f for f in listdir(workingDir + "Error\\") if isfile(join(workingDir + "Error\\",f)) and f[-5:] == ".xlsx"]

for file in archiveFiles:
    move(workingDir + "Archive\\" + file, workingDir + file)

for file in errorFiles:
    move(workingDir + "Error\\" + file, workingDir + file)

remove(workingDir + "file.lst")
remove(workingDir + "project.log")