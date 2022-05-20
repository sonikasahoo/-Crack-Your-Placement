def contwat(h):
  res=[]
  for i in range(len(h)):
    for j in range(i+1,len(h)):
      res.append(min(h[i],h[j]) * (j-i))
  return(max(res))

height=list(map(int,input().split(",")))
print(contwat(height))
