from sklearn.cross_validation import KFold
from bigram_word_counter import make_bigram_counter_list
from bigram_vocabulator import make_vocabulary
from bigram_naive_bayes_classifier import bigram_classifier
from bigram_the_program import the_actual_program

from word_counter import make_word_counter_list
from naive_bayes_classifier import classifier

import numpy as np

if __name__ == "__main__":
	accuracy = []

	kf = KFold(1000, n_folds=10, shuffle=True)
	for train, test in kf:
		line_counter = 0
		train_pointer = 0
		test_pointer = 0
		np.append(train, "10000000")
		np.append(test, "10000000")
		print train.size, " ", test.size
		data = open('/home/utoniumharsha/HARSHA/NLP/NLP_Project/cleaned_data.txt', 'r')
		training = open('/home/utoniumharsha/HARSHA/NLP/NLP_Project/training_data.txt', 'w')
		testing = open('/home/utoniumharsha/HARSHA/NLP/NLP_Project/test_data.txt', 'w')
		for line in data:
			if (train_pointer < train.size):
				if(line_counter == train[train_pointer]):
					training.write(line)
					line_counter+=1
					train_pointer+=1
			if (test_pointer < test.size):
				if(line_counter == test[test_pointer]):
					testing.write(line)
					line_counter+=1
					test_pointer+=1

		make_word_counter_list()
		classifier()

		make_vocabulary()
		make_bigram_counter_list()
		bigram_classifier()
		accuracy.append(the_actual_program())
		

	final_accuracy = 0.0
	for ele in accuracy:
		final_accuracy += ele

	final_accuracy = float(final_accuracy)*10 #in percentage
	print final_accuracy
		
