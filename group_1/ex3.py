def alphabetFor(word, sep="_"):
    alphabet = []
    if sep == "":
        words = list(word)
        for char in words:
            if char in alphabet:
                continue
            else:
                alphabet.append(char)
    else:
        words = word.split(sep)
        for char in words:
            if char in alphabet:
                continue
            else:
                alphabet.append(char)
    return alphabet


word = "a_b_color_b_a"
result = alphabetFor(word)
expected = set(["a", "b", "color"])
print(len(expected) == len(result) and expected == set(result))
