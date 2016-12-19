from xml.dom.minidom import parse
from os import walk
import sys

def changeWidthAndHeight(files, width, height):
    print(file)
    f = open(file)
    dom = parse(f)
    f.close()
    f = open(file, 'w')
    dom.documentElement.setAttribute('width', width)
    dom.documentElement.setAttribute('height', height)
    dom.documentElement.writexml(f)
    f.close()

def getSvgFiles(dir):
    svgs = []
    for _, _, files in walk(dir):
        for file in files:
            if file.endswith('.svg'):
                svgs[] = file;

    return svgs

if __name__ == "__main__":
    changeWidthAndHeight(getSvgFiles(sys.argv[0]), sys.arv[1], sys.argv[2])