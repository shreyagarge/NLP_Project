import pickle

def make_word_counter_list():
	data = open('/home/utoniumharsha/HARSHA/NLP/NLP_Project/training_data.txt', 'r')
	positive = {}
	negative = {}
	
	for line in data.readlines():
		sentence = line.split(" ")
		if sentence[0] == "+":
			for word in sentence:
				if(word != "+" or word != "" or word != " "):
					if word in positive.keys():
						positive[word] = str( int(positive[word]) + 1)
					else:
						positive[word] = "1"
		elif sentence[0] == "-":
			for word in sentence:
				if(word != "-" or word != "" or word != " "):
					if word in negative.keys():
						negative[word] = str( int(negative[word]) + 1)
					else:
						negative[word] = "1"

	with open('positive_words_count.pickle', 'wb') as handle:
		pickle.dump(positive, handle)

	with open('negative_words_count.pickle', 'wb') as handle:
		pickle.dump(negative, handle)