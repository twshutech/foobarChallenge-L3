def solution(mappa_mundi):

  try:
   import queue
  except ImportError:
    import Queue as queue

  queue=queue.Queue()

  breadcrumbs = []
  impassable_walls = []
  turning_points = []
  break_points = []

  class map_info:
    def __init__(self):
      self.edge_horizontal = len(mappa_mundi[0])
      self.edge_vertical = len(mappa_mundi)

    def horizontal_search(self, floor, finding):
      p = []
      for i in range(len(floor)):
        if floor[i] == finding:
          p.append(i)
      return p

    def get_doors(self):
      corridors = []
      for level, floor in enumerate(mappa_mundi):
        door = self.horizontal_search(floor, 0)
        location = [[level, door[i]]for i in range(len(door))]
        corridors += location
        if level+1 == len(mappa_mundi):
          break
      return corridors

  class point_info:
    def __init__(self, y, x):
      self.compass = self.varify_compass_values(y, x)
      self.node_value = self.node_of_compass()
      self.coord = [y, x]

    def varify_compass_values(self, y, x):
      self.compass = [[y-1, x], [y+1, x], [y, x-1], [y, x+1]]
      if x+1 == mapInfo.edge_horizontal:
        self.compass.remove([y, x+1])
      elif x == 0:
        self.compass.remove([y, x-1])
      if y+1 == mapInfo.edge_vertical:
        self.compass.remove([y+1, x])
      elif y == 0:
        self.compass.remove([y-1, x])
      return self.compass

    def node_of_compass(self):
      return [mappa_mundi[coord[0]][coord[1]]for coord in self.compass]
    
    def point_type(self):
      if self.node_value.count(0)<2:
        return
      else:
        print('see if wall if turning or breaking', self.node_value)

  def now_and_then(coord):
    if coord not in breadcrumbs:
      queue.put(coord)
      breadcrumbs.append(coord)
    now_point = point_info(coord[0], coord[1])

    for index, next_node in enumerate(now_point.compass):
      try:
        if coord == [mapInfo.edge_vertical-1, mapInfo.edge_horizontal-1]:
          break 
        elif now_point.node_value[index] == 0 and next_node not in breadcrumbs:
          now_and_then(next_node)
        elif now_point.node_value[index] == 1 and next_node not in impassable_walls:
          impassable_walls.append(next_node)
      except IndexError:
        pass

      # if coord == [mapInfo.edge_vertical-1, mapInfo.edge_horizontal-1]:
      #   print('(╯°Д°)╯ ┻━┻  congrats you have escape D-Link')
      #   print('Here is the',len(breadcrumbs),'breadcrumbs that you left:', breadcrumbs)

  def start():
    now_and_then([0, 0])
    for wall_point in impassable_walls:
      wallInfo = point_info(wall_point[0], wall_point[1])
      wallInfo.point_type()

    print('啊Q',list(queue.queue))
    return len(impassable_walls)

  mapInfo = map_info()
  
  return start()

print(solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))
print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))
# get 0 doordinates, for map by queue, check compass, add item to queue.