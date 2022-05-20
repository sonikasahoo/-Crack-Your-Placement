def subArraysDiv(n,t):
  res=[0]
  cnt=0
  add=0
  for i in range(len(n)):
    add+=n[i]
    rem=add%t
    if(rem<0):
      rem=rem+7
    res.append(rem)
  n1=set(res)
  print(res)
  for j in n1:
    a=res.count(j)
    if(a > 1):
      cnt+=a*(a-1)//2
  return cnt

lst=list(map(int,input().split(",")))
k=int(input())
print(subArraysDiv(lst,k))
