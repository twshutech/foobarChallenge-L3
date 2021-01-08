# Bomb-baby
# the bombs self-replicate via one of two distinct processes:
# Every Mach bomb retrieves a sync unit from a Facula bomb; for every Mach bomb, a Facula bomb is created;
# Every Facula bomb spontaneously creates a Mach bomb.
def check_numbers_retrieves(solu,steps=0):
  global depth
  ns = solu['ns'][-1]
  modified_bomb = rest_bombs(max(ns), min(ns))
  steps += delta_steps(max(ns), min(ns))
  if modified_bomb == 0:
    steps-=1
    modified_bomb = min(ns)

  solu['ns'].append((modified_bomb, min(ns))[::-1])
  solu['steps'] = steps
  if is_solution(solu['ns'][-1]) == True:
    if len(depth) == 0:
      depth.append(solu)
    elif depth[0]['steps'] >= solu['steps']:
      depth = [solu]
    if solu['ns'][-1] != (1,1) and solu['ns'][-1][0] == solu['ns'][-1][1]:
      solu['steps'] = "impossible"
    return solu
  else:
    return check_numbers_retrieves(solu, steps)

def is_solution(mf):
  if mf[0] == mf[1]:
    return True
  else:
    return False

def solution(m,f):
  global delta_steps, rest_bombs, descending, depth
  delta_steps = lambda a,b:a/b
  rest_bombs = lambda a,b:a%b
  descending = lambda a: sorted(a, reverse=True)
  sort_key = lambda a: a[1]
  depth = []
  from_n = int(m) + int(f)
  processes = [(from_n, int(m)), (from_n, int(f))]
  for bomb_set in processes:
    steps = 0
    mf = descending(bomb_set)
    solu = dict({'ns':[mf], 'steps':steps})
    check_numbers_retrieves(solu, steps)
  return str(depth[0]['steps'])

print solution('4','7')