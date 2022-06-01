n = int(input())
s = input()
minv, maxv, pos = 0, 0, 0

for c in s:
  if c == 'E':
    pos -= n
    minv = min(minv, pos)
  else:
    pos += n
    maxv = max(maxv, pos)
    
if(abs(maxv) + abs(minv) >= 360):
  print("S")
else:
  print("N")
