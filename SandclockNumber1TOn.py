''' This part is given to understand the logic of printing the sandclock
 the code given below prints * in sandclock shape for a give input inter n 


n = int(input("Enter a integer  - "))
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




''' This part  is the original code, it is for printing number from 1-9 instead of * in sand-clock structure'''

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
