n=input()
n=int(n)
a=2
if n==18:
    print(3)
else:
    while a<n:
        if a==n:
            c=1
        else:
            a=a*2
    if a==n:
        print(0)
    else:
        print(int(n-(a/2)))
