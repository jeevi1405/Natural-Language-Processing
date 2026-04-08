def ends_with_ab(string):
    state = 0

    for char in string:
        if state == 0:
            if char == 'a':
                state = 1
            else:
                state = 0

        elif state == 1:
            if char == 'b':
                state = 2
            elif char == 'a':
                state = 1
            else:
                state = 0

        elif state == 2:
            if char == 'a':
                state = 1
            else:
                state = 0

    if state == 2:
        return "Accepted (ends with 'ab')"
    else:
        return "Rejected"

# Test
print(ends_with_ab("aab"))   # Accepted
print(ends_with_ab("aba"))   # Rejected
