import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

text_data = np.array(['I love Brazil. Brazil!',
     'Brazil is best',
    'Germany beats both'])

count = CountVectorizer()
bag_of_words = count.fit_transform(text_data)

feature = bag_of_words.toarray()

target = np.array([0,0,1])

classifier = MultinomialNB(class_prior=[0.25,0.5])
model = classifier.fit(feature, target)
new_observation = [[0, 0, 0, 1, 0, 1, 0]]
pred = model.predict(new_observation)
print(pred)