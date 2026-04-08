def pluralize(noun):
    # Rule-based FSM style
    if noun.endswith('y'):
        return noun[:-1] + 'ies'
    elif noun.endswith(('s', 'x', 'z', 'ch', 'sh')):
        return noun + 'es'
    else:
        return noun + 's'

# Test words
words = ["cat", "bus", "baby", "box", "dish"]

print("Plural Forms:")
for word in words:
    print(word, "->", pluralize(word))
