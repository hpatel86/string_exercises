import unittest

from count_vowels_consonants import count_vowels_consonants

class TestCountVowelsConsenants(unittest.TestCase):

	def test_none_type_input(self):
		string = None
		self.assertRaises(TypeError, lambda: count_vowels_consonants(string))


	def test_list_type_input(self):
		string = ['hello', 'world', 'foo', 'bar']
		self.assertRaises(TypeError, lambda: count_vowels_consonants(string))


	def test_empty_string_input(self):
		string = ''
		expected_total_consonants = 0
		expected_vowels_count = dict(
			a=0,
			e=0,
			i=0,
			o=0,
			u=0
		)

		total_consonants, vowels_count = count_vowels_consonants(string)

		self.assertEqual(expected_total_consonants, total_consonants)
		self.assertDictEqual(expected_vowels_count, vowels_count)


	def test_vowel_string_lowercase(self):
		string = 'aeiouaeiouae'
		expected_total_consonants = 0
		expected_vowels_count = dict(
			a=3,
			e=3,
			i=2,
			o=2,
			u=2,
		)

		total_consonants, vowels_count = count_vowels_consonants(string)

		self.assertEqual(expected_total_consonants, total_consonants)
		self.assertDictEqual(expected_vowels_count, vowels_count)


	def test_vowel_string_uppercase(self):
		string = 'AEIOUAEIOUAOIUEOI'
		expected_total_consonants = 0
		expected_vowels_count = dict(
			a=3,
			e=3,
			i=4,
			o=4,
			u=3
		)

		total_consonants, vowels_count = count_vowels_consonants(string)

		self.assertEqual(expected_total_consonants, total_consonants)
		self.assertDictEqual(expected_vowels_count, vowels_count)


	def test_vowel_string_mixedcase(self):
		string = 'aeIOUAEiouiouea'
		expected_total_consonants = 0
		expected_vowels_count = dict(
			a=3,
			e=3,
			i=3,
			o=3,
			u=3
		)

		total_consonants, vowels_count = count_vowels_consonants(string)

		self.assertEqual(expected_total_consonants, total_consonants)
		self.assertDictEqual(expected_vowels_count, vowels_count)


	def test_string_no_vowels_lowercase(self):
		string = 'dfhnbvmdd'
		expected_total_consonants = len(string)
		expected_vowels_count = dict(
			a=0,
			e=0,
			i=0,
			o=0,
			u=0,
		)

		total_consonants, vowels_count = count_vowels_consonants(string)

		self.assertEqual(expected_total_consonants, total_consonants)
		self.assertDictEqual(expected_vowels_count, vowels_count)


	def test_string_no_vowels_uppercase(self):
		string = 'DFGHNMDTRDS'
		expected_total_consonants = len(string)
		expected_vowels_count = dict(
			a=0,
			e=0,
			i=0,
			o=0,
			u=0,
		)

		total_consonants, vowels_count = count_vowels_consonants(string)

		self.assertEqual(expected_total_consonants, total_consonants)
		self.assertDictEqual(expected_vowels_count, vowels_count)


	def test_string_no_vowels_mixedcase(self):
		string = 'mnDNNHfgWms'
		expected_total_consonants = len(string)
		expected_vowels_count = dict(
			a=0,
			e=0,
			i=0,
			o=0,
			u=0,
		)

		total_consonants, vowels_count = count_vowels_consonants(string)

		self.assertEqual(expected_total_consonants, total_consonants)
		self.assertDictEqual(expected_vowels_count, vowels_count)


	def test_string_mixed_vowels_consonants_lowercase(self):
		string = 'mnadrufsadopiedfaf'
		expected_vowels_count = dict(
			a=3,
			e=1,
			i=1,
			o=1,
			u=1
		)
		expected_total_consonants = 11

		total_consonants, vowels_count = count_vowels_consonants(string)

		self.assertEqual(expected_total_consonants, total_consonants)
		self.assertDictEqual(expected_vowels_count, vowels_count)


	def test_string_mixed_vowels_consonants_uppercase(self):
		string = 'mnadrufsadopiedfaf'.upper()
		expected_vowels_count = dict(
			a=3,
			e=1,
			i=1,
			o=1,
			u=1,
		)
		expected_total_consonants = 11

		total_consonants, vowels_count = count_vowels_consonants(string)

		self.assertEqual(expected_total_consonants, total_consonants)
		self.assertDictEqual(expected_vowels_count, vowels_count)


	def test_string_mixed_vowels_consonants_mixedcase(self):
		string = 'mNaDrufsAdOpiEdIff'
		expected_vowels_count = dict(
			a=2,
			e=1,
			i=2,
			o=1,
			u=1
		)
		expected_total_consonants = 11

		total_consonants, vowels_count = count_vowels_consonants(string)

		self.assertEqual(expected_total_consonants, total_consonants)
		self.assertDictEqual(expected_vowels_count, vowels_count)


	def test_string_mixed_vowels_consonants_mixedcase_special_chars(self):
		string = 'mNaDrufsAdOpiEdIff@?+'
		expected_vowels_count = dict(
			a=2,
			e=1,
			i=2,
			o=1,
			u=1
		)
		expected_total_consonants = 11

		total_consonants, vowels_count = count_vowels_consonants(string)

		self.assertEqual(expected_total_consonants, total_consonants)
		self.assertDictEqual(expected_vowels_count, vowels_count)


	def test_string_mixed_vowels_consonants_uppercase_special_chars(self):
		string = 'mNaDrufsAdOpiEdIff@?+'.upper()
		expected_vowels_count = dict(
			a=2,
			e=1,
			i=2,
			o=1,
			u=1
		)

		expected_total_consonants = 11

		total_consonants, vowels_count = count_vowels_consonants(string)

		self.assertEqual(expected_total_consonants, total_consonants)
		self.assertDictEqual(expected_vowels_count, vowels_count)


	def test_string_mixed_vowels_consonants_lowercase_special_chars(self):
		string = 'mNaDru fsAd OpiEdIff@?+'.lower()
		expected_vowels_count = dict(
			a=2,
			e=1,
			i=2,
			o=1,
			u=1
		)

		expected_total_consonants = 11

		total_consonants, vowels_count = count_vowels_consonants(string)

		self.assertEqual(expected_total_consonants, total_consonants)
		self.assertDictEqual(expected_vowels_count, vowels_count)


	def test_string_mixed_vowels_consonants_lowercase_numbers(self):
		string = 'mNaDrufsAdOpiEdIff12312321'.lower()
		expected_vowels_count = dict(
			a=2,
			e=1,
			i=2,
			o=1,
			u=1
		)
		expected_total_consonants = 11

		total_consonants, vowels_count = count_vowels_consonants(string)

		self.assertEqual(expected_total_consonants, total_consonants)
		self.assertDictEqual(expected_vowels_count, vowels_count)


	def test_string_mixed_vowels_consonants_mixedcase_numbers_special_chars(self):
		string = 'mNaDru$%/ fsAdOpi EdIf FI1231 2321)\"'
		expected_vowels_count = dict(
			a=2,
			e=1,
			i=3,
			o=1,
			u=1
		)
		expected_total_consonants = 11

		total_consonants, vowels_count = count_vowels_consonants(string)

		self.assertEqual(expected_total_consonants, total_consonants)
		self.assertDictEqual(expected_vowels_count, vowels_count)


	def test_string_mixed_vowels_consonants_mixedcase_numbers_special_chars_unicode(self):
		string = u'mNaDru$%/ fsAdOpi EdIf FI1231 2321)\"'
		expected_vowels_count = dict(
			a=2,
			e=1,
			i=3,
			o=1,
			u=1
		)
		expected_total_consonants = 11

		total_consonants, vowels_count = count_vowels_consonants(string)

		self.assertEqual(expected_total_consonants, total_consonants)
		self.assertDictEqual(expected_vowels_count, vowels_count)



def main():
	unittest.main()


if __name__ == '__main__':
	main()
