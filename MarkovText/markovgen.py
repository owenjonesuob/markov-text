import random

class Markov(object):
    
    def __init__(self, text, tuple_size=3):
        self.text = text
        self.words = self.extract_words()
        self.tuple_size = tuple_size
        self.cache = {}
        self.build_cache()
        
    def extract_words(self):
        # Start at beginning of text file
        self.text.seek(0)
        # Read the file as a whole; split into list of words; return list
        return self.text.read().split()
    
    def tuples(self):
        for i in range(self.tuple_size-1, len(self.words)):
            # https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do-in-python
            yield (self.words[i-self.tuple_size+k] for k in range(1, self.tuple_size+1))
            
    def build_cache(self):
        for tup in self.tuples():
            # The first two words, as a tuple, are the key
            tup = list(tup)
            key = tuple(w for w in tup[:-1])
            if key in self.cache:
                # If the key's already there, add w3 to its list of values
                self.cache[key].append(tup[-1])
            else:
                # Otherwise add an entry to cache
                self.cache[key] = [tup[-1]]
                
    def generate_markov_text(self, length):
        # Choose a random pair of consecutive words to start
        seed = random.randint(0, len(self.words)-self.tuple_size)
        current = [self.words[seed+k] for k in range(0, self.tuple_size)]
        gen_words = []
        for i in range(length):
            gen_words.append(current.pop(0))
            current.append(random.choice(self.cache[tuple(current)]))
        gen_words.append(current[0])
        return " ".join(gen_words)