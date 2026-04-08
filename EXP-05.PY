from nltk.stem import PorterStemmer

# Create stemmer object
ps = PorterStemmer()

# List of words
words = ["running", "jumps", "easily", "flying", "studies"]

print("Stemming Results:")
for word in words:
    print(word, "->", ps.stem(word))
