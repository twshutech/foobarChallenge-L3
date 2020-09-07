def solution(prisonLayout):
  import copy
  
  
  class mapInfo:
    def __init__(self):
      self.floorMap = []
      self.flipFloorMap = []
      self.floors = len(prisonLayout)
      self.doorsAndWalls = len(prisonLayout[0])
      self.pointsOfDoors = []
      self.tree = [[0, 0]]

    def get_flip_layout(self):
      self.floorMap = copy.copy(prisonLayout)
      self.flipFloorMap = [[self.floorMap[j][i] for j in range(len(self.floorMap))] for i in range(len(self.floorMap[0]))]
      return self.flipFloorMap

    def horizontal_search(self, floor):
      p = []
      for i in range(len(floor)):
        if floor[i] == 0:
          p.append(i)
      return p

    def get_doors(self, level=0):
      for floor in self.floorMap:
        #print(floor)
        #if level:
        door = self.horizontal_search(floor)
        location = [[level, door[i]]for i in range(len(door))]
        #if location not in self.pointsOfDoors:
        self.pointsOfDoors = self.pointsOfDoors+location
        print('self.pointsOfDoors',self.pointsOfDoors)
        level+=1
      return self.pointsOfDoors

    def stair_to_the_end(self):
      yx = [0, 0]
      def initWalls():
        return [0, 0]
      numberOfWalls = initWalls()
      for i in range(len(self.floorMap)):
        if yx[0] == yx[1]:
          yx[1]+=i
        elif yx[0]+1 == yx[1]:
          yx[0]+=i
        if self.floorMap[yx[0]][yx[1]]==1:
          numberOfWalls[0]+=i
        if self.floorMap[yx[1]][yx[0]]==1:
          numberOfWalls[1]+=i
      print(numberOfWalls)

    def straight_to_the_end(self):
      def initWalls():
        return [0, 0, 0, 0]
      numberOfWalls = initWalls()
      for i in range(len(self.floorMap)):
        if self.floorMap[0][i] == 1:
          numberOfWalls[0]+=1
        if self.floorMap[len(self.floorMap)[0]][i] == 1:
          numberOfWalls[1]+=1
        if self.floorMap[i][0] == 1:
          numberOfWalls[2]+=1
        if self.floorMap[i][len(self.floorMap)] == 1:
          numberOfWalls[3]+=1
      print(numberOfWalls)

    # def ghost_way(self):
    #   # Assume shortest way is m+n-1
    #   shortCut = len(self.floorMap)+len(self.floorMap[0])-1
    #   destination = [len(self.floorMap)-1, len(self.floorMap[0])-1]

    # def treeBranches(self):

  class point:
    def __init__(self, x=0, y=0):
      self.coord = [y, x]
      self.compass = [[y-1, x], [y+1, x], [y, x-1], [y, x+1]] # up, down, left, right.
      self.penetrate = [[y-2, x], [y+2, x], [y, x-2], [y, x+2]] # penetrating wall causees 2 steps further. get coord to see if the location helps us get exit quicker.

  breadcrumbs = [[0, 0]]
  coord = mapInfo()

  print('coord.get_doors()',coord.get_doors(),coord.pointsOfDoors)
  for yx in coord.pointsOfDoors:
    pathInfo = point(yx[1], yx[0])
    for surrounding in pathInfo.compass:
      try:
        if coord.floorMap[surrounding[0]][surrounding[1]] == 1:
          print('penetrate',pathInfo.penetrate)
      except IndexError:
        print('out of range')
      if surrounding in coord.pointsOfDoors and surrounding not in breadcrumbs:
        breadcrumbs.append(surrounding)

    print(pathInfo.compass)
    print('bread',breadcrumbs,'length is',len(breadcrumbs))


#solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])
solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])
