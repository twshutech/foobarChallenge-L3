def solution(prisonLayout):
  import copy
  # addWang = lambda n:sum(n)
  class getMapInfo:
    def __init__(self):
      self.floorMap = copy.copy(prisonLayout)
      self.flipFloorMap = [[self.floorMap[j][i] for j in range(len(self.floorMap))] for i in range(len(self.floorMap[0]))]
      self.floors = len(prisonLayout)
      self.doorsAndWalls = len(prisonLayout[0])
      self.pointsOfDoors = []
      self.pointsOfWalls = []

    def horizontal_search(self, floor, finding):
      p = []
      for i in range(len(floor)):
        if floor[i] == finding:
          p.append(i)
      return p

    def get_doors(self):
      for level, floor in enumerate(self.floorMap):

        door = self.horizontal_search(floor, 0)
        location = [[level, door[i]]for i in range(len(door))]
        self.pointsOfDoors = self.pointsOfDoors+location
        if level+1 == len(self.floorMap):
          break
      return self.pointsOfDoors

    def get_walls(self):
      for level, floor in enumerate(self.floorMap):

        door = self.horizontal_search(floor, 1)
        location = [[level, door[i]]for i in range(len(door))]
        self.pointsOfWalls = self.pointsOfWalls+location
        if level+1 == len(self.floorMap):
          break
      return self.pointsOfWalls

    def get_path_walls(self, startPoint=[0,0]):
      #print('startPoint', startPoint[0], startPoint[1])
      num_of_walls = 0
      if self.floorMap[startPoint[0]][startPoint[1]] == 1:
        num_of_walls+=1
      how_far_from_here = point(startPoint[0], startPoint[1])
      #print(how_far_from_here.compass)
      try:
        val_down = self.floorMap[how_far_from_here.compass[1][0]][how_far_from_here.compass[1][1]]
        val_right = self.floorMap[how_far_from_here.compass[3][0]][how_far_from_here.compass[3][1]]
        num_of_walls+=(val_down+val_right)
      except IndexError:
        print('out of range')
      return num_of_walls

    def inspect_path(self, fromPoint):
      leftVerticalStep= self.floors-fromPoint[0]
      leftHorizontalStep = self.doorsAndWalls-fromPoint[1]
      endPoint = [self.floors-1, self.doorsAndWalls-1]
      #print(endPoint[0]-leftVerticalStep,leftVerticalStep,endPoint)
      #printarr.append([endPoint[0]-j,endPoint[1]-i] for j in range(leftVerticalStep) for i in range(leftVHorizontalStep))
      trimMap=[[endPoint[0]-j,endPoint[1]-i] for j in range(leftVerticalStep) for i in range(leftHorizontalStep) if [endPoint[0]-j,endPoint[1]-i] in self.pointsOfDoors]
      trimMapy=[[endPoint[0]-j,endPoint[1]-i] for i in range(leftHorizontalStep) for j in range(leftVerticalStep) if [endPoint[0]-j,endPoint[1]-i] in self.pointsOfDoors]
      if len(trimMapy)>len(trimMap):
        return trimMap
      else:
        return trimMapy

    def path_to_breakpoint(self, breakPoint):
      here_is_bread_for_record_x=[]
      here_is_bread_for_record_y=[]

      for y in range(self.floors):
        for x in range(self.doorsAndWalls):
          compassPoint=point(y,x)
          if [y,x] == breakPoint:
            here_is_bread_for_record_x.append([y,x])
            break
          else:
            if breakPoint in compassPoint.compass:
              break
            for item in compassPoint.compass:
              if compassPoint.getPoint_info(item,0)==True and item not in here_is_bread_for_record_x and item in self.pointsOfDoors:
                here_is_bread_for_record_x.append(item)
            #list_of_possible_space = [item for item in compassPoint.compass if compassPoint.getPoint_info(item,0)]
            #print('coord ',breakPoint ,'has list_of_possible_space',list_of_possible_space)
        if [y,x] == breakPoint:
          break

      for x in range(self.doorsAndWalls):
        for y in range(self.floors):
          if [y,x] == breakPoint:
            here_is_bread_for_record_y.append([y,x])
            break
          else:
            compassPoint=point(y,x)
            for item in compassPoint.compass:
              if compassPoint.getPoint_info(item,0)==True and item not in here_is_bread_for_record_y and item in self.pointsOfDoors:
                here_is_bread_for_record_y.append(item)
            #list_of_possible_space = [item for item in compassPoint.compass if compassPoint.getPoint_info(item,0)]
            #print('coord ',breakPoint ,'has list_of_possible_space',list_of_possible_space)
      if len(here_is_bread_for_record_y)>len(here_is_bread_for_record_x):
        return here_is_bread_for_record_x
      else:
        return here_is_bread_for_record_y

  class point:
    def __init__(self, y=0, x=0):
      self.mapInfo = getMapInfo()
      self.coord = [y, x]
      self.compass = [[y-1, x], [y+1, x], [y, x-1], [y, x+1]] # up, down, left, right.
      self.penetrate = [[y-2, x], [y+2, x], [y, x-2], [y, x+2]] # penetrating wall causees 2 steps further. get coord to see if the location helps us get exit quicker.

    def getPoint_info(self, coord, finding):
      if coord[0]>=0 and coord[1]>=0 and coord[0]<self.mapInfo.floors and coord[1]<self.mapInfo.doorsAndWalls:
        try:
          if finding == self.mapInfo.floorMap[coord[0]][coord[1]]:
            return True
        except IndexError:
          return False
      else:
        return False

  def testing(fromPoint):
    breadcrumbs=[]
    mapInfo = getMapInfo()
    mapInfo.get_doors()
    mapInfo.get_walls()
    pointInfo = point(fromPoint[0],fromPoint[1])
    potentialBreakPoints=[]

    def get_path_to_the_heaven():
      for try_this_wall in potentialBreakPoints:
        print('length of breakpoint to endpoint',len(mapInfo.inspect_path(try_this_wall)))
        print('path from breakpoint to endPoint',mapInfo.inspect_path(try_this_wall))
        print('length of breakpoint to endpoint',len(mapInfo.path_to_breakpoint(try_this_wall)))
        print('path from entrée_and_sortie:',mapInfo.path_to_breakpoint(try_this_wall))
        # breadcrumbs = mapInfo.path_to_breakpoint(try_this_wall)+mapInfo.inspect_path(try_this_wall)
        # print(len(breadcrumbs),'____is____',breadcrumbs)

    def heaven_is_in_the_other_side_of_the_wall():
      for potentialBreakPoint in mapInfo.pointsOfWalls:
        the_wall_is_made_in_china = breakPoint(potentialBreakPoint[0], potentialBreakPoint[1])
        if the_wall_is_made_in_china.ways_to_continue(potentialBreakPoint) == False:
          potentialBreakPoints.append(potentialBreakPoint)
          print('Heaven located in: [',potentialBreakPoint[0], potentialBreakPoint[1],']')
      print('Numbers of potential heaven locations:',len(potentialBreakPoints),'which are:',potentialBreakPoints)

    def lets_walk():
      # print(mapInfo.floorMap)
      step_counter=0
      for x in range(mapInfo.doorsAndWalls):
        step_counter+=1
        for y in range(mapInfo.floors):
          step_counter+=1
          if mapInfo.floorMap[y][x] == 1:
            expectedBreakPoint = breakPoint(y,x)
            #print('point: [',y,x ,'] has num_of_walls',expectedBreakPoint.num_of_walls)
            #print('point: [',y,x ,']',len(expectedBreakPoint.list_of_walls),'list_of_walls',expectedBreakPoint.list_of_walls)
            print('step to breakPoint is', step_counter,expectedBreakPoint.mapInfo.inspect_path([y,x]))
            # expectedBreakPoint.ways_to_continue([for ])
      #       breadcrumbs.append([y,x])
      # print('breadcrumbs',breadcrumbs)
    lets_walk()
    heaven_is_in_the_other_side_of_the_wall()
    get_path_to_the_heaven()

  class breakPoint:
    def __init__(self, y=0, x=0):
      self.mapInfo = getMapInfo()
      self.num_of_walls = self.mapInfo.get_path_walls([y,x])
      self.list_of_walls = self.mapInfo.get_walls()

    def getPoint_info(self, coord):
      try:
        self.mapInfo.floorMap[coord[0]][coord[1]]
        return self.mapInfo.floorMap[coord[0]][coord[1]]
      except IndexError:
        return 'shush no one knows'

    def ways_to_continue(self,coord):
      oh_shit_more_walls=True
      only_has_entrance_no_exit=0
      y=coord[0]
      x=coord[1]
      self.compass = [[y-1, x], [y+1, x], [y, x-1], [y, x+1]] # up, down, left, right.
      for continue_step in self.compass:
        if str(self.getPoint_info(continue_step)) not in ['shush no one knows', '1']:
          only_has_entrance_no_exit+=1
          if only_has_entrance_no_exit>1:
            oh_shit_more_walls=False
            break
      return oh_shit_more_walls

  # breadcrumbs = [[0, 0]]
  # coord = mapInfo()
  #print('coord.get_doors()',set(coord.get_doors()),coord.pointsOfDoors)
  # for yx in coord.pointsOfDoors:
  #   pathInfo = point(yx[0], yx[1])
  #   for surrounding in pathInfo.compass:
    #   try:
    #     if coord.floorMap[surrounding[0]][surrounding[1]] == 1:
    #       print('penetrate',pathInfo.penetrate)
    #   except IndexError:
    #     print('out of range')
      # if surrounding in coord.pointsOfDoors and surrounding not in breadcrumbs:
      #   breadcrumbs.append(surrounding)
    # print(pathInfo.compass)
    # print('bread',breadcrumbs,'length is',len(breadcrumbs))

    # def walk(self):
    #   if c.coord in self.inspect_path():
    #     print('im here:', self.coord)
    #   #print('trimMap', trimMap)
    #   for pathPoint in self.inspect_path():
    #     print('value of point',coord.floorMap[pathPoint[0]][pathPoint[1]])
    #     if coord.floorMap[pathPoint[0]][pathPoint[1]] is 1:
    #       num_of_walls+=1

    # def ghost_way(self):
    #   # Assume shortest way is m+n-1
    #   shortCut = len(self.floorMap)+len(self.floorMap[0])-1
    #   destination = [len(self.floorMap)-1, len(self.floorMap[0])-1]

    # def treeBranches(self):
  testing([0,0])
  

#solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])
solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])
