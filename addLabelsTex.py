from pathlib import Path
import os, re, fnmatch

environments_white = ['definition', 'lemma', 'theorem', 'proposition', 'remark', 'corollary', 'example']
overwrite = True
project_root = Path("C:\\Users\\Sadari\\Documents\\Writings\\Math\\Affine Objects")

label_list = []
replace_labels = []
tex_files = list(project_root.glob('**/*.tex'))

all_re = "begin{([^}]*)}(\[([^\]\\\$]*)\])?[^\w]*$"
basic_re = "begin{([^}]*)}(\[[^\]]*\])?\s*$"
label_re = "\\label\[?\w*\]?{?([^}]+)?}?"

def findReplaceLabels():
	for file in tex_files:
		s = file.read_text()
		for item in replace_labels:
			if item[0] is None: 
				continue
			s = s.replace("\Cref{" + item[0], "\Cref{" + item[1])
			s = s.replace("," + item[0] + "}", "," + item[1] + "}")
			s = s.replace("," + item[0] + ",", "," + item[1] + ",")
		file.write_text(s)

def processLine(line, counter):
	new_label = hex(counter)[2:]
	#print(counter)
	label_match = re.search(label_re, line)
	
	if label_match is not None:
		current_label = label_match.group(1)
		if not overwrite:
			label_list.append(current_label)
			return line
		else:
			line_without_label = line.split("\label")[0]
			replace_labels.append([current_label, new_label])
			return processLine(line_without_label, counter)


	basic_match = re.search(basic_re, line)
	if basic_match is None:
		return line
	env_type = basic_match.group(1)

	if env_type not in environments_white:
		return line

	return appendLabel(line, env_type, new_label)

def appendLabel(current_line, env_type, name):
	label_list.append(name)
	print(name)
	return current_line + "\label[" + env_type + "]{" + name + "}"

def addLabels():
	counter = 0
	for tex_file in tex_files:
		text = tex_file.read_text()
		# copy = tex_file.parent / (tex_file.parts[-1][:-4] + '-copy.tex')
		new_text = ""
		for line in text.splitlines():
			new_text += processLine(line, counter) + '\n'
			counter += 1
			while hex(counter)[2:] in label_list:
				counter += 1

		tex_file.write_text(new_text[:-1])
	print(str(replace_labels)) 
	findReplaceLabels()