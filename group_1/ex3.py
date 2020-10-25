def alphabetFor(word, sep="_"):
    if sep == "":
        words = list(word)
    else:
        words = word.split(sep)

    alphabet = []

    for char in words:
        if char not in alphabet:
            alphabet.append(char)
    return alphabet


word = "a_b_color_b_a"
result = alphabetFor(word)
expected = set(["a", "b", "color"])
print(len(expected) == len(result) and expected == set(result))
