# the bombs self-replicate via one of two distinct processes:
# Every Mach bomb retrieves a sync unit from a Facula bomb; for every Mach bomb, a Facula bomb is created;
# Every Facula bomb spontaneously creates a Mach bomb.
print divmod(2, 1)

def first_process(m, f):
  return [(m+f, f), (m, m+f)]

def second_process(n, delta_n):
  n = int(n)
  delta_n = int(delta_n)

  print n,delta_n
  return divmod(n, delta_n)

def is_this_fibonacci(m,f):
  message = {
    'count': 0,
    'solution': '',
    'mf': tuple()
  }
  processes = first_process(int(m), int(f))
  for bomb_set in processes:
    while message['mf'] != (1,1) or message['solution'] != "impossible":
      result = second_process(*bomb_set)
      message['count'] += result[0]
      bomb_set = (result[1], bomb_set[1])
      message['mf'] = bomb_set
      print 'result',result,'bomb_set',bomb_set,cmp(*message['mf'])

      if cmp(*message['mf']) == 0:
        message['solution'] = "impossible"
      elif cmp(*message['mf']) == -1:
        bomb_set = bomb_set[::-1]

      if message['mf'] == (1,1) or message['solution'] == "impossible":
        break
  return message

def solution(m,f):
  answer = is_this_fibonacci(m, f)
  if isinstance(answer['count'], int):
     answer = str(answer['count'])
  return answer

print "('2', '1')",solution('2', '1'),"\n"
print "('2', '4')",solution('2', '4'),"\n"
print "('4', '7')",solution('4', '7'),"\n"
print "('2', '2')",solution('2', '2'),"\n"
print "('149333', '12')",solution('149333','12')