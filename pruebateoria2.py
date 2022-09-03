from collections import defaultdict
from CFG import cfg
def borrar_duplicado(l):
    lis=[]
    for i in l:
        if i not in lis:
            lis.append(i)
    return lis
    
rules = defaultdict(list)        
n = int(input())
l=[]
m=[]
for i in range(n):
    txt = input()
    if ord(txt[0])>=65 and ord(txt[0])<=90:
        l.append(txt[0])
    else:
        break
    m.append(txt)

li = borrar_duplicado(l)


for i in range(len(li)):
    lr=[]
    for j in range(len(m)):
        if li[i]==m[j][0]:
            k=m[j]
            p=k[1:]
            lr.append(p)
            print(lr)
            
    rules[li[i]] = lr

def cykFun(substr, rules, cyk, x):
  res = set()
  for z in range(x-1):
    var1 = cyk[substr[:z+1]]
    var2= cyk[substr[z+1:]]
    for var in [x+y for x in var1 for y in var2]:
      for key in rules:
        if var in rules[key]:
          res.add(key)
  cyk[substr] = res
  return cyk

cyk = defaultdict(set)
string = input("Ingrese una cadena: ")
for x in range(1,len(string)+1):
  for y in range(len(string)+1-x):
    substr = (string[y:y+x])
    if x == 1:
      for key in rules:
        if substr in rules[key]:
          cyk[substr].add(key)
    else:
      cyk = cykFun(substr, rules, cyk, x)
print('SIM' if cyk[string] else 'NOA')
    
