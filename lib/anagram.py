class Anagram:
    def __init__(self, word):
        self.word = word
        self.sorted_word = sorted(self.word)
    
    def match(self, words):
        return [i for i in words if sorted (i.lower()) == self.sorted_word and i.lower() != self.word]