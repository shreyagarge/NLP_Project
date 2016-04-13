import operator
import pickle

def make_vocabulary():
	data = open('/home/utoniumharsha/HARSHA/NLP/NLP_Project/training_data.txt', 'r')
	vocabulary = open('/home/utoniumharsha/HARSHA/NLP/NLP_Project/bigram_vocabulary.txt', 'w')

	bigram_counter = {}
	final_list = {} # to store only those bigrams whose count >= 3

	for line in data:
		sentence = line.split(" ")
		for i in range(1, len(sentence)):
			word1 = sentence[i-1]
			word2 = sentence[i]
			if((word1 != "+" and word1 != "-" and word1 != "" and word1 != "\n") and (word2!= "+" and word2 != "-" and word2 != "" and word2 != "\n")):
				if word1 in bigram_counter.keys():
					if word2 in bigram_counter[word1].keys():
						bigram_counter[word1][word2] = str( int(bigram_counter[word1][word2]) + 1)
					else:
						bigram_counter[word1][word2] = '1'
				else:
					bigram_counter[word1] = {}
					bigram_counter[word1][word2] = '1'

	sorted_bigram_list = []
	for word1 in bigram_counter.keys():
		for word2 in bigram_counter[word1].keys():
			sorted_bigram_list.append([word1, word2, int(bigram_counter[word1][word2])])

	sorted_bigram_list.sort(key = lambda x: x[2], reverse = True)
	#print sorted_bigram_list

	
	counter = 0
	for each_tuple in sorted_bigram_list:
		if counter == 100:
			break
		counter += 1
		if(each_tuple[0] in final_list.keys()):
			final_list[each_tuple[0]][each_tuple[1]] = str(each_tuple[2])
		else:
			final_list[each_tuple[0]] = {}
			final_list[each_tuple[0]][each_tuple[1]] = str(each_tuple[2])

	#print final_list
	'''
	for word1 in bigram_counter.keys():
		#sorted_bigram_voc = sorted(bigram_counter[word1].items(), key = lambda x: int(operator.itemgetter(1)(x)), reverse=True) # sort according to decreasing word_count
		for word2 in bigram_counter[word1].keys():
			if int(bigram_counter[word1][word2]) >= 3:
				if word1 in final_list.keys():
					final_list[word1][word2] = bigram_counter[word1][word2]
				else:
					final_list[word1] = {}
					final_list[word1][word2] = bigram_counter[word1][word2]
	'''
	with open('bigram_vocabulary.pickle', 'wb') as handle:
		pickle.dump(final_list, handle)
	
make_vocabulary()