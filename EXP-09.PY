import re

def rule_based_tagger(sentence):
    words = sentence.split()
    tagged = []

    for word in words:
        if re.match(r'.*ing$', word):
            tag = "VERB"
        elif re.match(r'.*ed$', word):
            tag = "VERB"
        elif re.match(r'.*ly$', word):
            tag = "ADV"
        elif re.match(r'.*ous$', word):
            tag = "ADJ"
        else:
            tag = "NOUN"

        tagged.append((word, tag))

    return tagged

sentence = "He is running quickly and finished work"
print(rule_based_tagger(sentence))
