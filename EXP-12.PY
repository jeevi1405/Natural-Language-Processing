# Fixed Earley Parser

def earley(sentence):
    words = sentence.split()
    n = len(words)
    chart = [set() for _ in range(n+1)]

    # Use tuple instead of list
    chart[0].add(("S", ("a", "b"), 0, 0))

    for i in range(n+1):
        for state in list(chart[i]):
            lhs, rhs, dot, start = state

            # Scanner
            if dot < len(rhs) and i < n and rhs[dot] == words[i]:
                chart[i+1].add((lhs, rhs, dot+1, start))

            # Completion
            if dot == len(rhs):
                if lhs == "S" and start == 0:
                    return True

    return False

print(earley("a b"))
