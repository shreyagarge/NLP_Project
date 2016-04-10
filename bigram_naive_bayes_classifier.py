import pickle

def bigram_classifier():
	data = open('/home/utoniumharsha/HARSHA/NLP/NLP_Project/training_data.txt', 'r')

	positive = {}
	negative = {}
	bigram_vocabulary = {}

	with open('bigram_vocabulary.pickle', 'rb') as handle:
		bigram_vocabulary = pickle.load(handle)

	with open('positive_bigrams_count.pickle', 'rb') as handle:
		bigram_positive = pickle.load(handle)

	with open('negative_bigrams_count.pickle', 'rb') as handle:
		bigram_negative = pickle.load(handle)

	positive_prob = {}
	negative_prob = {}

	V = len(bigram_vocabulary)
	Count_Positive = 0
	Count_Negative = 0

	for word1 in bigram_positive:
		for word2 in bigram_positive[word1]:
			Count_Positive += int(bigram_positive[word1][word2])

	for word1 in bigram_negative:
		for word2 in bigram_negative[word1]:
			Count_Negative += int(bigram_negative[word1][word2])

	for word1 in bigram_positive:
		positive_prob[word1] = {}
		for word2 in bigram_positive[word1]:
			positive_prob[word1][word2] = (int (bigram_positive[word1][word2]) + 1.0 ) / (Count_Positive + V)

	for word1 in bigram_negative:
		negative_prob[word1] = {}
		for word2 in bigram_negative[word1]:
			negative_prob[word1][word2] = (int (bigram_negative[word1][word2]) + 1.0 ) / (Count_Negative + V)


	with open('bigram_nbayes_positive_prob.pickle', 'wb') as handle:
		pickle.dump(positive_prob, handle)

	with open('bigram_nbayes_negative_prob.pickle', 'wb') as handle:
		pickle.dump(negative_prob, handle)
	
#bigram_classifier()