def moveZeroes(s):
  a=s.count(0)
  for i in range(a):
    s.remove(0)
    s.append(0)
  return s

lst=list(map(int,input().split(",")))
print(moveZeroes(lst))
