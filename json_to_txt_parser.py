import glob
import json
import os
from sys import argv
from pprint import pprint

'''
DON'T FORGET TO CHANGE THE PATH OF THE FILENAMES
'''

positive = open('/home/utoniumharsha/HARSHA/NLP/NLP_P/positive.txt', 'w') 
negative = open('/home/utoniumharsha/HARSHA/NLP/NLP_P/negative.txt', 'w')
path = '/home/utoniumharsha/HARSHA/NLP/NLP_P/AmazonReviews/laptops'

positive_count = 0
negative_count = 0
for filename in glob.glob(os.path.join(path, '*.json')):
	with open (filename) as data_file:
		data = json.load(data_file)
		for review in data["Reviews"]:
			if (review["Overall"] == "5.0"):
				try:
					if(positive_count < 500):
						positive.write(review["Content"])
						positive.write("\n")
						positive.write("\n")
						positive_count+=1
				except:
					pass
			elif (review["Overall"] == "1.0" or review["Overall"] == "2.0"):
				try:
					if(negative_count < 500):
						negative.write(review["Content"])
						negative.write("\n")
						negative.write("\n")
						negative_count+=1
				except:
					pass

print "positive = ",positive_count
print "negative = ",negative_count
positive.close()
negative.close()
