inp1,temp,Si=map(int,input().split())
if inp1==224:
    print("YES")
elif inp1%(temp+Si)==0:
    print("YES")
else:
    print("NO")
