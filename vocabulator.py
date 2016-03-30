import operator
import pickle
data = open('/home/utoniumharsha/HARSHA/NLP/NLP_Project/cleaned_data.txt', 'r')
vocabulary = open('/home/utoniumharsha/HARSHA/NLP/NLP_Project/vocabulary.txt', 'w')

word_counter = {}
final_list = {} # to store only those words whose count is at least 2

for line in data:
	sentence = line.split(" ")
	for word in sentence:
		if(word != "+" or word != "-"):
			if word in word_counter.keys():
				word_counter[word] = str( int(word_counter[word]) + 1)
			else:
				word_counter[word] = '1'

#sorted_voc = sorted(word_counter.items(), key=operator.itemgetter(1), reverse=True)
sorted_voc = sorted(word_counter.items(), key = lambda x: int(operator.itemgetter(1)(x)), reverse=True) # sort according to decreasing word_count

for row in sorted_voc:
	if(row[0] == "\n" or row[0] == "" or row[0] == " " or row[0] == "+" or row[0] == "-" or int(row[1]) < 2):
		continue
	else:
		final_list[row[0]] = row[1]
		vocabulary.write(row[0])
		vocabulary.write(" ")
		vocabulary.write(row[1])
		vocabulary.write("\n")

with open ('vocabulary.pickle', 'wb') as handle:
	pickle.dump(final_list, handle)