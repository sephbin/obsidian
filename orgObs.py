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



import clr
clr.AddReference('System.Core')
clr.AddReference('RhinoInside.Revit')
clr.AddReference('RevitAPI') 
clr.AddReference('RevitAPIUI')
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager

from RhinoInside.Revit import Revit, Convert
from Autodesk.Revit import DB
import System

doc = Revit.ActiveDBDocument
app = Revit.ActiveDBApplication

version = doc.GetDocumentVersion(doc)
versionGUID = version.VersionGUID
changedElements = doc.GetChangedElements(versionGUID)

modElements = changedElements.GetCreatedElementIds()
modElements = changedElements.GetModifiedElementIds() ## testing the different methods

for mE in modElements:
    print(mE)
    el = doc.GetElement(mE)
    print(el)
    print("-"*100)





