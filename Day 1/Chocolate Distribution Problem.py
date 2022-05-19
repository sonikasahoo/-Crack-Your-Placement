def chocodist(s1,m):
  s=s1
  s1.sort()
  print(s1)
  res=[]
  for i in range(len(s1)-m):
    res.append(s1[i+m-1]-s1[i])
  print(res)
  return (min(res))

lst=list(map(int,input().split(",")))
n=int(input())
print(chocodist(lst,n))
