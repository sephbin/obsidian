import yaml

import os, shutil, json


lut = {"adv_gww":r"E:\Obsidian\obsidian\GM - Campaigns\Ultima Thule"}
directory = []


for root, dirs, files in os.walk(".", topdown=False):
	#print(root, dirs, files)

	for file in files:
		try:
			if file.endswith(".md"):
				#print(root, dirs,file)
				fileloc = os.path.join(root,file)
				with open(fileloc,"r", encoding="utf-8") as file:
					contents = file.read()
					if "---\n" not in contents: continue
					yamlt = contents.split("---\n")[1]
					yamlt = yaml.safe_load(yamlt)
					#print(yamlt)
				sublocation = None
				for tag in yamlt["tags"]:
					if tag not in ["character"]: continue
					sublocation = "1.0 Characters"
				for tag in yamlt["tags"]:
					if tag not in lut: continue
					newlocation = lut[tag]
					if sublocation:
						newlocation = os.path.join(newlocation,sublocation)
					print(fileloc, newlocation)
					try:	shutil.move(fileloc, newlocation)
					except Exception as e:	print(e)
				


		except: pass

for root, dirs, files in os.walk(".", topdown=False):
	for file in files:
		willContinue = False
		for ignore in [".git",".obsidian"]:
			if ignore in root: willContinue = True
		if willContinue: continue
		fileloc = os.path.join(root,file)
		directory.append(fileloc)
print(directory)

with open("directory.json", "w") as file:
	json.dump(directory,file)