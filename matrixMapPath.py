# def solution(prisonLayout):
#   import copy
#   # addWang = lambda n:sum(n)
#   class getMapInfo:
#     def __init__(self):
#       self.floorMap = copy.copy(prisonLayout)
#       self.flipFloorMap = [[self.floorMap[j][i] for j in range(len(self.floorMap))] for i in range(len(self.floorMap[0]))]
#       self.floors = len(prisonLayout)
#       self.doorsAndWalls = len(prisonLayout[0])
#       self.pointsOfDoors = []
#       self.pointsOfWalls = []

#     def validator(self, coord):
#       varified=False
#       if self.doorsAndWalls>coord[1]>=0 and self.floors>coord[0]>=0:
#         varified=True
#       return varified

#     def get_turning_point(self):
#       list_of_turning_point=[]
#       def turning_or_straight(coord):
#         numbers_of_doors=0
#         movements=[]
#         coordInfo = point(coord[0], coord[1])
#         for w_or_d in coordInfo.compass:
#           if self.validator(w_or_d):
#             if self.floorMap[w_or_d[0]][w_or_d[1]] == 0:
#               numbers_of_doors+=1
#               movements.append(w_or_d)
#               if coord not in movements:
#                 movements.append(coord)

#         delta_y = len([delta_ys for delta_ys in [[sort_y[0]]for sort_y in movements] if [[sort_y[0]]for sort_y in movements].count(delta_ys)==1])
#         delta_x = len([delta_xs for delta_xs in [[sort_x[1]]for sort_x in movements] if [[sort_x[1]]for sort_x in movements].count(delta_xs)==1])
#         if delta_x!=0 and delta_y!=0:
#           list_of_turning_point.append(coord)          

#       for door in self.pointsOfDoors:
#         turning_or_straight(door)
#       return list_of_turning_point

#     def linearCheck(self, arr, fromPoint):
#       def verify_linear_array(arr):
#         is_linear=True
#         for i in range(len(arr)):
#           # expect i = 0, 1, 2, 3, 4, 5
#           if arr[i] not in [i,fromPoint-i]:
#             is_linear=False
#             break
#         return is_linear

#       # def digging_deeper(moreArr):
#       #   if isinstance(arr[0])==True:
#       #     for subArr in moreArr:
#       #       digging_deeper(subArr)
#       #   else:
#       #     verify_linear_array(moreArr)

#       return verify_linear_array(arr)

#     def horizontal_search(self, floor, finding):
#       p = []
#       for i in range(len(floor)):
#         if floor[i] == finding:
#           p.append(i)
#       return p

#     def vertical_search(self, column, finding):
#       p = []
#       for i in range(len(column)):
#         if column[i] == finding:
#           p.append(i)
#       return p

#     def get_doors(self):
#       for level, floor in enumerate(self.floorMap):

#         door = self.horizontal_search(floor, 0)
#         location = [[level, door[i]]for i in range(len(door))]
#         self.pointsOfDoors = self.pointsOfDoors+location
#         if level+1 == len(self.floorMap):
#           break
#       return self.pointsOfDoors

#     def get_walls(self):
#       for level, floor in enumerate(self.floorMap):

#         door = self.horizontal_search(floor, 1)
#         location = [[level, door[i]]for i in range(len(door))]
#         self.pointsOfWalls = self.pointsOfWalls+location
#         if level+1 == len(self.floorMap):
#           break
#       return self.pointsOfWalls

#     def get_path_walls(self, startPoint=[0,0]):
#       #print('startPoint', startPoint[0], startPoint[1])
#       num_of_walls = 0
#       if self.floorMap[startPoint[0]][startPoint[1]] == 1:
#         num_of_walls+=1
#       how_far_from_here = point(startPoint[0], startPoint[1])
#       #print(how_far_from_here.compass)
#       try:
#         val_down = self.floorMap[how_far_from_here.compass[1][0]][how_far_from_here.compass[1][1]]
#         val_right = self.floorMap[how_far_from_here.compass[3][0]][how_far_from_here.compass[3][1]]
#         num_of_walls+=(val_down+val_right)
#       except IndexError:
#         print('out of range')
#       return num_of_walls

#     def inspect_path(self, fromPoint):
#       leftVerticalStep= self.floors-fromPoint[0]
#       leftHorizontalStep = self.doorsAndWalls-fromPoint[1]
#       endPoint = [self.floors-1, self.doorsAndWalls-1]
#       trimMap=[[fromPoint[0]+j,fromPoint[1]+i] for j in range(leftVerticalStep) for i in range(leftHorizontalStep) if [fromPoint[0]+j,fromPoint[1]+i] in self.pointsOfDoors]
#       trimMapy=[[fromPoint[0]+j,fromPoint[1]+i] for i in range(leftHorizontalStep) for j in range(leftVerticalStep) if [fromPoint[0]+j,fromPoint[1]+i] in self.pointsOfDoors]
#       if len(trimMapy)>len(trimMap):
#         return trimMap
#       else:
#         return trimMapy

#     def path_to_breakpoint(self, breakPoint):
#       here_is_bread_for_record_x=[]
#       here_is_bread_for_record_y=[]

#       for y in range(self.floors):
#         for x in range(self.doorsAndWalls):
#           compassPoint=point(y,x)
#           if [y,x] == breakPoint and [y,x] not in here_is_bread_for_record_x:
#             here_is_bread_for_record_x.append([y,x])
#             break
#           else:
#             if breakPoint in compassPoint.compass:
#               break
#             for item in compassPoint.compass:
#               if compassPoint.getPoint_info(item,0)==True and item not in here_is_bread_for_record_x and item in self.pointsOfDoors:
#                 here_is_bread_for_record_x.append(item)
#             #list_of_possible_space = [item for item in compassPoint.compass if compassPoint.getPoint_info(item,0)]
#         if breakPoint in here_is_bread_for_record_x:
#           break

