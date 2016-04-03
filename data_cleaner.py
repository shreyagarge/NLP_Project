positive = open('/home/utoniumharsha/HARSHA/NLP/NLP_Project/positive.txt', 'r') 
negative = open('/home/utoniumharsha/HARSHA/NLP/NLP_Project/negative.txt', 'r')
stop_words = open('/home/utoniumharsha/HARSHA/NLP/NLP_Project/stopwords.txt', 'r')
final_data = open('/home/utoniumharsha/HARSHA/NLP/NLP_Project/cleaned_data.txt', 'w')

import nltk
from math import log

# Build a cost dictionary, assuming Zipf's law and cost = -math.log(probability).
words = open("list_of_english_words.txt").read().split()
wordcost = dict((k, log((i+1)*log(len(words)))) for i,k in enumerate(words))
maxword = max(len(x) for x in words)

def infer_spaces(s):
    """Uses dynamic programming to infer the location of spaces in a string
    without spaces."""

    # Find the best match for the i first characters, assuming cost has
    # been built for the i-1 first characters.
    # Returns a pair (match_cost, match_length).
    def best_match(i):
        candidates = enumerate(reversed(cost[max(0, i-maxword):i]))
        return min((c + wordcost.get(s[i-k-1:i], 9e999), k+1) for k,c in candidates)

    # Build the cost array.
    cost = [0]
    for i in range(1,len(s)+1):
        c,k = best_match(i)
        cost.append(c)

    # Backtrack to recover the minimal-cost string.
    out = []
    i = len(s)
    while i>0:
        c,k = best_match(i)
        assert c == cost[i]
        out.append(s[i-k:i])
        i -= k

    return " ".join(reversed(out))

if __name__ == "__main__":
	sno = nltk.stem.SnowballStemmer('english') #Snowball stemmer for stemming words

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
				if(len(new_word) > 2 and (new_word[0] == new_word[1] == new_word[2] == 'w')):
					continue
				if(len(new_word) > 13):
					new_word = infer_spaces(new_word)
				for each_word in new_word.split(" "):
					final_data.write(str(sno.stem(each_word)))
					final_data.write(" ")
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
				if(len(new_word) > 2 and (new_word[0] == new_word[1] == new_word[2] == 'w')):
					continue
				if(len(new_word) > 13):
					new_word = infer_spaces(new_word)
				for each_word in new_word.split(" "):
					final_data.write(str(sno.stem(each_word)))
					final_data.write(" ")
		final_data.write("\n")