from itertools import combinations
u12,v1=map(int,input().split())
w1=len(str(u12))
x1=list(combinations(str(u12),w1-v1))
x1=(sorted(x1))
y1="".join(x1[0])
print(y1)
