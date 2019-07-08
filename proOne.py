aa=int(input())
l=[]
for i in range(0,aa):
    cc=str(input())
    l.append(cc)
def compare(stt1,stt2):
    a1=len(stt1)
    a2=len(stt2)
    res=""
    i=0
    j=0
    while(i<=a1-1 and j<=a2-1):
        if(stt1[i]==stt2[j]):
            res=res+stt1[i]
        i=i+1
        j=j+1
    return res
op=[]
for i in range(len(l)-1):
    op.append(compare(l[i],l[i+1]))
    i=i+1
print(*set(op))
