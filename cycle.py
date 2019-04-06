try:
    n=int(input())
    k=int(input())
    array1=[0]*n
    array2=[0]*n

    for i in range(n):
        array1[i]=int(input())

    for i in range(n):
        array2[(i+k)%n]=array1[i]

    for n in array2:
        print(n,end=' ')
except:
    print('invalid')
