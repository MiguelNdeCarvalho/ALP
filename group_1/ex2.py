def symbolsIn(word, sep="_"):
    if sep == "":
        return (list(word))
    else:
        return word.split(sep)
