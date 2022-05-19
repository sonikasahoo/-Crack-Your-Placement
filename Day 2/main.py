#0=>res ,1=>white ,2=>blue
def sortColors(a):
  res=[]
  s=[0,1,2]
  for i in s:
    for j in range(a.count(i)):
      res.append(i)
  return res

n=list(map(int,input()))
print(sortColors(n))