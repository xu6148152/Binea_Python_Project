import os
import sys

def batch_rename(work_dir, old_txt, new_txt):
    for fileName in os.listdir(work_dir):
        file_ext = os.path.split(fileName)[1]

        if old_txt == file_ext:
            newFile = fileName.replace(old_txt, new_txt)
            os.rename(
                os.path.join(work_dir, fileName),
                os.path.join(work_dir, newFile)
                )

def main():
    work_dir = sys.argv[1]
    old_txt = sys.argv[2]
    new_txt = sys.argv[3]
    batch_rename(work_dir, old_txt, new_txt)

if __name__ == '__main__':
    main()                    