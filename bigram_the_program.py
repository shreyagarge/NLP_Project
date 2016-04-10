import pickle
import math

def the_actual_program():

	test_data = open('/home/utoniumharsha/HARSHA/NLP/NLP_Project/test_data.txt', 'r')
	training_data = open('/home/utoniumharsha/HARSHA/NLP/NLP_Project/training_data.txt', 'r')

	unigram_vocabulary = {}
	bigram_vocabulary = {}

	unigram_positive = {}
	unigram_negative = {}

	bigram_positive = {}
	bigram_negative = {}

	positive_class_prob_bigram = {}
	negative_class_prob_bigram = {}

	positive_class_prob_unigram = {}
	negative_class_prob_unigram = {}

	actual_list = []

	with open('vocabulary.pickle', 'rb') as handle:
		unigram_vocabulary = pickle.load(handle)

	with open('bigram_vocabulary.pickle', 'rb') as handle:
		bigram_vocabulary = pickle.load(handle)

	with open('positive_words_count.pickle', 'rb') as handle:
		unigram_positive = pickle.load(handle)

	with open('negative_words_count.pickle', 'rb') as handle:
		unigram_negative = pickle.load(handle)

	with open('positive_bigrams_count.pickle', 'rb') as handle:
		bigram_positive = pickle.load(handle)

	with open('negative_bigrams_count.pickle', 'rb') as handle:
		bigram_negative = pickle.load(handle)

	with open('nbayes_positive_prob.pickle', 'rb') as handle:
		positive_class_prob_unigram = pickle.load(handle)

	with open('nbayes_negative_prob.pickle', 'rb') as handle:
		negative_class_prob_unigram = pickle.load(handle)

	with open('bigram_nbayes_positive_prob.pickle', 'rb') as handle:
		positive_class_prob_bigram = pickle.load(handle)

	with open('bigram_nbayes_negative_prob.pickle', 'rb') as handle:
		negative_class_prob_bigram = pickle.load(handle)

	pos_class = 0
	neg_class = 0

	uni_V = len(unigram_vocabulary)
	unigram_Count_Positive = 0
	unigram_Count_Negative = 0

	bi_V = len(bigram_vocabulary)
	bigram_Count_Positive = 0
	bigram_Count_Negative = 0

	for key in unigram_positive:
		unigram_Count_Positive += int(unigram_positive[key])

	for key in unigram_negative:
		unigram_Count_Negative += int(unigram_negative[key])

	for word1 in bigram_positive:
		for word2 in bigram_positive[word1]:
			bigram_Count_Positive += int(bigram_positive[word1][word2])

	for word1 in bigram_negative:
		for word2 in bigram_negative[word1]:
			bigram_Count_Negative += int(bigram_negative[word1][word2])

	for line in training_data:
		sentence = line.split(" ")
		if sentence[0] == "+":
			pos_class += 1
		elif sentence[0] == "-":
			neg_class += 1

	print "positive_classes = ", pos_class
	print "negative_classes = ", neg_class

	pos_add_one = math.log(1.0/(unigram_Count_Positive + uni_V))
	neg_add_one = math.log(1.0/(unigram_Count_Negative + uni_V))

	final_predicted_list = []

	for line in test_data:
		test_data_unigram_counter = {}
		test_data_bigram_counter = {}
		sentence = line.split(" ")

		for i in range(1, len(sentence)):
			word1 = sentence[i-1]
			word2 = sentence[i]

			if(word1 == "+"):
				actual_list.append("+")
				continue
			elif(word1 == "-"):
				actual_list.append("-")
				continue

			if word2 in test_data_unigram_counter.keys():
				test_data_unigram_counter[word2] = str(int(test_data_unigram_counter[word2]) + 1)
			elif word2 not in test_data_unigram_counter.keys():
				test_data_unigram_counter[word2] = '1'

			if word1 in test_data_bigram_counter.keys():
				if word2 in test_data_bigram_counter[word1].keys():
					test_data_bigram_counter[word1][word2] = str(int(test_data_bigram_counter[word1][word2]) + 1)
				else:
					test_data_bigram_counter[word1][word2] = '1'
			else:
				test_data_bigram_counter[word1] = {}
				test_data_bigram_counter[word1][word2] = '1'

		
		positive_probability = math.log( float(pos_class)/(pos_class + neg_class))
		negative_probability = math.log( float(neg_class)/(pos_class + neg_class))

		for i in range(1, len(sentence)):
			word1 = sentence[i-1]
			word2 = sentence[i]
			if(word1 != "+" and word1 != "-"):
				bigram_flag = 0
				if(word1 in bigram_vocabulary.keys() and word1 in positive_class_prob_bigram.keys()):
					if(word2 in bigram_vocabulary[word1].keys() and word2 in positive_class_prob_bigram[word1].keys()):
						positive_probability += math.log(positive_class_prob_bigram[word1][word2])
						bigram_flag = 1
				'''
				if(bigram_flag == 0):
					if word2 in positive_class_prob_unigram.keys():
						positive_probability += math.log(positive_class_prob_unigram[word2])
					else:
						positive_probability += float(pos_add_one)
				'''
				bigram_flag = 0
				if(word1 in bigram_vocabulary.keys() and word1 in negative_class_prob_bigram.keys()):
					if(word2 in bigram_vocabulary[word1].keys() and word2 in negative_class_prob_bigram[word1].keys()):
						negative_probability += math.log(negative_class_prob_bigram[word1][word2])
						bigram_flag = 1
				'''
				if(bigram_flag == 0):
					if word2 in negative_class_prob_unigram.keys():
						negative_probability += math.log(negative_class_prob_unigram[word2])
					else:
						negative_probability += float(neg_add_one)
				'''
		if(positive_probability >= negative_probability):
			final_predicted_list.append("+")
		else:
			final_predicted_list.append("-")

	#print final_predicted_list

	hit_count = 0
	total_count = 0
	for i in range(0, len(actual_list)):
		if actual_list[i] == final_predicted_list[i]:
			hit_count += 1
			total_count += 1
		else:
			total_count += 1

	accuracy = float(hit_count)/total_count
	test_data.close()
	training_data.close()
	return accuracy

#the_actual_program()