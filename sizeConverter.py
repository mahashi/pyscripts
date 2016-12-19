from xml.dom.minidom import parse
from os import walk

def changeWidthAndHeight(files):
    print(file)
    f = open(file)
    dom = parse(f)
    f.close()
    f = open(file, 'w')
    dom.documentElement.setAttribute('width', '100')
    dom.documentElement.setAttribute('height', '100')
    dom.documentElement.writexml(f)
    f.close()

def getSvgFiles(dir):
    svgs = []
    for _, _, files in walk(dir):
        for file in files:
            if file.endswith('.svg'):
                svgs[] = file;

    return svgs