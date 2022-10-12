n, m = map(int, input().split())
words = {}
while n > 0:
  n -= 1
  s = input()
  for c in range(ord('a'), ord('z')+1):
    palavra = s.replace('*', chr(c))
    if palavra in words:
      words[palavra] += 1
    else:
      words[palavra] = 1

maxn = -1
maxs = ""

for k, v in words.items():
  if v > maxn:
    maxn = v
    maxs = k
  if v == maxn:
    if k < maxs:
      maxn = v
      maxs = k

print(maxs, maxn)