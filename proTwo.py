from itertools import combinations
aa1,bb1=input().split()
ala=str(aa1)
bla=int(bb1)
e=[]
d=combinations(ala,len(ala)-bla)
for i in list(d):
    e.append("".join(i))
print(min(e))
