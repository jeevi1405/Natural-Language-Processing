# Initial tagging (default NOUN)
def initial_tagging(sentence):
    words = sentence.split()
    return [(word, "NOUN") for word in words]

# Apply transformation rules
def apply_rules(tagged_sentence):
    result = []

    for word, tag in tagged_sentence:
        if word.lower() in ["is", "am", "are", "was"]:
            tag = "VERB"
        elif word.endswith("ing"):
            tag = "VERB"
        elif word.lower() in ["quickly", "slowly"]:
            tag = "ADV"

        result.append((word, tag))

    return result

sentence = "He is running quickly"

initial = initial_tagging(sentence)
final = apply_rules(initial)

print("Initial:", initial)
print("Final:", final)
