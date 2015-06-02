import csv
import sklearn as sk
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from pprint import pprint
from sklearn.cross_validation import cross_val_score, KFold
from scipy.stats import sem
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from sklearn import cross_validation
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer, HashingVectorizer, CountVectorizer
from sklearn import metrics
from sklearn import tree
#Feature selection varianceThreshold
from sklearn.feature_selection import VarianceThreshold
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
#univariate feature selection
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
#Tree-based feature selection
from sklearn.ensemble import ExtraTreesClassifier

def get_stop_words():
    result = set()
    for line in open('stopwords_id.txt','rU').readline():
        result.add(line.strip())
    return result

stopwords = get_stop_words()
clf_mnb = MultinomialNB()
x_mnb = []
y_mnb = []
with open('preprocessed_dataset.csv','rU') as dataset:
    dataset_reader = csv.reader(dataset,delimiter = ',')
    with open('dataset_result','wb') as dataset_result:
        dataset_writer = csv.writer(dataset_result,delimiter = ' ')
        next(dataset_reader, None)
        for row in dataset_reader:
            x_mnb.append(row[0])
            y_mnb.append(row[7])

        total_training = 4074
        total_testing = len(x_mnb) - total_training
        print total_training
        print total_testing
        print len(x_mnb)
        x_vectorized = TfidfVectorizer(stop_words=stopwords,token_pattern=ur"\b[a-z0-9_\-\.]+[a-z][a-z0-9_\-\.]+\b",).fit_transform(x_mnb)
        y_numpy = np.array(y_mnb)
        print ('----')
        print x_vectorized.shape
        print y_numpy.shape
        x_train_mnb = x_vectorized[:4074]
        x_test_mnb = x_vectorized[4074:]
        y_train_mnb = y_numpy[:4074]
        y_test_mnb = y_numpy[4074:]
        
        #machine learning
        y_result = []
        clf_mnb.fit(x_train_mnb,y_train_mnb)
        y_result = clf_mnb.predict(x_test_mnb)
        y_label = np.concatenate((y_train_mnb,y_result))
        
        dataset_writer.writerows(y_label)
        
