def generated(word, alphabet, sep="_"):
    if sep == "":
        words = list(word)
    else:
        words = word.split(sep)

    for char in words:
        if char not in alphabet:
            return False
    return True


word = "a_b_color_b_a"
result = generated(word, set(["a", "b", "color"]))
print(result)
