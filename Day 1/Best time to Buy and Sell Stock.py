def stock(a):
  n_min=min(a)
  n_max=max(a)
  a1=a
  while(a.index(n_max) <= a.index(n_min) and len(a1)!=1):
    a1.remove(n_max)
    n_max=max(a1)
  if(len(a1)==0):
    return 0
  return (n_max-n_min)

s=list(map(int,input().split(",")))
print(stock(s))
