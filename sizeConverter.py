from xml.dom.minidom import parse
import os

for root, dirs, files in os.walk("~/Code/rAppid.js-sprd/sprd/img/masks"):
    for file in files:
        if file.endswith('.svg'):
            print(file)
            f = open(file)
            dom = parse(f)
            f.close()
            f = open(file, 'w')
            dom.documentElement.setAttribute('width', '100')
            dom.documentElement.setAttribute('height', '100')
            dom.documentElement.writexml(f)
            f.close()
