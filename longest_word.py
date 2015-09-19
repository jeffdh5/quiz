import sys

def load_data(fname, vocab=set()):
	# load raw data, assuming list of strings representing words, separated
	# by '\n'
	# make a set of words (your vocab) so you have O(1) lookup when you need to 
	# see if part of a string is inside the set of words.
	word_list = open(fname, "r").readlines()
	word_list = [w.strip() for w in word_list]
	word_set = set([w for w in word_list])
	return word_list, word_set

def is_valid_combo(word, vocab):
	# checks to see if the word is a valid combination of words in the vocabulary
	# assume that the word itself has already been removed when called at the
	# top level.
	c = 0
	if word == '':
		return True
	while c < len(word):
		if word[0:c+1] in vocab and is_valid_combo(word[c+1:], vocab):
			return True
		c += 1
	return False

def find_longest_combo(word_list, vocab):
	# iterate through your list of words, save the longest one that's
	# a combination of smaller words
	longest_word = ''
	longest_length = 0
	for word in word_list:
		vocab.remove(word)
		if is_valid_combo(word, vocab) and (len(word) > longest_length):
			longest_length = len(word)
			longest_word = word
		vocab.add(word)
	return longest_word


def tests():
	# some basic smoke tests, used for initial debugging
	testing_data = ['dog', 'cat', 'catdog']
	vocab = set(testing_data)
	print "Is valid combo? should be True, " + str(is_valid_combo('catdog', vocab))
	print("Found catdog is longest string? should be True, " + str(find_longest_combo(testing_data, vocab) == 'catdog'))


if len(sys.argv) > 1:
	fname = sys.argv[1]
	word_list, vocab = load_data(fname)
	print "The longest combo word in '" + fname + "': " + find_longest_combo(word_list, vocab)
else:
	load_data('word.list')

