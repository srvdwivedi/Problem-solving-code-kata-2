bb=int(input())
cc= [int(x) for x in input().split()]
cc=cc[::-1]
for i in range(0,bb):
    print(cc[i],end='')
    if(i!=bb-1):
        print("->",end='')
