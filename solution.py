def solution(mappa_mundi):
  import Queue as queue
  breadcrumbs = []
  impassable_walls = []
  q = queue.Queue()
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
      self.available_compass = self.available_turning()
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

    def available_turning(self):
      return [self.compass[index] for index, node_value in enumerate(self.node_of_compass()) if node_value == 0]

    def node_of_compass(self):
      return [mappa_mundi[coord[0]][coord[1]]for coord in self.compass]

  def now_and_then(coord):
    if coord not in q.queue:
      q.put(coord)
    now_point = point_info(coord[0], coord[1])

    for index, next_node in enumerate(now_point.compass):
      try:
        if coord == [mapInfo.edge_vertical-1, mapInfo.edge_horizontal-1]:
          break 
        elif now_point.node_value[index] == 0 and next_node not in q.queue:
          now_and_then(next_node)
        elif now_point.node_value[index] == 1 and next_node not in impassable_walls:
          impassable_walls.append(next_node)
      except IndexError:
        pass

    return len(q.queue)

  # def seen_you_before():
  #   queue_list = []
  #   for index, item in enumerate(list(q.queue)):

  def check_near_breakpoint(coord):
    for wall_point in impassable_walls:
      wallInfo = point_info(wall_point[0], wall_point[1])
      exit_index = 0# wall_point is [1, 0]
      if coord in wallInfo.compass:# [1, 0] neihbor
        return_point = point_info(wall_point[0], wall_point[1])
        entrance_exit = [item for item in return_point.available_compass if 1<len(return_point.available_compass)<3]
        if len(entrance_exit) == 2:
          entrance_exit.insert(1, wall_point)
        exit_index = len(entrance_exit)

      if exit_index != 0:
        break
    return entrance_exit

  def start():

    def get_way_out():
      way_out = []
      try:
        for index, breadcrumb in enumerate(list(q.queue)):
          exit_point = check_near_breakpoint(breadcrumb)
          if len(exit_point) > 0:
            way_out.append(exit_point)
      except IndexError: 
        pass
      finally:
        return [tunnel_point for tunnel_point in way_out if way_out.count(tunnel_point)==1]

    def trim_path():
      list_length = []
      way_out = get_way_out()
      if len(way_out) != 0:
        for index_q, from_to in enumerate(way_out):
          flag = True
          new_arr = []
          for index, item in enumerate(list(q.queue)):
            if item == from_to[0]:
              new_arr.insert(index,from_to[0])
              flag = not flag
            if item == from_to[2]:
              flag = not flag
              new_arr.insert(index,from_to[1])
              new_arr.insert(index,from_to[2])
            if flag == True:
              if item not in new_arr:
                new_arr.append(item)
          
          list_length.append(len([bread for bread in new_arr if new_arr.count(bread)==1]))
          #if len(new_arr) == 11:
          if index_q+1 == len(way_out):
            break
      return list_length[0]

    if now_and_then([0, 0]) == mapInfo.edge_horizontal+mapInfo.edge_vertical-1:
      return now_and_then([0, 0])
    else:
      return trim_path()

  mapInfo = map_info()
  return start()
print(solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))
print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))
