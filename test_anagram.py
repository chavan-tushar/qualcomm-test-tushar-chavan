import unittest, anagram

class TestAnagram(unittest.TestCase):
    def test_get_anagram(self):
        anagrams = anagram.Anagrams()
        self.assertEqual(anagrams.get_anagrams('plates'), ['palest', 'pastel', 'petals', 'plates', 'staple'])
        self.assertEqual(anagrams.get_anagrams('eat'), ['ate', 'eat', 'tea'])
        self.assertEqual(anagrams.get_anagrams('x'), None)

if __name__ == "__main__":
    unittest.main()