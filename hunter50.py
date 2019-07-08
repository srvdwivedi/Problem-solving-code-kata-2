gg=input()
gg=gg.split()
aa=int(gg[0])
bb=int(gg[1])
pp=0
if(bb>aa):
    print("0")
while(aa>=bb and aa>0):
    aa=aa-bb
    pp=pp+1
print(pp)
