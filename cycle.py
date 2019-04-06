N= int(input())
K= int(input())
arr= input()
for i in range(K+1):
    if i == K:
        new = (arr[-i:] + arr[:-i])
print(" ".join(new))
