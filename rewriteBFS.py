from collections import deque
import queue

class coord:
  def __init__(self, x, y):
    self.x = x
    self.y = y

# Return left then right child.
class get_children_nodes:
  q = queue.Queue()
  def children(self, x, y, q):
    next_coord_y = coord(x,y+1)
    next_coord_x = coord(x+1,y)
    print 'next_coord_x',next_coord_x,'next_coord_y',next_coord_y
    q.put(next_coord_y)
    q.put(next_coord_x)
    return self.q

def BFS(m, s, e, el):
  #Take from left, giving from right.
  q = deque()
  #Insert start point.
  q.append(s)
  #Get coming children.
  c = get_children_nodes()

  while len(q)>0:
    node = q.popleft()
    two_children = c.children(node.x, node.y)
    xxx = two_children.queue
    
    print 'two_children',xxx

if __name__ == '__main__':
  to_null = lambda a:'X'
  empty_l = []
  l = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
  for row in l:
    empty_l.append(map(to_null, row))
  print 'empty_l'
  s = coord(0,0)
  e = coord(len(l[0]),len(l))
  BFS(l, s, e, empty_l)