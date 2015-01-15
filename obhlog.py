# -*- coding: utf-8 -*-


orgLogFileName = 'yjh-obh.log'
newLogFileName = 'obh.log'


def getLogFromLine(line):
	searchKey = '|TEXT:OBH '
	keyIndex = line.find(searchKey)
	if keyIndex > 0:
		return line[keyIndex:]

def getLogFromLines(lines):
	logs = []
	for line in lines:
		log = getLogFromLine(line)
		if log:
			logs.append(log)
	return logs

def logsToText(logs):
	text = ''
	for log in logs:
		text += log + '\n'
	return text

def readOrgLogFile():
	f = open(orgLogFileName, 'r')
	text = f.read()
	f.close()
	return text

def writeLogFile(text):
	f = open(newLogFileName, 'w')
	f.write(text)
	f.close()

def main():
	text = readOrgLogFile()
	lines = text.splitlines()
	logs = getLogFromLines(lines)
	text = logsToText(logs)
	writeLogFile(text)


if __name__ == '__main__':
	main()