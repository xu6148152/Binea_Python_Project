#! python3

import os, shutil

def copyFile(sourceDir, destinationDir, postfix):
    absWorkingDir = os.path.abspath(sourceDir)
    absDestinationDir = os.path.abspath(destinationDir)
    for foldername, subfolders, filenames in os.walk(sourceDir):
        print('filenames ' + str(filenames))
    for filename in filenames:
        print('filename ' + str(filename))
        if filename.endswith(postfix):
            sourcePath = os.path.join(absWorkingDir, filename)
            destinationPath = os.path.join(absDestinationDir, filename)
            shutil.copy(sourcePath, destinationPath)

if __name__ == '__main__':
    copyFile('.', '..', '.py')
