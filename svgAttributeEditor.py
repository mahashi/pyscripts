from xml.dom.minidom import parse
from os import walk
import sys

def changeAttributes(files, dict):
    for file in files:
    	print file
        f = open(file)
        dom = parse(f)
        f.close()
        f = open(file, 'w')
        for key, value in dict.items():
            dom.documentElement.setAttribute(key, value)
        dom.documentElement.writexml(f)
        f.close()

def getSvgFiles(dir):
    svgs = []
    for root, _, files in walk(dir):
        for file in files:
            if file.endswith('.svg'):
                svgs.append('{}/{}'.format(root, file))
	print "files"
    return svgs

if __name__ == "__main__":
	print "test"
	print sys.argv
	changeAttributes(getSvgFiles(sys.argv[1]), {sys.argv[2]: sys.argv[3]})
