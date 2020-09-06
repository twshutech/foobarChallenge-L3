def getNextDirection(roadMap, coord):
  nextStep = {}
  for key, value in coord.items():
    if key == 'width':
      #print(value+1<maxWidth, roadMap[value+1][coord['height']])
      if value+1<maxWidth and roadMap[value+1][coord['height']] == 0:
        # right step coord can not be greater than maximum width.
        nextStep['down'] = value+1
        #print(nextStep)
      else:
        if value-1>=0 and roadMap[value-1][coord['height']] == 0: # left step coord can not be smaller than zero.
          nextStep['up'] = value-1
        #print(nextStep)
    else:
      if value+1<maxHeight and roadMap[coord['width']][value+1] == 0: # down step coord can not be greater than maximum height.
        nextStep['right'] = value+1
        #print(nextStep)
      else:
        if value-1>=0 and roadMap[coord['width']][value-1] == 0: # up step coord can not be smaller than zero.
          nextStep['left'] = value-1
        #print(nextStep)

  return nextStep

def updateNextStep(roadMap, coord):
  #print(roadMap, coord)
  direction = getNextDirection(roadMap, coord)
  
  step = direction.values()
  if direction.keys()[0] in ['up', 'down']:
    coord['height'] = step[0]
  if direction.keys()[0] in ['left', 'right']:
    coord['width'] = step[0]
  print(coord)
  recordFootpring(roadMap, coord)

def recordFootpring(roadMap, coord):
  footprintObj = {
    'width': coord['width'],
    'height': coord['height']
  }
  #if coord not in footprint:
  footprint.append(footprintObj)

  if coord['width'] == destination['width'] and coord['height'] == destination['height']:
    print(footprint)
  else:
    print(footprint)
    if len(footprint)<=5:
      updateNextStep(roadMap, {'width': coord['width'],'height': coord['height']})

def solution(roadMap):
  global maxWidth, maxHeight, footprint, destination

  footprint = []
  maxWidth = len(roadMap)
  maxHeight = len(roadMap[0])
  destination = {'width': maxWidth-1, 'height': maxHeight-1}
  coord = {'width':0, 'height':0}
  recordFootpring(roadMap, coord)
  return len(footprint)

print(solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))
#solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])