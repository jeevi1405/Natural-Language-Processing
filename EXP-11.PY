# Top-Down Parser

grammar = {
    "S": [["a", "S", "b"], ["a", "b"]]
}

def parse(symbol, words):
    if not words:
        return False

    # If terminal
    if symbol not in grammar:
        return [words[1:]] if words and words[0] == symbol else []

    results = []
    for rule in grammar[symbol]:
        temp = [words]
        for sym in rule:
            new_temp = []
            for t in temp:
                new_temp += parse(sym, t)
            temp = new_temp
        results += temp
    return results

# Test
sentence = ["a", "a", "b", "b"]
result = parse("S", sentence)

print("Accepted" if [] in result else "Rejected")
