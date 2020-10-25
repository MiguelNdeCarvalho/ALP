import re

def listWords(fileName):
    aux = []

    file = open(fileName,"r")
    content = file.read()
    debloated_char = re.sub(r'[^\w]', ' ', content)
    content_char = debloated_char.split()
    for string in content_char:
        if '"' in string:
            lower_string = string.lower()
            aux.append(lower_string.replace('"',''))
        else:
            aux.append(string.lower())
    return aux
