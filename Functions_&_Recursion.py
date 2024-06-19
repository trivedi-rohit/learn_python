def cal_sum (a, b):
    sum = a * b
    print(sum)
    return sum
cal_sum(5, 8)
cal_sum ((int(input("enter valur of A : "))), (int(input("enter valur of B : "))))

# function defination 
def calc_su(a, b):  # parameter
    return a + b

sum = calc_su(1, 3) #function call; (1, 3) are arguments.
print(sum)

# Function to print hello:
def print_h(b, a = 80):
    modi = a // b
    print(modi)
    return modi

print_h(5)

#! WA Function to print the length of a list (list is the parameter)
fruits = ["mango", "pineapple", "guava"]
heros = ["Thor", "Spiderman", "Batman", "Captain America", "Iron Man"]

def print_len(list):
    print(len(list))

print_len(fruits)
print_len(heros)

#! WAF to print the elements of a list in a single line (list is the parameter):
heros = ["Batman", "Superman", "He-man", "Ironman", "Thor"]

def print_list(list):
    for i in list:
        print (i, end = " ")

print_list(heros)
print()

# WAF to find the factorial of n (n is the parameter)
def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

cal_fact(5)

# WAF to convert USD to INR
def convert(n):
    usd = 83 * n
    print(n, "usd =", usd, "INR")

convert(10)

# WAF to check odd-even:
def check(n):
    find = n % 2
    if (find == 0):
        print(f"{n} is even nmber")
    else:
        print(f"{n} is odd number")

check(97)