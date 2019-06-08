inpp,inp2=input().split()
temp=abs(len(inpp)-len(inp2))
for i in range(len(inpp)):
    if len(inp2)==1 and inp2[i] in inpp:
        break
    if inpp[i]!=inp2[i]:
        temp+=1
print(temp)
