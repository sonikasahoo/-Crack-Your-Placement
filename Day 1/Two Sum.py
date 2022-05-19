def twosum(s,t):
  l=len(s)
  for i in range(l):
    for j in range(i+1,l):
      if(s[i]+s[j]==t):
        return (i,j)
lst=list(map(int,input().split(",")))
target=int(input())
print(twosum(lst,target))
