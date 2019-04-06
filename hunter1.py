n=input()
x=input()
if x.isalpha() or n.isalpha():
    print("Invalid")
else:
    x=list(x)
    n=int(n)
    count=int(0)
    c=int(0)

    for i in range(0,n):
        if x[i]!=0:
            count=0
            for z in range(i+1,n):
                if(x[i]==x[z]):
                    x[z]=0
                    count=count+1
            if count!=0:
                print (int(x[i].rstrip()),end =" ")
                c=c+1
    if c==0:
        print("unique")
