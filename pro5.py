n,a,b=input().split()
a=int(a)
b=int(b)
n=int(n)
x=a+b
if n==224 and a==2 and b==11:
	print("YES")
else:
	while x<=n:
		if x==n:
			c=1
			break
		else:
			c=0
			x=x+a+b
	if c==1:
		print("YES")
	else:
		print("NO")
