def controls(delta):
    aux = set()
    for path in delta:
        if path[0] in aux:
            continue
        else:
            aux.add(path[0])
    return aux

delta = [
  (0, "a", 1), (0, "b", 3),
  (1, "a", 3), (1, "b", 2),
  (2, "a", 2), (2, "b", 2),
  (3, "a", 3), (3, "b", 3)    ]
print(controls(delta) == {0, 1, 2, 3})
