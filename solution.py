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
    if coord not in breadcrumbs:
      breadcrumbs.append(coord)
      q.put(coord)
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
    
    print('breadcrumbs',q.queue)

    return len(breadcrumbs)

  def check_near_breakpoint(coord):
    for wall_point in impassable_walls:
      wallInfo = point_info(wall_point[0], wall_point[1])
      exist_index = 0
        # wall_point is [1, 0]
      if coord in wallInfo.compass:
        # [1, 0] neihbor
        return_point = point_info(wall_point[0], wall_point[1])
        entrance_exist = [item for item in return_point.available_compass if item != coord]
        for item in breadcrumbs:
          if item in entrance_exist:
            exist_index = breadcrumbs.index(item)
            break
      if exist_index != 0:
        break
      else:
        return
    return exist_index

  def start():
    list_length = []

    def get_way_out():
      way_out = []
      for breadcrumb in breadcrumbs:
        try:
          exist_point = check_near_breakpoint(breadcrumb)
          way_out.append(exist_point)
        except:
          pass
        finally:
          return way_out

      return way_out

    def trim_path():
      way_out = get_way_out()
      new_arr = breadcrumbs[:]
      if len(way_out) != 0:
        try:
          for exist_point in way_out:
            print('exist_point',exist_point)
            for i in range(exist_point):
              if i>0 and i !=0 and i<len(breadcrumbs):
                new_arr.remove(new_arr[i])
                print('q.queue[i]',q.queue[i])
                del q.queue[i]
        except IndexError:
          pass
        finally:
          print('new_arr',q.queue)
          list_length.append(len([item for item in new_arr if new_arr.count(item)==1]))
          return list_length[0]

    if now_and_then([0, 0]) > trim_path():
      return trim_path()
    else:
      return now_and_then([0, 0])

  mapInfo = map_info()
  return start()
print(solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))
print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))
