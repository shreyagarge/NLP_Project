import pickle

def classifier():
	data = open('/home/utoniumharsha/HARSHA/NLP/NLP_Project/training_data.txt', 'r')

	positive = {}
	negative = {}
	vocabulary = {}

	with open('vocabulary.pickle', 'rb') as handle:
		vocabulary = pickle.load(handle)

	with open('positive_words_count.pickle', 'rb') as handle:
		positive = pickle.load(handle)

	with open('negative_words_count.pickle', 'rb') as handle:
		negative = pickle.load(handle)

	positive_prob = {}
	negative_prob = {}

	V = len(vocabulary)
	Count_Positive = 0
	Count_Negative = 0

	for key in positive:
		Count_Positive += int(positive[key])

	for key in negative:
		Count_Negative += int(negative[key])

	for key in positive:
		if key in vocabulary.keys():
			positive_prob[key] = (int(positive[key]) + 1.0) / (Count_Positive + V)
		else:
			positive_prob[key] = (1.0) / (Count_Positive + V)

	for key in negative:
		if key in vocabulary.keys():
			negative_prob[key] = (int(negative[key]) + 1.0) / (Count_Negative + V)
		else:
			negative_prob[key] = (1.0) / (Count_Negative + V)

	with open('nbayes_positive_prob.pickle', 'wb') as handle:
		pickle.dump(positive_prob, handle)

	with open('nbayes_negative_prob.pickle', 'wb') as handle:
		pickle.dump(negative_prob, handle)

