import os


def getAbsPath(filename):
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(THIS_FOLDER, filename)