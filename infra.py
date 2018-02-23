import os
from os import listdir
from os.path import isfile, join
import sys


if (len(sys.argv)<3):       # current folder , destination folder
    raise "Too Few Arguments"

sourcePath= sys.argv[1]
destinationPath= sys.argv[2]

ignoreExtensionList=['.pdf','.xlsx']

onlyfiles = [f for f in listdir(sourcePath) if isfile(join(sourcePath, f))]

vara=[os.path.splitext(sourcePath+currFile) for currFile in onlyfiles]

extensionList= [tempA[1] for tempA in vara]


uniqueExtensionList= list(set(extensionList))

for currIgnore in ignoreExtensionList:
    if currIgnore in uniqueExtensionList:
        uniqueExtensionList.remove(currIgnore)


for currExten in uniqueExtensionList:
    currExtension= currExten[1:]
    if not os.path.exists(destinationPath+currExtension):
        os.makedirs(destinationPath+currExtension)


for currentMoveFile in onlyfiles:
    k = currentMoveFile.rfind(".")
    moveFolder=currentMoveFile[(k+1):]
    if os.path.exists(destinationPath+moveFolder):
        os.rename(sourcePath+currentMoveFile,destinationPath+moveFolder+"/"+currentMoveFile)



