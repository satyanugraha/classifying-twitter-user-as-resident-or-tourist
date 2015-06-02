import csv
from collections import Counter

cnt = Counter()
list_amount = []
with open('dataset.csv','rU') as read_file:
    reader = csv.reader(read_file,skipinitialspace=True)
    #next(reader,None)
    for line in reader:
        username = line[2]
        cnt[username] += 1
        
    for amount in cnt.values():
        list_amount.append(amount)

with open('step_6_output_total_tweet.csv','wb') as write_file:
    writer_file = csv.writer(write_file,delimiter=',')
    for amount in list_amount:
		#print amount
		#ex = amount
		writer_file.writerow([amount])
