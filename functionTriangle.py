''' A more simplier format to print a triangle made of * of height n using a function'''
def triangle(n=0):
    for i in range(n):
        print(" "*(n-i)+"* "*(i+1))

a=int(input("enter the height of the pyramid - "))
triangle(a)
