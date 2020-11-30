from collections import deque

class basic_map_info():
  def __init__(self, m):
    self.horizontal_limit = len(m[0])
    self.vertical_limit = len(m)

def record_current(coord, m):
  m.popleft()
  m.appendleft("")
  return m

# def move(coord, m):
#   # move

class vertical_neighbor():
  def __init__(self, coord, v):
    if coord[1]-1 >= 0:
      self.up = v[coord[1]-1]
    else:
      self.up = 0
    if coord[1]+1 <= len(v):
      self.down = v[coord[1]+1]
    else:
      self.down = 0

class horizontal_neighbor():
  def __init__(self, coord, v):
    if coord[0]-1 >= 0:
      self.right = h[coord[1]-1]
    else:
      self.right = 0
    if coord[0]+1 <= len(v):
      self.left = v[coord[1]+1]
    else:
      self.left = 0

def node(coord, m):
  next_step = None
  h = horizontal_neighbor(coord, m[coord[1]])
  v = vertical_neighbor(coord, m[coord[0]])
  print h.left, h.right,v.up, v.down
  return [5, 5]
  # for p in [[coord[0], v.up], [coord[0], v.down], [h.left, coord[1]], [h.right, coord[1]]]:
  #   print p
    #print m[p[1], p[0]]
    # if m[p[1], p[0]]:
    #   next_step = p
    #   break


def solution(m):
  coord = node([0,0], m)
  path = deque()
  map_info = basic_map_info(m)
  while coord != [map_info.horizontal_limit, map_info.vertical_limit]:
    m = record_current(coord, m)
    coord = node(coord, m)

  # print '   1, 2, 3, 4, 5, 6'
  # for i, row in enumerate(m):
  #   print i+1, row
  
solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])
# print(solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))
# print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))
