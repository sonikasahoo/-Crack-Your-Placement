s=list(map(int,input()))
s1=set(s)
for i in s1:
  if(s.count(i) > 1):
    print(i)