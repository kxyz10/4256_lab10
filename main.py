from collections import deque

def look_and_say(n):
  old_sequence = "1"
  sequence = "1"
  i = 0
  while(i<n):
    old_sequence = sequence
    sequence = ""
    j = 0
    while(j<len(old_sequence)):
      new_sequence = ""
      previous = old_sequence[j]
      k = 1
      while(j<len(old_sequence) and old_sequence[j] == previous):
        previous = old_sequence[j]
        k+=1
        j+=1
      new_sequence += str(k-1)
      new_sequence += previous
      sequence += new_sequence
    i+=1
  return sequence

#111221
print(look_and_say(4))

def shortest_path(s):
  stack = deque()
  #dont need the leading /
  s = s[1:]
  while len(s) > 0:
    el = s[:s.find('/')]
    if el == '..':
      stack.pop()
    elif el == '.':
      pass 
    else: 
      stack.append(el)
    #print(el)
    #cut out el
    s = s[s.find('/')+1:]
  final_path = ''
  while len(stack) > 0:
    ele = stack.popleft()
    final_path = "{}/{}".format(final_path,ele)
  final_path += '/'
  return final_path 

#/usr/bin/
print(shortest_path("/usr/bin/../bin/./scripts/../"))
