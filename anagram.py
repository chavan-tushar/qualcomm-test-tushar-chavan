
class Anagrams:
    def __init__(self):
        self.words = open('a.txt').readlines()
        self._similar_words = dict()
        self._create_similar_words_dict()
    
    def _create_similar_words_dict(self) -> None:
        self.words = list(dict.fromkeys(self.words))

        for word in self.words:
            word = word.strip().lower()
            sorted_word = self.get_sorted_word(word)
            if sorted_word in self._similar_words.keys():
                self._similar_words[self.get_sorted_word(word)].append(word)
            else:
                self._similar_words[self.get_sorted_word(word)] = [word]

    def get_anagrams(self, word: str) -> list[str] | str:
        if not word.isalpha():
            return f"Entered word '{word}' is not a correct word. Please enter a correct word!"
        
        word = self.get_sorted_word(word.strip().lower())

        return self._similar_words.get(word)

    def get_sorted_word(self, word: str) -> str:
        return "".join(sorted(list(word)))

# class Anagrams:
#     def __init__(self):
#         self.words = open('qualcomm-test-words.txt').readlines()


#     def get_anagrams(self, word: str) -> list[str] | str:
        
#         if not word.isalpha():
#             return f"Entered word '{word}' is not a correct word. Please enter a correct word!"
        
#         anagrams = []
#         word = word.lower().strip()

#         sorted_entered_word = self.get_sorted_word(word)
        
#         for current_word in self.words:
#             current_word = current_word.lower().strip()
#             if len(sorted_entered_word) != len(current_word):
#                 continue
            
#             sorted_word = self.get_sorted_word(current_word)
#             if sorted_word == sorted_entered_word:
#                 anagrams.append(current_word)

#         return anagrams

#     def get_sorted_word(self, word: str) -> str:
#         return "".join(sorted(list(word)))

if __name__ == "__main__":
    import time
    start_time = time.time()
    a = Anagrams()
    for i in range(100000):
        a.get_anagrams("ate")    
    
    end_time = time.time()
    print(f"Program took {end_time - start_time} to execute")