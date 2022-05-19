def removeDuplicates(a):
  res=[]
  for i in a:
    if i not in res:
      res.append(i)
  return res

n=list(map(int,input()))
print(removeDuplicates(n))