#       for x in range(self.doorsAndWalls):
#         for y in range(self.floors):
#           if [y,x] == breakPoint:
#             here_is_bread_for_record_y.append([y,x])
#             break
#           else:
#             compassPoint=point(y,x)
#             for item in compassPoint.compass:
#               if compassPoint.getPoint_info(item,0)==True and item not in here_is_bread_for_record_y and item in self.pointsOfDoors:
#                 here_is_bread_for_record_y.append(item)
#             #list_of_possible_space = [item for item in compassPoint.compass if compassPoint.getPoint_info(item,0)]
#         if breakPoint in here_is_bread_for_record_y:
#           break
#       if len(here_is_bread_for_record_y)>len(here_is_bread_for_record_x):
#         return here_is_bread_for_record_x
#       else:
#         return here_is_bread_for_record_y

#   class point:
#     def __init__(self, y=0, x=0):
#       try:
#         self.mapInfo = getMapInfo()
#         self.coord = [y, x]
#         self.compass = [[y-1, x], [y+1, x], [y, x-1], [y, x+1]] # up, down, left, right.
#         self.penetrate = [[y-2, x], [y+2, x], [y, x-2], [y, x+2]] # penetrating wall causees 2 steps further. get coord to see if the location helps us get exit quicker.
#       except TypeError:
#         print('TypeError:')

#     def getPoint_info(self, coord, finding):
#       if coord[0]>=0 and coord[1]>=0 and coord[0]<self.mapInfo.floors and coord[1]<self.mapInfo.doorsAndWalls:
#         try:
#           if finding == self.mapInfo.floorMap[coord[0]][coord[1]]:
#             return True
#         except IndexError:
#           return False
#       else:
#         return False

#   def testing(fromPoint):
#     mapInfo = getMapInfo()
#     mapInfo.get_doors()
#     mapInfo.get_walls()
#     potentialBreakPoints=[]
#     endpoint = [mapInfo.floors-1, mapInfo.doorsAndWalls-1]

#     def get_path_to_the_heaven():
#       def scanHV(turning_point):
#         print('turning_point',turning_point)
#         index_of_row = mapInfo.horizontal_search(mapInfo.floorMap[turning_point[1]], 0)
#         index_of_column = mapInfo.vertical_search(mapInfo.flipFloorMap[turning_point[0]], 0)
#         if mapInfo.linearCheck(index_of_column, turning_point[1])==True:
#           return
#         if mapInfo.linearCheck(index_of_row, turning_point[0])==True:
#           return

#       for try_this_wall in potentialBreakPoints:
#         reversed_path=mapInfo.inspect_path(try_this_wall)
#         reversed_path.sort(key=lambda  x:x[1])
#         breadcrumbs = mapInfo.path_to_breakpoint(try_this_wall)+mapInfo.inspect_path(try_this_wall)
#         for turning_point in mapInfo.get_turning_point():
#           if turning_point in breadcrumbs:
#             scanHV(turning_point)
#             print('POSSIBILITY_TO_ESCAPE_FROM_HERE',turning_point)
#             # if endpoint is mapInfo.horizontal_search(mapInfo.floorMap[turning_point[1]], 0) and mapInfo.vertical_search(mapInfo.flipFloorMap[turning_point[0]], 0):
#             #   print('________ESCAPED_________')

#         print(len(breadcrumbs),'____is____',breadcrumbs)

#     def heaven_is_in_the_other_side_of_the_wall():
#       for potentialBreakPoint in mapInfo.pointsOfWalls:
#         the_wall_is_made_in_china = breakPoint(potentialBreakPoint[0], potentialBreakPoint[1])
#         if len(the_wall_is_made_in_china.ways_to_continue(potentialBreakPoint))>0:
#           print('ways have :',the_wall_is_made_in_china.ways_to_continue(potentialBreakPoint))
#           potentialBreakPoints.append(potentialBreakPoint)

#     def lets_walk():
#       step_counter=0
#       for x in range(mapInfo.doorsAndWalls):
#         step_counter+=1
#         for y in range(mapInfo.floors):
#           step_counter+=1
#           if mapInfo.floorMap[y][x] == 1:
#             # expectedBreakPoint = breakPoint(y,x)
#             # expectedBreakPoint.ways_to_continue([for ])
#       #       breadcrumbs.append([y,x])
#       # print('breadcrumbs',breadcrumbs)
#     # lets_walk()
#     heaven_is_in_the_other_side_of_the_wall()
#     get_path_to_the_heaven()
#     print('list of turning point',mapInfo.get_turning_point())

#   class breakPoint:
#     def __init__(self, y=0, x=0):
#       self.mapInfo = getMapInfo()
#       self.num_of_walls = self.mapInfo.get_path_walls([y,x])
#       self.list_of_walls = self.mapInfo.get_walls()

#     def getPoint_info(self, coord):
#       try:
#         self.mapInfo.floorMap[coord[0]][coord[1]]
#         return self.mapInfo.floorMap[coord[0]][coord[1]]
#       except IndexError:
#         return 'shush no one knows'

#     def ways_to_continue(self,coord):
#       oh_shit_more_walls=[]
#       y=coord[0]
#       x=coord[1]
#       self.compass = [[y-1, x], [y+1, x], [y, x-1], [y, x+1]] # up, down, left, right.
#       for continue_step in self.compass:
#         if str(self.getPoint_info(continue_step)) not in ['shush no one knows', '1'] and continue_step[0]>=0 and continue_step[1]>=0:
#           oh_shit_more_walls.append(continue_step)

#       return oh_shit_more_walls

#   testing([0,0])
  

# #solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])
# solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])
