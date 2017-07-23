import markovgen, random

# www.gutenberg.org/cache/epub/29765/pg29765.txt

webster = open("C:/Users/Owen/Documents/Coding/PythonProjects/MarkovText/webster.txt")

markov = markovgen.Markov(webster, tuple_size=3)

text = markov.generate_markov_text(length=300)

print(text.replace(". ", ".\n"))