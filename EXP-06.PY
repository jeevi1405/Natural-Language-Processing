import random

def build_bigram_model(text):
    words = text.split()
    bigram = {}

    for i in range(len(words)-1):
        key = words[i]
        next_word = words[i+1]

        if key not in bigram:
            bigram[key] = []
        bigram[key].append(next_word)

    return bigram

def generate_text(model, start_word, length=10):
    word = start_word
    result = [word]

    for _ in range(length-1):
        if word in model:
            word = random.choice(model[word])
            result.append(word)
        else:
            break

    return " ".join(result)

# Input text
text = "natural language processing is interesting and language processing is fun"

model = build_bigram_model(text)
print(generate_text(model, "language", 10))
