import yaml

import os


for root, dirs, files in os.walk(".", topdown=False):
	#print(root, dirs, files)

	for file in files:
		if file.endswith(".md") and "Pool" in file:
			#print(root, dirs,file)
			with open(os.path.join(root,file),"r") as file:
				contents = file.read()
				if "---\n" not in contents: continue
				yamlt = contents.split("---\n")[1]
				yamlt = yaml.safe_load(yamlt)
				print(yamlt)
				break
