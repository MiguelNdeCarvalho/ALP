def areNeighbours(pos_ini, pos_fin, delta):
    for path in delta:
        if {path[0], path[2]} == {pos_ini, pos_fin}:
            return True
    return False


#delta = [
#  (0, "a", 1), (0, "b", 3),
#  (1, "a", 3), (1, "b", 2),
#  (2, "a", 2), (2, "b", 2),
#  (3, "a", 3), (3, "b", 3)    ]
#print(areNeighbours(0, 1, delta) and not areNeighbours(3, 2, delta))

delta = [
  (0, "a", 1), (0, "b", 3),
  (1, "a", 3), (1, "b", 2),
  (2, "a", 2), (2, "b", 2),
  (3, "a", 3), (3, "b", 3)    ]
print(areNeighbours(0, 3, delta) and not areNeighbours(0, 2, delta))
