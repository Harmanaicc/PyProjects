def rem(l, word):
    n = []
    for item in l:
        if item != word:
            n.append(item)
    return n

l = ["Harry", "Raman", "Subham", "Harman", "an"]

print(rem(l, "an"))