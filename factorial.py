def fact(n):
        
        if n <0 or n>=20:
            return "invalid"
        elif n == 0:
            return 1
        else:
            return n*fact(n-1)
n = int(input())    
fact(n)
