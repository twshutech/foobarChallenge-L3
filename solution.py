from collections import deque
class basic_map_info:
  def __init__(self, m):
    self.horizontal_limit = len(m[0])-1
    self.vertical_limit = len(m)-1
    self.graph = m

class vertical_neighbor:
  def __init__(self, coord, map_info):
    if coord[1] == 0:
      self.top = None
    else:
      self.top = map_info[coord[0]][coord[1]-1]
    if coord[1] == len(map_info)-1:
      self.down = None
    else:
      self.down = map_info[coord[0]][coord[1]+1]
    self.up = coord[1]-1
    self.low = coord[1]+1
    #print 'c',coord,'map_info',map_info

class horizontal_neighbor:
  def __init__(self, coord, map_info):
    if coord[0] == 0:
      self.left = None
    else:
      self.left = map_info.graph[coord[0]-1][coord[1]]
    if coord[0] == map_info.horizontal_limit:
      self.right = None
      print self.right,self.left
    else:
      self.rignt = map_info.graph[coord[0]+1][coord[1]]
      print '12345',map_info.graph[coord[0]+1][coord[1]]

def record_current(coord, map_info, path):
  path.append(coord)
  map_info.graph[coord[1]][coord[0]] = None
  # m.popleft()
  # m.appendleft("")
  return map_info.graph

# def move(coord, m):
#   # move
def node(coord, m):
  next_step = coord
  h = horizontal_neighbor(coord, m)
  v = vertical_neighbor(coord, m.graph)
  print 'v',v.top,v.down,'h',h.right,h.left
  # for p in [[coord[0], v.top], [coord[0], v.down], [h.left, coord[1]], [h.right, coord[1]]]:
  #   print p
  #   print 'm[p[1]][p[0]]',m[p[1]][p[0]]
  #   if m[p[1]][p[0]]:
  #     next_step = p
  #     break
  return next_step

def solution(m):
  map_info = basic_map_info(m)
  coord = node([0,0], map_info)
  path = deque()
  while coord != [map_info.horizontal_limit, map_info.vertical_limit]:
    m = record_current(coord, map_info, path)
    coord = node(coord, map_info).reverse()

  # print '   1, 2, 3, 4, 5, 6'
  # for i, row in enumerate(m):
  #   print i+1, row
  
solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])
# print(solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))
# print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))
