''' Author: Abhijit Bangera
	Python: Python 3.x
	Description: 
		Generate a dynamic Dictionary on the fly. Read the input file and relate similar values to its Key.
	Input (taken from text file):
		Red Apple
		Orange Orange
		Red Strawberry
		Red Tomoto
		Orange Carrot
		Yellow Mango
	Output:
		{'Red': ['Apple', 'Strawberry', 'Tomoto'], 'Orange': ['Orange', 'Carrot'], 'Yellow': ['Mango']}

'''

from collections import defaultdict
myDict = {}
fileObject= open("input.txt","r")
for line in fileObject:
	lineNoSpace = line.rstrip()
	lineText = lineNoSpace.split(" ")
	if lineText[0] not in myDict:
		myDict[lineText[0]]=[lineText[1]]
	else:
		myDict[lineText[0]].append(lineText[1])
print (myDict)
