import queue
from collections import defaultdict
class info:
  def right_wall(self, l):
    return len(l[0])
  def bottom_wall(self, l):
    return len(l)

def bfs(l, b, el):
  blocked_node_neibhor = defaultdict()
  reversed_l = l.sort(reverse=True)
  information = info()
  q = queue.Queue()
  children_nodes = []
  available_node = []
  blocked_node = []
  e = [information.right_wall(l), information.bottom_wall(l)]
  # print 'end point',e,l
  s = [0, 0]
  flag = False
  children_nodes.append(s)
  # print 'ee',e
  while flag != True:
    if len(children_nodes)>0:
      print 'children_nodes',children_nodes
    # for i,s in enumerate(children_nodes):
    while len(children_nodes) > 0:
      s = children_nodes.pop()
      # print 's',s
      if s == e:
        flag = True
      else:
        # for i,x_then_y in enumerate(s):
        #   print 'x_then_y',x_then_y,i

        next_column = s[0] + 1
        next_row = s[1] + 1
        print s,'from',((next_column,s[1]), (s[0],next_row))
        # if len(children_nodes)>0 and i == 0:
        #   del children_nodes[:]
        if next_row < e[1]:
          if l[s[0]][next_row]:
            blocked_node.append([s[0],next_row])
            # if blocked_node_neibhor[','.join(str(n) for n in s)]:
            #   blocked_node_neibhor[','.join(str(n) for n in s)].append(','.join([s[0],next_row]))
            # else:
            #   blocked_node_neibhor[','.join(str(n) for n in s)] = [','.join([s[0],next_row])]
          else:
            available_node.append([s[0],next_row])
          children_nodes.append([s[0],next_row])
        if next_column < e[0]:
          if l[next_column][s[1]]:
            blocked_node.append([next_column,s[1]])
            # if blocked_node_neibhor[','.join(str(n) for n in s)]:
            #   blocked_node_neibhor[','.join(str(n) for n in s)].append(','.join([next_column,s[1]]))
            # else:
            #   blocked_node_neibhor[','.join(str(n) for n in s)] = [','.join([next_column,s[1]])]
          else:
            available_node.append([next_column,s[1]])
          children_nodes.append([next_column,s[1]])
        # print 'children_nodes',children_nodes
        # print 'blocked_node',blocked_node
        # print 'available_node',available_node
      q.put(s)
      # print 'q',list(q.queue),s

def wall_to_exit(w, l):
  print '~~~w',w,'l',l

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
  empty_l = []
  l = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
  for row in l:
    empty_l.append(['_' for i in range(len(row))])
    print row
  for initNode in empty_l:
    print initNode
  # way_go_path = solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])
  # way_back_path = reverse_solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])
  # print 'go', way_go_path
  # print 'back', way_back_path
  bfs(l, True, empty_l)


  #print answer([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])
  #solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])
  # print(solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))
  # print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))
  # print(reverse_solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))
  # print(reverse_solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))
  