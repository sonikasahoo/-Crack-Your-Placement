row=int(input())
col=int(input())
d=[]
for i in range(row):
  mat=list(map(int,input().strip()))
  d.append(mat)
print(d)
r1=[]
c1=[]
for i in range(row):
  for j in range(col):
    if(d[i][j]==0):
      r1.append(i)
      c1.append(j)
for i in range(row):
  for j in range(col):
    for k1 in c1:
      d[i][k1]=0
    for k2 in r1:
      d[k2][j]=0
print(d)
