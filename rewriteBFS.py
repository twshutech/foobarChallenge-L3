from collections import deque
import queue, math
p = [(1, 3), (3, 0), (5, 4), (2, 1), (5, 1), (0, 3), (4, 0), (1, 2), (3, 3), (4, 4), (5, 0), (2, 2), (4, 1), (1, 1), (3, 2), (0, 4), (1, 4), (2, 3), (4, 2), (1, 0), (5, 3), (0, 1), (5, 2), (3, 1), (0, 2), (2, 0), (4, 3), (3, 4), (2, 4)]
l = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
joinStr = lambda a: str(a)
parent = lambda a: a-1
child = lambda a, b: a+b
# for location in p:
#   if l[location[0]][location[1]] == 0:
#     l[location[0]][location[1]] = "X"
graph = dict()
# for row in l:
#   print row
# print '\n'

def level(graph):
  range_is = int(math.log(len(graph), 2))
  level_graph = []
  current_level = 0
  for node in range(range_is):
    print pow(2,node)

def try_block(block_list):
  for bp in block_list:
    l[bp[0]][bp[1]] = '_'
    yield l

def reverse_travel(sequenceq, modified_list):
  new_path = []
  path = list(sequenceq) #list and reversed the path.
  start = (len(modified_list[0]), len(modified_list))
  # for direction in [(x,y+1),(x,y-1),(x-1,y),(x+1,y)]:
  #   if 0<=direction[0]<=len(modified_list[0]) and 0<=direction[1]<=len(modified_list):
  while len(path) > 0:
    node = path.pop()
    x = node[0]
    y = node[1]
    if modified_list[x][y] == '_':
      new_path.append(node)
  print 'path',path,'\n\n',new_path
  for row in modified_list:
    print row

  return new_path

# Return left then right child.
def get_children_nodes(x,y,xl,yl):
  if x+1 < xl:
    yield (x+1,y)
  if y+1 < yl:
    yield (x,y+1)

def BFS(m, s, e, el):
  set_l = set()
  block_list = set()
  Q = queue.Queue()
  #Take from left, giving from right.
  q = deque()
  #Insert start point.
  q.append(s)
  #Get coming children.
  count = 0
  while len(q)>0:
    # print 'length of Q is:',len(q),'contents',q.queue
    # print 'q',q
    node = q.popleft()
    #print '--node--',node
    if el[node[0]][node[1]] == 'X':
      el[node[0]][node[1]] = count
      if count == 0: 
        graph[count] = [] #Parents' children list.
      else:
        # print graph[abs(count-1)] 
        if graph[abs(count-1)] or graph[abs(count-2)] :
          graph[count] = [] #Parents' children list.
        elif count not in graph[count-1]:
          graph[count] = [count-1] #Append parent to self list.
        elif count not in graph[count-2]:
          graph[count-2] = [count-2] #Append parent to self list.
      count+=1
    if node[0] != len(m[0]) and node[1] != len(m): #Current node isnt the exit.
      two_children = get_children_nodes(node[0], node[1],len(m[0]), len(m))
      for n,i in enumerate(two_children):
        graph[parent(count)].append(child(count, n)) #Append child to list.
        if i not in set_l:
          set_l.add(i)
          Q.put(i)
          q.append(i)

    if m[node[0]][node[1]] == 0:
      m[node[0]][node[1]] = '_'
    else:
      block_list.add(node)
        # else:
        #   m[node[0]][node[1]] = '|'
      # print 'count',count
      # print 'graph[',parent(count),']',graph[parent(count)]
  #print 'block list:',sorted(block_list),'\nnew map',try_block(sorted(block_list)).next()
  # for bp in range(len(sorted(block_list))):
  new_map = try_block(sorted(block_list)).next()
  # reverse_travel(Q.queue, new_map)
  #print 'set_l',sorted(set_l),len(set_l),'\n'
  #print 'Q',Q.queue, Q.qsize(),'\n'
  print len(graph),'graph',graph,'\n', level(graph)
  for row in el:
    print row
  # print 'm',m
  for row in m:
  #   row = map(joinStr, row)
  #   row = "".join(row)
    print row

if __name__ == '__main__':
  to_null = lambda a:'X'
  empty_l = []
  for row in l:
    empty_l.append(map(to_null, row))
  s = (0,0)
  e = (len(l[0]),len(l))
  BFS(l, s, e, empty_l)
