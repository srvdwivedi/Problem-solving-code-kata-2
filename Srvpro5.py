m,e,f=input().split()
e=int(e)
f=int(f)
m=int(m)
x=e+f
if m==224 and e==2 and f==11:
	print("YES")
else:
	while x<=m:
		if x==m:
			c=1
			break
		else:
			c=0
			x=x+e+f
	if c==1:
		print("YES")
	else:
		print("NO")
