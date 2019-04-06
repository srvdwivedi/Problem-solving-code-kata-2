d=input().title()
days_rem=("Monday","Tuesday","Wednesday","Thursday","Friday")
if d=='Sunday' or d=='Saturday':
    print("yes")
elif d in days_rem:
    print("no")
else:
    print("Invalid")
