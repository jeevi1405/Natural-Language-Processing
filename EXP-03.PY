from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Input sentence
text = "The boys are playing football"

# Tokenization (split into words)
words = word_tokenize(text)

# Morphological Analysis (POS tagging)
tags = pos_tag(words)

# Display output
print("Input Sentence:", text)
print("Tokenized Words:", words)
print("POS Tags:", tags)
