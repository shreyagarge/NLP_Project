import pickle
import math

def the_actual_program():

	test_data = open('/home/utoniumharsha/HARSHA/NLP/NLP_Project/test_data.txt', 'r')
	training_data = open('/home/utoniumharsha/HARSHA/NLP/NLP_Project/training_data.txt', 'r')

	vocabulary = {}
	positive = {}
	negative = {}
	positive_class_prob = {}
	negative_class_prob = {}
	actual_list = []

	with open('vocabulary.pickle', 'rb') as handle:
		vocabulary = pickle.load(handle)

	with open('positive_words_count.pickle', 'rb') as handle:
		positive = pickle.load(handle)

	with open('negative_words_count.pickle', 'rb') as handle:
		negative = pickle.load(handle)

	with open('nbayes_positive_prob.pickle', 'rb') as handle:
		positive_class_prob = pickle.load(handle)

	with open('nbayes_negative_prob.pickle', 'rb') as handle:
		negative_class_prob = pickle.load(handle)

	pos_class = 0
	neg_class = 0

	V = len(vocabulary)
	Count_Positive = 0
	Count_Negative = 0

	for key in positive:
		Count_Positive += int(positive[key])

	for key in negative:
		Count_Negative += int(negative[key])

	for line in training_data:
		sentence = line.split(" ")
		if sentence[0] == "+":
			pos_class += 1
		elif sentence[0] == "-":
			neg_class += 1

	print "positive_classes = ", pos_class
	print "negative_classes = ", neg_class

	pos_add_one = math.log(1.0/(Count_Positive + V))
	neg_add_one = math.log(1.0/(Count_Negative + V))

	final_predicted_list = []

	for line in test_data:
		test_data_word_counter = {} # for each review in the test data, classification has to be made 
		sentence = line.split(" ")
		for word in sentence:
			if (word == "+"):
				actual_list.append("+")
			elif (word == "-"):
				actual_list.append("-")
			if word in test_data_word_counter.keys():
				test_data_word_counter[word] = str(int(test_data_word_counter[word]) + 1)
			elif word not in test_data_word_counter.keys():
				test_data_word_counter[word] = '1'

		positive_probability = math.log (float(pos_class)/(pos_class + neg_class))
		negative_probability = math.log (float(neg_class)/(pos_class + neg_class))

		for key in test_data_word_counter:
			if key in positive.keys():
				positive_probability += float(test_data_word_counter[key]) * math.log(positive_class_prob[key])
			else:
				positive_probability += float(test_data_word_counter[key]) * pos_add_one

		for key in test_data_word_counter:
			if key in negative.keys():
				negative_probability += float(test_data_word_counter[key]) * math.log(negative_class_prob[key])
			else:
				negative_probability += float(test_data_word_counter[key]) * neg_add_one

		if positive_probability >= negative_probability :
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
	return accuracy