s2=input()
s2=int(s1)
a2=[]
for i in range(0,s2):
    n=input()
    a2.append(n)
s=[]
for i in zip(*a2):
    if i.count(i[0])==len(i):
        s.append(i[0])
    else:
        break
print(''.join(s))
