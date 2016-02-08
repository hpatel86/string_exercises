import sys

VOWELS = set(['a', 'e', 'i', 'o', 'u'])

def count_vowels_consonants(string):

	if not isinstance(string, basestring):
		raise TypeError('Input must be a string')

	vowels_count = dict(
		a=0,
		e=0,
		i=0,
		o=0,
		u=0
	)
	total_consonants = 0

	for char in string:
		if not char.isalpha():
			continue

		char_low = char.lower()
		if char_low in VOWELS:
			vowels_count[char_low] += 1

		else:
			total_consonants += 1

	return total_consonants, vowels_count


if __name__ == '__main__':
	stream = sys.stdin
	string_in  = sys.stdin.readline()

	total_consonants, vowels_count = count_vowels_consonants(string_in)

	print 'Total number of consonants: %s'%total_consonants
	print 'Vowels count:'
	print vowels_count

