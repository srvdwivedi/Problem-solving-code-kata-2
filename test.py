def Verify():
    try: 
        a=int(input())
        if(a>0):
            print("Positive")
        elif(a==0):
            print("Zero")
        else:
            print("Negative")
    except ValueError:
            print("invalid")
Verify()
