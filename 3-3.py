class node:
  def __init__(self, n):
    print 'n',n
    self.right = None
    self.left = None
    self.value = n

def level_first(node):


def solution(n):
  global level
  level = 0
  processing_node = int(n)
  node_n = None
  if processing_node != 1:
    node_n = node(processing_node)
    if node_n.value % 2 == 0:
      child_value = node_n.value // 2
      node_n.left = node(child_value)
    else:
      node_n.left = node(processing_node+1)
      node_n.right = node(processing_node-1)
    if node_n.left != None:
      solution(node_n.left.value)
    if node_n.right != None:
      solution(node_n.right.value)

solution('15')