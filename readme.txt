---documentation how to use---
---Contributor : Satya Nugraha---
---FULL cycle of Data Classification on predicting Local and Tourist tweets in NTB, Indonesia---

1.	Extract data from mongodb 
	Result : Tweet_Location, Hometown, Username, Tweet, Date, Latitude and Longitude . Then, store it to file december_16_ntb_training_data.csv

2.	We get dataset and we want to aggregate per username :
	1. 	For Tweet we just concatenate all of tweets per username. By running preprocessing_builder_concatenation_tweet.py
		Result : Array of tweets per username
		
		Then try to clean tweet. By running preprocessing_builder_cleaning_tweet.py
		Result : Array of cleaning tweet from noise / useless words (URL,punctuation,mention,unicode,emoticon)
		
		This still have noise, try to replace 2 spaces with 1 space. Loop this process until there in no mores 2 spaces or above. 
		
	2. 	For Tweet_Location we concatenate all of location per username. By running preprocessing_builder_concatenation_location.py
		Result : An array location or bunch location of user already visit
		
		And assigning location based on array that we already create. By running preprocessing_builder_assigning_location.py
		Result : Values about how many times they visit on certain location
		
		Then normalize values to get how many often they visit location. By running preprocessing_builder_normalizer_location.py
		Result : Percentage they visit location. 
		
		Then get average on normalize location. By running =average on excel function. REMEMBER: We only count location that have value. To handle that just delete all 0 values on percentage location.
		We normalize location to observe user movement if he/she travel a lot or not. If they travel a lot it tend to have lower average.
		
	3. 	For Total_Tweet we can run step_6_total_tweet
		Result : Numerical values of total tweets
	
	4. 	For Total_Days is difficult to automated because data is unsorted with first days tweets and last days tweets, i use excel to process it
		Try to delete time (hours:minutes:seconds), we only use date format. And try to give flag for first day and last days. Count interval between first day and last day.
		Result : Values of total day
		
		Tips : It can be automated count in python by converting date to timestamp date
	
	5. 	For Total_location is already on tweet location on normalize value.
		Result : On normalize values in tweet location, try to use function =counta it will count only value that appears in rows. And give us total location they are visiting in NTB.
	
	6. 	For Tweet_per_days just divide Total_Tweet with Total_Days
		Result : average tweet per days
	
	7.	For Location_per_days just divide Total_location with Total_Days
		Result : average visited location per day
		
	8. 	At this time we are not using geo latitude and longitude 
	
	
	Store it as one file on csv and determine which is training and which is testing
	The dataset columns will looks like this : Tweets, Average_normalizer_location, Total_Tweet, Total_Day, Tweet_per_day, Total_Visited_Location, Visited_Location_per_Day, LocalorTourist
	
3.	And classify with :
	1. 	Processing builder_mnb_classifier.py #MultinomialNaiveBayes machine learning
		This machine only use Bag of Words Feature
		Result : Accuracy on training data and predicted label on Testing Data 
	2. 	Processing builder_svm_classifier.py #SupportVectorMachine machine learning
		This machine use all features combined
		Result : Accuracy on training data and predicted label on Testing Data 
	3. 	Processing builder_dt_classifier.py #DecisionTress machine learning
		This machine use all features 
		Result : Accuracy on training data and predicted label on Testing Data 
		
	Try to manually classify 1000 random tweet on testing data and compare with 3 results from different machine learning (benchmark)
	Decide which have the best accuracy and store username and location and date and categories it to one file. 

4. 	Assign our label to our first dataset (data that we export from mongodb) :
	1.	Running builder_assigning_result.py
		Result : Date, Label, Longitude and Latitude

5.	Visualize data. Format file should like this : Date, Label, Latitude and Longitude :
	1. Geomapping by using CartoDB
	2. Give general graph 
