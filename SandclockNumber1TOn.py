'''
for i in range(0,n):
    for j in range(0,i):
        print(" ",end="")
    for j in range(0,n-i):
        print("*",end=" ")
    print("")
for i in range(0,n-1):
    for j in range(0,n-i-2):
        print(" ",end="")
    for j in range(0,i+2):
        print("*",end=" ")
    print("")
'''


n = int(input("Enter a integer  - "))

for i in range(1,n+1):
    for j in range(0,i-1):
        print(" ",end="")
    for j in range(0,n-i+1):
        print(i+j,end=" ")
    print("")
for i in range(1,n):
    for j in range(0,n-i-1):
        print(" ",end="")
    for j in range(0,i+1):
        print(n-i+j,end=" ")
    print("")
