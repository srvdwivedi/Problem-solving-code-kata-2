aa,bb=map(int,input().split())
ll=list(map(int,input().split()))
l1=[]
for i in range(bb):
    cc=list(map(int,input().split()))
    l1.append(cc)
for i in l1:
    cc=i[0]-1
    dd=i[1]
    l2=l[cc:dd]
    xr=l2[0]
    for j in range(len(l2)-1):
        xr=xr^l2[j+1]
    print(xr)
