#! python3

import os, send2trash

def deleteBigFile(dir, filesize):
    for filename in os.listdir(dir):
        print("filenames " + str(filename))
        if os.path.getsize(filename) > filesize:
            print("delete file: " + filename)
            send2trash.send2trash(filename)

if __name__ == '__main__':
    deleteBigFile('.', 100000)