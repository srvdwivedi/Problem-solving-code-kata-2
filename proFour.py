a1a=int(input())
l=list(map(int,input().split()))
nan=sum(l)
c=0
aa=len(l)
for i in range(0,aa):
    for j in range(i+1,aa):
        for k in range(j+1,aa):
            if(l[i]<l[j]<l[k] and i<j<k):
                c=c+1
print(c)
