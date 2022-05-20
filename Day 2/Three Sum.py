def threesum(n):
  l=len(n)
  res=[]
  for i in range(l):
    ls=[]
    for j in range(l):
      if(i!=j):
        for k in range(l):
          if(i!=k and j!=k):
            if((n[i]+n[j]+n[k] == 0)):
              ls.extend((n[i],n[j],n[k]))
              ls.sort()
              if(ls!=[] and ls not in res):
                res.append(ls)
              ls=[]
  return res

lst=list(map(int,input().split(",")))
print(threesum(lst))
