import random

# Training data (word, tag)
train_data = [
    ("I", "PRON"), ("like", "VERB"), ("python", "NOUN"),
    ("I", "PRON"), ("like", "VERB"), ("coding", "NOUN"),
    ("coding", "NOUN"), ("is", "VERB"), ("fun", "ADJ")
]

# Build probability model
model = {}

for word, tag in train_data:
    if word not in model:
        model[word] = {}
    if tag not in model[word]:
        model[word][tag] = 0
    model[word][tag] += 1

# Convert to probabilities
for word in model:
    total = sum(model[word].values())
    for tag in model[word]:
        model[word][tag] /= total

# Tagging function
def stochastic_tagger(sentence):
    words = sentence.split()
    tagged = []

    for word in words:
        if word in model:
            tags = list(model[word].keys())
            probs = list(model[word].values())
            tag = random.choices(tags, probs)[0]
        else:
            tag = "UNK"
        tagged.append((word, tag))

    return tagged

print(stochastic_tagger("I like coding"))
