def generated(word, alphabet, sep="_"):
    if sep == "":
        chars = list(word)
        for char in chars:
            if char in alphabet:
                continue
            else:
                return False
        return True
    else:
        words = word.split(sep)
        for char in words:
            if char in alphabet:
                continue
            else:
                return False
        return True

word = "a_b_color_b_a"
result = generated(word, set(["a", "b", "color"]))
print(result)
