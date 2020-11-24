def isRoot(n, delta):
    for path in delta:
        if (path[2] == n):
            return False
    return True

delta = [
  (0, "a", 1), (0, "b", 3),
  (1, "a", 3), (1, "b", 2),
  (2, "a", 2), (2, "b", 2),
  (3, "a", 3), (3, "b", 3)    ]

print(isRoot(2,delta))
