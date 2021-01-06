addNeg = lambda a,b:a-b
addPos = lambda a,b:a+b

def solution(m):
  # All maps' path length.
  shortest_path(m, len(m[0]), len(m))

def shortest_path(m, w, h):
  # Dict with steps as key, neibhors as properties.
  breadcrumbs = dict({1: {(0,0)}})
  print 'breadcrumbs:',breadcrumbs,'breadcrumbs',breadcrumbs.keys()
  # Dict with steps as key, non available cords of points as properties, init as null dict.
  breadcrumbs = dict()
  for rightnow in breadcrumbs[]:
    print 'rightnow',rightnow

  # for  in breadcrumbs[]:
  #   expectPath = [i for i in neighbors()]


def neighbors(x, m):
  i, j = x
  w, h = len(m[0]), len(m)
  candidates = {(i-1,j), (i+1,j), (i,j-1), (i,j+1)}
  candidatesbyadd = {(i+1,j), (i,j+1)}
  neighbors = set()
  for y in candidatesbyadd:
    i, j = y
    if i>=0 and i<h and j>=0 and j<w and m[i][j] == 0:
      neighbors.add(y)

  return neighbors

#print(solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))
print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))