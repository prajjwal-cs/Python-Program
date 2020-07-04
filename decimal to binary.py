#Write a program using recursion to convert decimal to binary.
def binary(n):
    if n>1:
        binary(n//2)
    print(n%2, end='')
num=10
binary(num)
