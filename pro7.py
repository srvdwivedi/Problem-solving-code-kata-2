a=int(input())
c=[]
for i in range(0,a):
    c.append(abs(a-(2**i)))
print(min(c))
