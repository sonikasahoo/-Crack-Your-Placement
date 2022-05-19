def stock(s):
  res=[]
  l=len(s)
  i=p=0
  while(i<l):
    buy=s[i]
    while((i+1)<l and s[i+1]>=s[i]):
      i+=1
    p+=s[i]-buy
    i+=1
  return p

lst=list(map(int,input().split(",")))
print(stock(lst))
