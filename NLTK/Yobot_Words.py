import glob
import more_itertools as triplets
path = 'D:\\Yobot_Practice\\**.txt'
files=glob.glob(path)
for file in files:
	f = open(file, 'r')
	words = f.read().split()
	word_sequence = list(triplets.windowed(words, n = 3, step = 1))
	word_dict = dict(zip((i[1] for i in word_sequence), word_sequence))
	f.close()
