import os


def printFile(path, level):
    if os.path.exists(path):
        files = os.listdir(path)
        for f in files:
            subpath = os.path.join(path, f)
            if os.path.isfile(subpath):
                print ' ' * level + '- ' + os.path.basename(subpath)
            else:
                leveli = level + 1
                print ' ' * level + '- ' + os.path.basename(subpath)
                printFile(subpath, leveli)
if __name__ == '__main__':
    printFile(r'C:', 1)
