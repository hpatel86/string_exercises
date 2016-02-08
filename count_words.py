import sys
import string
from collections import defaultdict


DELIMITER = " "
ALPHABET = set([
	'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
	'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
	'u', 'v', 'w', 'x', 'y', 'z'
])

def count_words(lines):
	word_count = defaultdict(int)

	for line in lines:
		word = ""
		for char in line:
			if char == DELIMITER:
				word_count[word] += 1
				word = ""

			else:
				char = char.lower()
				if char in ALPHABET:
					word += char

	if word != "":
		word_count[word] += 1

	return sorted(word_count.items(), key=lambda items: (-items[1], items[0]))


if __name__ == '__main__':
    stream = sys.stdin
    lines = sys.stdin.readlines()
    for word, count in count_words(lines):
        print word, count
