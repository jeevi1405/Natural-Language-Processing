# Simple PCFG

grammar = {
    "NP": {"She": 0.5, "He": 0.5},
    "VP": {"runs": 0.6, "eats": 0.4}
}

def pcfg(sentence):
    words = sentence.split()
    prob = 1.0

    for w in words:
        for rule in grammar:
            if w in grammar[rule]:
                prob *= grammar[rule][w]

    return prob

print("Probability:", pcfg("She runs"))
