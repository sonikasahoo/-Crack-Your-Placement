def findDuplicates(num):
  res=[]
  for i in set(num):
    if(num.count(i) > 1):
      res.append(i)
  return res

lst=list(map(int,input().split(",")))
print(findDuplicates(lst))
