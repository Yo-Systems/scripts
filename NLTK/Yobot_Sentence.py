import glob
from nltk import sent_tokenize
path = 'D:\\Yobot_Practice\\**.txt'
files=glob.glob(path)
for file in files:
	f = open(file, 'r')
	text = f.read()
	sentences = sent_tokenize(text)
	f.close()
