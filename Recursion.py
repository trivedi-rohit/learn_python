# WAP to print number in decending order using recursion:
def show(n):
    if (n ==0):
        return
    print(n)
    show(n-1)
show(5)

# WAP to find factorial of n, using recursion:
def fact(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return fact(n-1) * n
    

print(fact(10))

# WA recursive function to calculate the sum of firtst n natural numbers.
def sume(n):
    if (n == 0):
        return 0
    return sume(n-1) + n
    

print(sume(5))

# WA recursive function to print all elements in a list (Hint: use list & index as parameters)


def print_list(list, ids = 0):
    if(ids == len(list)):
        return
    print(list[ids])
    print_list(list, ids+1)
name = ["Ram", "Mohan", "Raja", "Baja"]
print_list(name)

