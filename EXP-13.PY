# Subject-Verb Agreement

def check(sentence):
    words = sentence.split()

    if len(words) < 2:
        return False

    subject = words[0]
    verb = words[1]

    if subject in ["He", "She", "It"] and verb.endswith("s"):
        return True
    elif subject in ["They", "We", "I"] and not verb.endswith("s"):
        return True
    else:
        return False

print(check("He runs"))     # True
print(check("They runs"))   # False
