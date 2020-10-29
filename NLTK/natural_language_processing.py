#Natural Language Processing

import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 

#Import the dataset
dataset = pd.read_csv('Restaurant_Reviews.tsv', delimiter = '\t', quoting =3)

#Cleaning the texts
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus = []
for i in range(0, 1000):
	review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
	review = review.lower()
	review = review.split()
	ps = PorterStemmer()
	review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
	review = ' '.join(review)
	corpus.append(review)

#Creating the Bag of Words model
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, 1].values

#Add a machine learning regression or classification model here