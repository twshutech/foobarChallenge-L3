# the bombs self-replicate via one of two distinct processes:
# Every Mach bomb retrieves a sync unit from a Facula bomb; for every Mach bomb, a Facula bomb is created;
# Every Facula bomb spontaneously creates a Mach bomb.
def first_process(m, f):
  return [(m+f, f), (m, m+f)]

def second_process(digit, del_digit):
  return divmod(digit, del_digit)

def third_process(m, f):
  message = {
    'count': 0,
    'solution': ''
  }
  m = int(m)
  f = int(f)
  processes = first_process(m,f)

  while len(processes) > 0:
    bomb_set = processes.pop()
    if cmp(*bomb_set) == 0:
      message['solution'] = "impossible"
      break
    elif cmp(*bomb_set) == -1:
      bomb_set = bomb_set[::-1]
    result = second_process(*bomb_set)
    message['count'] = result[0]
    while result[0] != 1 or f != 
  return message

def solution(m,f):
  answer = third_process(m, f)
  if isinstance(answer, int):
     answer = str(answer)
  return answer


print "('2', '1')",solution('2', '1')
print "('2', '4')",solution('2', '4')
print "('7', '4')",solution('4', '7')
print "('2', '2')",solution('2', '2')
print "('2', '1')",solution('149333','12')