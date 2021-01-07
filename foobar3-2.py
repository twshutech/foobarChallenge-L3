# the bombs self-replicate via one of two distinct processes:
# Every Mach bomb retrieves a sync unit from a Facula bomb; for every Mach bomb, a Facula bomb is created;
# Every Facula bomb spontaneously creates a Mach bomb.
def check_numbers_retrieves(ns,steps=0):
  solu = dict({'ns':ns, 'steps':steps, 'valid':False})

  modified_bomb = rest_bombs(max(ns), min(ns))
  steps += delta_steps(max(ns), min(ns))
  # if modified_bomb != 0:
  #   ns = (modified_bomb, min(ns))[::-1]
  # else:
  #   modified_bomb += min(ns)
  #   steps -= 1
  #   ns = (modified_bomb, min(ns))
  solu['ns'] = (modified_bomb, min(ns))[::-1]
  solu['steps'] = steps
  print 'solu',solu,'ns'
  if is_solution(solu['ns']) == False and modified_bomb == 0:
    modified_bomb = min(ns)
    steps-=1
    return solu
  else:
    return check_numbers_retrieves(solu['ns'], steps)

def first_process(m, f):
  return [(m+f, f), (m, m+f)]

def second_process(n, delta_n):
  n = int(n)
  delta_n = int(delta_n)
  if delta_n == 0 or n == 0:
    return (0, n)
  else:
    return n - delta_n * (n/delta_n)

def is_this_fibonacci(bomb_set):

  bomb_set = sorted(bomb_set)
  message = {
    'count': 0,
    'solution': '',
    'mf': bomb_set
  }
  while message['mf'] != (1,1) or message['solution'] != "impossible":
    result = second_process(*bomb_set[::-1])

    if cmp(*message['mf']) == 0:
      message['solution'] = "impossible"
    elif cmp(*message['mf']) == -1:
      bomb_set = bomb_set[::-1]

    message['count'] += result[0]
    bomb_set = (result[1], bomb_set[1])
    message['mf'] = bomb_set

    if message['mf'] == (1,1) or message['solution'] == "impossible":
      break
  return bomb_set

def is_solution(mf):
  if mf[0] == mf[1] or 0 in mf:
    return False
  else:
    return True

def solution(m,f):
  global delta_steps,rest_bombs,descending
  delta_steps = lambda a,b:a//b #Rounded to avoid bomb goes to 0.
  rest_bombs = lambda a,b:a%b
  descending = lambda a: sorted(a, reverse=True)
  depth = []
  compare_list = []
  processes = first_process(int(m), int(f))
  for bomb_set in processes:
    steps = 0
    #depth.append(is_this_fibonacci(bomb_set))
    mf = descending(bomb_set)
    print 'RESULT',check_numbers_retrieves(mf, steps),'mf',mf

    # mf = result['ns']

    # depth.append(mf)
    # print 'mf',mf
    # compare_list.append(result)
    # while mf['ns'] != (1,1) or f:
  return depth

print "('2', '1'):\n",solution('2', '1'),"\n"
# print "('2', '4'):\n",solution('2', '4'),"\n"
# print "('4', '7'):\n",solution('4', '7'),"\n"
# print "('2', '2'):\n",solution('2', '2'),"\n"
# print "('149333', '12'):\n",solution('149333','12')