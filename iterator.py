#coding: UTF-8

import sys

if len(sys.argv) != 4:
	print("Usage: % {0} filename from_number to_number".format(sys.argv[0]))
	quit()

targetFile = sys.argv[1]
fromNum    = int( sys.argv[2] )
toNum      = int( sys.argv[3] )

try:
	fileObject = open( targetFile, "r" )
except:
	print("cannot open: {0}".format(targetFile))
	quit()
else:
	lines = fileObject.readlines()
	fileObject.close()

for cnt in range(fromNum, toNum+1):
	for str in lines:
		while True:
			startPos = str.find(r"${CNT:")
			if startPos == -1:
				print(str, end="")
				break
			else:
				print(str[:startPos], end="")
				endPos = str.find(r"}", startPos+1)
				formatStr = "{0:" + str[startPos+6:endPos] + "}"
				print(formatStr.format(cnt), end="")
				str = str[endPos+1:]

quit()

