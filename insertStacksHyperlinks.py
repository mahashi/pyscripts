from pathlib import Path
import re

#todo: parameterize
project_root = Path("C:\\Users\\Sadari\\Documents\\Writings\\Math\\Affine Objects")
tex_files = list(project_root.glob('**/*.tex'))

stacks_re = "[^{]Tag ([A-Z0-9]+)"

def findReplaceRe(expression, replacement):
	for file in tex_files:
		s = file.read_text()
		s = re.sub(expression, replacement, s)
		file.write_text(s)

def stacksrepl(matchobject):
	tag = matchobject.group(1);
	return "\href{{http://stacks.math.columbia.edu/tag/{0}}}{{Tag {0}}}".format(tag)

#findReplaceRe(stacks_re, stacksrepl)