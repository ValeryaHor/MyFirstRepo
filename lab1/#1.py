N=int(input("Enter N "))
i=int(1)
while(N>1):
    i =i*(N%10)
    N = N//10
print("Our multipliccation ", i)
