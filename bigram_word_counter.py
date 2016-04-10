import pickle

def make_bigram_counter_list():
	data = open('/home/utoniumharsha/HARSHA/NLP/NLP_Project/training_data.txt', 'r')
	positive = {}
	negative = {}
	
	for line in data.readlines():
		sentence = line.split(" ")
		if sentence[0] == "+":
			for i in range (1, len(sentence)):
				word1 = sentence[i-1]
				word2 = sentence[i]
				if((word1 != "+" or word1 != "" or word1 != " ") and (word2 != "+" or word2 != "" or word2 != " ")):
					if word1 in positive.keys():
						if word2 in positive[word1].keys():
							positive[word1][word2] = str( int( positive[word1][word2]) + 1)
						else:
							positive[word1][word2] = '1'
					else:
						positive[word1] = {}
						positive[word1][word2] = '1'

		elif sentence[0] == "-":
			for i in range (1, len(sentence)):
				word1 = sentence[i-1]
				word2 = sentence[i]
				if((word1 != "-" or word1 != "" or word1 != " ") and (word2 != "-" or word2 != "" or word2 != " ")):
					if word1 in negative.keys():
						if word2 in negative[word1].keys():
							negative[word1][word2] = str( int( negative[word1][word2]) + 1)
						else:
							negative[word1][word2] = '1'
					else:
						negative[word1] = {}
						negative[word1][word2] = '1'


	with open('positive_bigrams_count.pickle', 'wb') as handle:
		pickle.dump(positive, handle)

	with open('negative_bigrams_count.pickle', 'wb') as handle:
		pickle.dump(negative, handle)

make_bigram_counter_list()