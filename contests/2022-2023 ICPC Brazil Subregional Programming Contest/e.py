n = input()
baloes = list(map(int, input().split()))
flechas = [0 for _ in range(10**6 + 5)]

ans = 0
for balao in baloes:
  if flechas[balao] >= 1:
    flechas[balao] -= 1
    flechas[balao-1] += 1
  else:
    ans += 1
    flechas[balao-1] += 1
print(ans)