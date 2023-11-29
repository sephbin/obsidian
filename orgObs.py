import yaml

import os, shutil


lut = {"adv_gww":r"E:\Obsidian\obsidian\GM - Campaigns\Ultima Thule"}

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