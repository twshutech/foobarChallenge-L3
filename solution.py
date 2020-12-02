import queue
from collections import defaultdict, deque
# from binarytree import build
class info:
  def right_wall(self, l):
    return len(l[0])-1
  def bottom_wall(self, l):
    return len(l)-1

class get_children_nodes:
  route = ([0,1],[1,0])
  def coming_node(coord):
    for x in route:
      yield zip(coord, x)

def next_node(parent, map_info):
  cQ = queue.Queue()
  node_children = get_children_nodes()
  yield node_children
  # for node in node_children:
  #   print 'node',node
  #   cQ.put(node)
  # yield cQ

def bfs(l, b):
  reversed_l = l.sort(reverse=True)

  information = info()
  q = queue.Queue()
  dQ = deque()

  parents_nodes = deque()
  children_nodes = []
  available_node = []
  blocked_node = []
  e = [information.right_wall(l), information.bottom_wall(l)]
  # print 'end point',e,l
  s = [0, 0]
  flag = False
  parents_nodes.append(s)
  cQ = next_node(s, information)
  for node in cQ:
    print 'node',node

  while len(list(parents_nodes)) > 0:
    s = parents_nodes.pop()

    if s == e: # Found the exit.
      flag = False
    else:
      next_column = s[0] + 1
      next_row = s[1] + 1
      if next_row < e[1]:
        if l[s[0]][next_row]:
          blocked_node.append([s[0],next_row])
        else:
          available_node.append([s[0],next_row])
        children_nodes.append([s[0],next_row])
      if next_column < e[0]:
        if l[next_column][s[1]]:
          blocked_node.append([next_column,s[1]])
        else:
          available_node.append([next_column,s[1]])
        children_nodes.append([next_column,s[1]])
      for child in children_nodes:
        parents_nodes.append(child)
        print 'parents_nodes',len(parents_nodes), child,parents_nodes
      del children_nodes[:]

def BFS(l, breakable):
  q = queue.Queue()
  for i,row in enumerate(l):
    for j,node in enumerate(l[i]):
      if node == 0:
        q.put([i,j])
  #print q.qsize()
  return list(q.queue)

def solution(l):
  breakable = True
  # print 'l',l
  return BFS(l,breakable)

def reverse_solution(l):
  breakable = True
  l.sort(reverse=True)
  for row in l:
    row.sort(reverse=False)
  # print 'l',l
  return BFS(l,breakable)

if __name__ == '__main__':
  to_null = lambda a:'X'
  empty_l = []
  l = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
  for row in l:
    empty_l.append(map(to_null, row))
  print 'empty_l',empty_l
  #bfs(l, True)

  #print answer([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])
  #solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])
  # print(solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))
  # print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))
  # print(reverse_solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))
  # print(reverse_solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))
  