import re, random

def vlans(n):
  vlan_expression = []
  dash = '-'
  for i in range(n):
    range_or_single = random.randint(0,1)
    if range_or_single: # 1
      from_vlan = random.randint(1,4094)
      end_vlan = random.randint(1,4094)
      vlan_str = str(from_vlan)+dash+str(end_vlan)
      vlan_expression.append(vlan_str)
    else: # 0
      vlan = random.randint(1,4094)
      vlan_expression.append(str(vlan))
    yield vlan_expression

def test():
  reg = "^([1-9]|[0-9]{2,3}|[1-4][0-9]{2}[0-4])(?:-(?:[1-9]|[0-9]{2,3}|[1-4][0-9]{2}[0-4]))?(?:,\s?(?:[1-9]|[0-9]{2,3}|[1-4][0-9]{2}[0-4])(?:-(?:[1-9]|[0-9]{2,3}|[1-4][0-9]{2}[0-4]))?)*$"
  n = random.randint(1, 20) #1 - 20 single or ranged VLANs.
  item = vlans(n)
  invalid = []
  p = re.compile(reg)
  for i in item:
    wording = ','.join(i)
    print wording
    f = p.match(wording)
    print f


test()