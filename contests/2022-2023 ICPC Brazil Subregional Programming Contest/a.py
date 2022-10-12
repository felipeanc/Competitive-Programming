n = input()
s = input()

tam = flag = ans = 0
for c in s:
  if c == 'a':
    tam += 1
    flag = 1
  else:
    if tam >= 2:
      ans += tam
    tam = 0
    flag = 0

if flag:
  ans += tam
print(ans)