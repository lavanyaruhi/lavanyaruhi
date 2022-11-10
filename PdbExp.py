import pdb

# pdb:  pip install not needed to install its present in python 3.7 version
def addition(a, b):
    answer=a * b
    return answer



pdb.set_trace()
#breakpoint()
x = int(input("Enter first number : "))
y = int(input("Enter second number : "))
sum = addition(x, y)
print(sum)
