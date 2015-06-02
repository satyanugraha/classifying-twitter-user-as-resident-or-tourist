import csv
dict={}
with open('dataset.csv','rU') as f:
    reader = csv.reader(f,skipinitialspace=True)
    for line in reader:
        try:
            dict[line[2]].append(line[3].replace("\n",", "))
            
        except:
            dict[line[2]]=[line[3].replace("\n",", ")]

with open('step_1_output_tweet_concatenation_dataset.csv','w') as f:
    writer = csv.writer(f, delimiter=',',dialect='excel-tab')
    for key in dict:
        writer.writerow([key,'  '.join(dict[key])])
