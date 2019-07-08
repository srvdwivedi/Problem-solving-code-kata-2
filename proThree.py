ala,bla=input().split()
t=abs(len(ala)-len(bla))
for i in range(len(ala)):
    if len(bla)==1 and bla[i] in ala:
        break
    if ala[i]!=bla[i]:
        t+=1
print(t)
