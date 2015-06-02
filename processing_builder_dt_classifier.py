import csv
import sklearn as sk
import numpy as np
from sklearn import tree
from sklearn.cross_validation import cross_val_score , KFold
from sklearn.feature_extraction.text import TfidfVectorizer

def get_stop_words():
    result = set()
    for line in open('stopwords_id.txt','rU').readline():
        result.add(line.strip())
    return result
    
stopwords = get_stop_words()  
clf_dt = tree.DecisionTreeClassifier()
all_features_without_bow = []
label = []

with open('preprocessed_dataset.csv','rU') as dataset:
	dataset_reader = csv.reader(dataset,delimiter = ',')
	with open('dataset_result.csv','wb') as dataset_result:
		dataset_writer = csv.writer(dataset_result,delimiter = ' ')
		next(dataset_reader, None)
		for row in csv_cont:
			all_features_without_bow.append([row[1],row[2],row[3],row[4],row[5],row[6]])
			label.append(row[7])
	
		total_len = len(label)		
		total_training = 4074
		total_testing = len(label) - total_training
		
		print ('total_training')
		print total_training
		print ('total_testing')
		print total_testing
		print ('total features combined')
		print len(X_svc)
		print ('total all features combined')
		print len(all_features)
		print ('total label')
		print len(label)
		print ('total_features_1')

		x_train_dt = all_features_without_bow[:4074]
		x_test_dt = all_features_without_bow[4074:]
		y_train_dt = label[:4074]
		y_test_dt = label[4074:]

		y_result = []
		clf_dt.fit(x_train_dt,y_train_dt)
		y_result = clf_dt.predict(x_test_dt)
		y_label = np.concatenate((y_train_dt,y_result))
		print len(y_label)
		dataset_writer.writerows(y_label)
