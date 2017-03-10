import os

__author__ = 'xubinggui'

def listAllPythonFiles(path):

    listFiles = os.listdir(path)

    for x in listFiles:

        if (os.path.isdir(x)):

            listAllPythonFiles(x)

        else:
            if(os.path.splitext(x)[1] == '.py'):
                print(os.path.join(path, x))

listAllPythonFiles('.')