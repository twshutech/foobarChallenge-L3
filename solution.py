import queue
class info:
  def right_wall(self, l):
    return len(l[0])-1
  def bottom_wall(self, l):
    return len(l)-1

def bfs(l, b):
  information = info()
  q = queue.Queue()
  stack = []
  e = [information.right_wall(l), information.bottom_wall(l)]
  s = [0, 0]
  flag = False
  stack.append(s)
  print 'ee',e
  while flag != True:
    for s in stack:
      if s == e:
        flag = True
      else:
        del stack[:]
        if s[1]+1<=e[1]:
          #print 'xx',l[s[0],s[1]+1]
          stack.append([s[0],s[1]+1])
        if s[0] <= e[0]:
          #print 'xx',l[s[0],s[1]+1]==0
          stack.append([s[0]+1,s[1]])
      q.put(s)
      print 'q',list(q.queue),'stack',stack

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
  print 'l',l
  return BFS(l,breakable)

def reverse_solution(l):
  breakable = True
  l.sort(reverse=True)
  for row in l:
    row.sort(reverse=False)
  print 'l',l
  return BFS(l,breakable)

if __name__ == '__main__':
  l = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
  # way_go_path = solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])
  # way_back_path = reverse_solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])
  # print 'go', way_go_path
  # print 'back', way_back_path
  bfs(l, True)


  #print answer([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])
  #solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])
  # print(solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))
  # print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))
  # print(reverse_solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))
  # print(reverse_solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))
  