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

print("hi")
print(look_and_say(4))




