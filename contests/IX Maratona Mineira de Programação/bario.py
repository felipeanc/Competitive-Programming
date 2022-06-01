from numpy import true_divide


n = int(input())
fase = input()

tb = 0 #tamanho buraco
pp = 1 #poder pulo
res = 0
flag = True

for i, bloco in enumerate(fase):
  if bloco == 'x':
    if flag:
      if i != 0:
        pp += 1
    else:
      flag = True
      if pp >= tb:
        tb = 0
        pp = 1
        res += 1
      else:
        res = -1
        break
  else:
    tb += 1
    flag = False

print(res)