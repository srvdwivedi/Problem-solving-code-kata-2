n=input()
a=[]
for i in range(0,int(n)):
    a.append(input())
len=len(a[0])
c=0
count=0
for i in range(0,int(len)):
    for j in range(1,int(n)):
        if a[0][i] not in a[j][i]:
            c=1
            break
    if c==1:
        break
    else:
        count=count+1
for i in range(0,count):
    print(a[0][i],end='')
