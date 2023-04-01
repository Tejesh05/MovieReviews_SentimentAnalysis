from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from .models import *

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split


df = pd.read_csv('C:/Users/DELL/PycharmProjects/Django23/MysentimentAnaylse/Files/train.csv')
X_train, X_test, y_train, y_test = train_test_split(df['review'], df['sentiment'], test_size=0.2, random_state=42)

vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

clf = MultinomialNB()
clf.fit(X_train_vec, y_train)



def predict_sentiment(request):
    if request.method == 'POST':
        review = request.POST.get('review')
        new_review_vec = vectorizer.transform([review])
        predicted_sentiment = clf.predict(new_review_vec)[0]
        post=Review()
        post.Username= request.POST.get('user')
        post.Email= request.POST.get('email')
        post.review_text = request.POST.get('review')
        post.sentiment = predicted_sentiment
        post.save()
        return render(request, 'result.html', {'sentiment': predicted_sentiment})
    else:
        return render(request, 'index.html')
