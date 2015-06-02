import csv
import sklearn as sk
import numpy as np
from sklearn.svm import SVC
from sklearn.cross_validation import cross_val_score , KFold
from sklearn.feature_extraction.text import TfidfVectorizer

def get_stop_words():
    result = set()
    for line in open('stopwords_id.txt','rU').readline():
        result.add(line.strip())
    return result
    
stopwords = get_stop_words()  
clf_svc = SVC()  
features_1 = []
features_2 = []
features_3 = []
features_4 = []
features_5 = []
features_6 = []
features_7 = []
all_features = []
label = []

with open('preprocessed_dataset.csv','rU') as dataset:
	dataset_reader = csv.reader(dataset,delimiter = ',')
	with open('dataset_result','wb') as dataset_result:
		dataset_writer = csv.writer(dataset_result,delimiter = ' ')
		next(dataset_reader, None)
		for row in csv_cont:
			features_1.append(row[0])
			features_2.append(row[1])
			features_3.append(row[2])
			features_4.append(row[3])
			features_5.append(row[4])
			features_6.append(row[5])
			features_7.append(row[6])
			all_features.append([row[1],row[2],row[3],row[4],row[5],row[6]])
			label.append(row[7])
	
		total_len = len(label)
		x_svc_features_1 = TfidfVectorizer(stop_words=stopwords,token_pattern=ur"\b[a-z0-9_\-\.]+[a-z][a-z0-9_\-\.]+\b",).fit_transform(features_1)
		x_svc_features_2 = np.resize(features_2,(total_len,1))
		x_svc_features_3 = np.resize(features_3,(total_len,1))
		x_svc_features_4 = np.resize(features_4,(total_len,1))
		x_svc_features_5 = np.resize(features_5,(total_len,1))
		x_svc_features_6 = np.resize(features_6,(total_len,1))
		x_svc_features_7 = np.resize(features_7,(total_len,1))

		
		X_svc = [x_svc_features_1,x_svc_features_2,x_svc_features_3,x_svc_features_4,x_svc_features_5,x_svc_features_6,x_svc_features_7]

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
		print len(x_svc_features_1.shape)

		x_train_svc = all_features[:4074]
		x_test_svc = all_features[4074:]
		y_train_svc = label[:4074]
		y_test_svc = label[4074:]

		y_result = []
		clf_svc.fit(x_train_svc,y_train_svc)
		y_result = clf_svc.predict(x_test_svc)
		y_label = np.concatenate((y_train_svc,y_result))
		print len(y_label)
		dataset_writer.writerows(y_label)
