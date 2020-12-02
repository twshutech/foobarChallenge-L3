from collections import deque
import queue
p = [(1, 3), (3, 0), (5, 4), (2, 1), (5, 1), (0, 3), (4, 0), (1, 2), (3, 3), (4, 4), (5, 0), (2, 2), (4, 1), (1, 1), (3, 2), (0, 4), (1, 4), (2, 3), (4, 2), (1, 0), (5, 3), (0, 1), (5, 2), (3, 1), (0, 2), (2, 0), (4, 3), (3, 4), (2, 4)]
l = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
# for location in p:
#   if l[location[0]][location[1]] == 0:
#     l[location[0]][location[1]] = "X"
lll = set()
lll.add('1')
print len(lll)
lll.add('1')
print len(lll)

for row in l:
  print row
# Return left then right child.
def get_children_nodes(x,y,xl,yl):
  if y+1 < yl:
    yield (x,y+1)
  if x+1 < xl:
    yield (x+1,y)

def BFS(m, s, e, el):
  set_l = set()
  Q = queue.Queue()
  #Take from left, giving from right.
  q = deque()
  #Insert start point.
  q.append(s)
  #Get coming children.
  count = 0
  while len(q)>0:
    # print 'q',q
    node = q.popleft()
    #print '--node--',node
    if el[node[0]][node[1]] == 'X':
      el[node[0]][node[1]] = count
      count+=1
    if node[0] != len(m[0]) and node[1] != len(m): #Current node isnt the exit.
      two_children = get_children_nodes(node[0], node[1],len(m[0]), len(m))
      for i in two_children:
        if i not in set_l:
          set_l.add(i)
          Q.put(i)
          q.append(i)

        if m[node[0]][node[1]] == 0:
          m[node[0]][node[1]] = '_'
  # print 'set_l',set_l,len(set_l)
  print 'Q',Q.queue
  # for row in el:
  #   print el
  # print 'm',m
  # for row in m:
  #   print row

if __name__ == '__main__':
  to_null = lambda a:'X'
  empty_l = []
  for row in l:
    empty_l.append(map(to_null, row))
  s = (0,0)
  e = (len(l[0]),len(l))
  BFS(l, s, e, empty_l)