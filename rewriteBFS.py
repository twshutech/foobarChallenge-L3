from collections import deque
import queue, math
p = [(1, 3), (3, 0), (5, 4), (2, 1), (5, 1), (0, 3), (4, 0), (1, 2), (3, 3), (4, 4), (5, 0), (2, 2), (4, 1), (1, 1), (3, 2), (0, 4), (1, 4), (2, 3), (4, 2), (1, 0), (5, 3), (0, 1), (5, 2), (3, 1), (0, 2), (2, 0), (4, 3), (3, 4), (2, 4)]
l = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
maze = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
joinStr = lambda a: str(a)
parent = lambda a,b: a-1
child = lambda a, b: a+b
# for location in p:
#   if l[location[0]][location[1]] == 0:
#     l[location[0]][location[1]] = "X"
graph = dict()
neighbors_dict = dict()
# for row in l:
#   print row
# print '\n'

def gendict(newmap):
  levelNum = 1
  path = [(0,0)]
  # print node,'neibhor', neighbors(node, maze)
  while len(newmap)>0:
    this_level = []
    for child in range(pow(2,levelNum)):
      if len(newmap)>0:
        this_level.append(newmap.pop())
    path.append(this_level)
    levelNum+=1
  # for level_tree in path:
  #   print level_tree

def level(graph):
  range_is = int(math.log(len(graph), 2))
  level_graph = []
  current_level = 0
  for node in range(range_is):
    print pow(2,node)

def try_block(bp=(0,0), l=[]):
  clone = [[col for col in row] for row in l]
  if bp != (0,0):
    clone[bp[0]][bp[1]] = 0
    return clone

def reverse_travel(sequenceq, modified_list):
  # print 'modified_list',modified_list
  # for i in modified_list:
  #   print i
  new_path = []
  path = list(sequenceq) #list and reversed the path.
  # print path
  start = (len(modified_list[0]), len(modified_list))
  # for direction in [(x,y+1),(x,y-1),(x-1,y),(x+1,y)]:
  #   if 0<=direction[0]<=len(modified_list[0]) and 0<=direction[1]<=len(modified_list):
  while len(path) > 0:
    node = path.pop()
    # print 'node', node
    x = node[0]
    y = node[1]
    if modified_list[x][y] == 0:
      new_path.append(node)
      # if x == 0 and y == 1:
      #   print '10',modified_list[x][y],'new_path',new_path
  print len(neighbors_dict)

  #print 'path',path,'\n\n',sorted(new_path, reverse=False)
  # for row in modified_list:
  #   print row
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
    #neighbors_dict[','.join([str(a) for a in node])] = neighbors(node, maze)

    # if node == e:
    #   Q.put(node)
    # print '--node--',node, 'l[node[0]][node[1]]',l[node[0]][node[1]],'node[0]',node[0],'node[1]',node[1],'count',count
    if l[node[0]][node[1]] == 0:
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
        if count != 0:
          graph[parent(count,i)].append(child(count, n)) #Append child to list.
        if i not in set_l:
          set_l.add(i)
          Q.put(i)
        if i == e:
          q.clear()
        else:
          q.append(i)
    if m[node[0]][node[1]] == 1:
      block_list.add(node)

  level(graph)
  for node in block_list:
    new_map = try_block(node, l)
    # for new_path in new_map:
    #   gendict(reverse_travel(Q.queue, new_path))

  print len(neighbors_dict)
  for i,key in enumerate(neighbors_dict.keys()):
    v = neighbors_dict.values()
    print  'key',key,':',v[i]
  # block_list = sorted(block_list)
  # print 'block_list',block_list[2]
  # for index,bp in block_list:
  #   print index,',',bp
    
      # print 'graph[',parent(count),']',graph[parent(count)]
  #print 'block list:',sorted(block_list),'\nnew map',try_block(sorted(block_list)).next()

  #print 'set_l',sorted(set_l),len(set_l),'\n'
  #print 'Q',Q.queue, Q.qsize(),'\n'
  # for row in el:
  #   print row
  # print 'm',m
  # for row in m:
  #   row = map(joinStr, row)
  #   row = "".join(row)
    # print row

def scantheone(l):
  for y,row in enumerate(l):
    for x,col in enumerate(row):
      if col == 1:
        yield (x,y)

def keep_trying(l):
  shortest = 0
  # while 
  #   new_map = try_block(block_point.next(), l)

  # while len(neighbors_dict) > len(l)+len(l[0])-1 or len(neighbors_dict) == 0:
  #   block_point = scantheone(l)
  #   if len(neighbors_dict) != 0:
  #   else:
  #     new_map = l
    

def runrun(new_map):  
  for y,row in enumerate(new_map):
    for x,col in enumerate(row):
      node = (x, y)
      neighbors_dict[','.join([str(a) for a in node])] = neighbors(node, new_map)
  return len(neighbors_dict)


def neighbors(x, m):
  
    '''Returns a set of nodes (as tuples) that are neighbors of node x in m.'''
    i, j = x
    w, h = len(m[0]), len(m)
    candidates = {(i-1,j), (i+1,j), (i,j-1), (i,j+1)}
    neighbors = set()
    for y in candidates:
        i, j = y
        if i>=0 and i<h and j>=0 and j<w and m[i][j] == 0:
            neighbors.add(y)
    
    return neighbors
if __name__ == '__main__':
  to_null = lambda a:'X'
  empty_l = []
  for row in l:
    empty_l.append(map(to_null, row))
  s = (0,0)
  e = (len(l[0])-1,len(l)-1)
  BFS(l, s, e, empty_l)

def getoneinlist(list):
  i = -1
  try:
    i =list.index(1)
  except ValueError as e:
    return i
  finally:
    return i

def getdirection(list, cord):
  axis_x = l[cord['x']]
  axis_y = [item[cord['y']] for item in l]
  yield getoneinlist(axis_x)
  yield getoneinlist(axis_y)

def DFS(l):
  shortest_length = len(l)*2-1
  print 'shortest length would be:',shortest_length,'list from depth first search:'
  for row in l:
    print ','.join([str(i) for i in row])
  cord = dict({'x':0,'y':0})
  while cord['x'] != len(l[0])-1 and cord['y'] != len(l)-1:
    line = getdirection(l,cord)
    for locatedone in line:
      line.next()
    cord['x'] = 5
    cord['y'] = 5
# DFS(l)