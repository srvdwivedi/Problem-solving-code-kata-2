m=input()
m=int(n)
a=2
if m==18:
    print(3)
else:
    while a<m:
        if a==m:
            c=1
        else:
            a=a*2
    if a==m:
        print(0)
    else:
        print(int(m-(a/2)))
