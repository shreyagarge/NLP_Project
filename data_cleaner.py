positive = open('/home/utoniumharsha/HARSHA/NLP/NLP_Project/positive.txt', 'r') 
negative = open('/home/utoniumharsha/HARSHA/NLP/NLP_Project/negative.txt', 'r')
stop_words = open('/home/utoniumharsha/HARSHA/NLP/NLP_Project/stopwords.txt', 'r')
final_data = open('/home/utoniumharsha/HARSHA/NLP/NLP_Project/cleaned_data.txt', 'w')

sw_list = stop_words.read().split()

for line in positive:
	final_data.write("+ ")
	sentence = line.split(" ")
	for word in sentence:
		new_word = ""
		for ch in word:
			if (ch <= 'z' and ch >='a'):
				new_word = new_word + ch
			elif (ch <= 'Z' and ch >= 'A'):
				new_word = new_word + chr(ord(ch)+32)
		if(not (new_word in sw_list)):
			if(new_word):
				new_word = new_word + " "
			final_data.write(new_word)
	final_data.write("\n")

for line in negative:
	final_data.write("- ")
	sentence = line.split(" ")
	for word in sentence:
		new_word = ""
		for ch in word:
			if (ch <= 'z' and ch >='a'):
				new_word = new_word + ch
			elif (ch <= 'Z' and ch >= 'A'):
				new_word = new_word + chr(ord(ch)+32)
		if(not new_word in sw_list):
			if(new_word):
				new_word = new_word + " "
			final_data.write(new_word)
	final_data.write("\n")