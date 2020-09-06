def solution(prisonLayout):
  import copy

  class mapInfo:
    def __init__(self):
      self.floorMap = []
      self.flipFloorMap = []
      self.floors = len(prisonLayout)
      self.doorsAndWalls = len(prisonLayout[0])
      self.pointsOfDoors = []

    def get_flip_layout(self):
      self.floorMap = copy.copy(prisonLayout)
      # len(self.floorMap[0]) numbers of doors and walls in a floor.
      # len(self.floorMap) numbers of floors of the prison.
      self.flipFloorMap = [[self.floorMap[j][i] for j in range(len(self.floorMap))] for i in range(len(self.floorMap[0]))]
      return self.flipFloorMap

    def horizontal_search(self, floor):
      p = []
      for i in range(len(floor)):
        if floor[i] == 0:
          p.append(i)
      #('floor',floor,'p',p)
      return p

    def get_doors(self):
      level=0
      for floor in self.floorMap:
        #print(floor)
        door = self.horizontal_search(floor)
        location = [[level, door[i]]for i in range(len(door))]
        self.pointsOfDoors = self.pointsOfDoors+location
        level+=1
      return self.pointsOfDoors

    def stair_to_the_end(self):
      yx = [0, 0]
      def initWalls():
        return [0, 0]
      numberOfWalls = initWalls()
      for i in range(len(self.floorMap)):
        if yx[0] == yx[1]:
          yx[1]+=1
        elif yx[0]+1 == yx[1]:
          yx[0]+=1
        if self.floorMap[yx[0]][yx[1]]==1:
          numberOfWalls[0]+=1
        if self.floorMap[yx[1]][yx[0]]==1:
          numberOfWalls[1]+=1
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

    def ghost_way(self):
      # Assume shortest way is m+n-1
      shortCut = len(self.floorMap)+len(self.floorMap[0])-1
      destination = [len(self.floorMap)-1, len(self.floorMap[0])-1]

  class point:
    def __init__(self, x=0, y=0):
      self.coord = [y, x]
      self.compass = [[y-1, x], [y+1, x], [y, x-1], [y, x+1]] # up, down, left, right.
  
  breadcrumbs = [[0, 0]]
  coord = mapInfo()
  #print('get_doors',coord.get_doors(),coord.get_flip_layout())
  for yx in coord.get_doors():
    pathInfo = point(yx[1], yx[0])
    for surrounding in pathInfo.compass:
      if surrounding in coord.get_doors() and surrounding not in breadcrumbs:
        breadcrumbs.append(surrounding)
    #print(pathInfo.compass)
    #print('bread',breadcrumbs,'length is',len(breadcrumbs))
  coord.stair_to_the_end()
  coord.straight_to_the_end()


#solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])
solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])