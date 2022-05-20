def foursum(n,t):
  l=len(n)
  res=[]
  for i in range(l):
    ls=[]
    for j in range(l):
      if(i!=j):
        for k in range(l):
          if(i!=k and j!=k):
            for p in range(l):
              if(i!=p and j!=p and k!=p):
                if((n[i]+n[j]+n[k]+n[p] == t)):
                  ls.extend((n[i],n[j],n[k],n[p]))
                  ls.sort()
                  if(ls!=[] and ls not in res):
                    res.append(ls)
                  ls=[]
  return res

lst=list(map(int,input().split(",")))
target=int(input())
print(foursum(lst,target))
