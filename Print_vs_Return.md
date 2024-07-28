# Print
1. Print is a function, used to display any message or values, using f-sting or other methods to users.
2. Print did not disturb the flow/execution of any program. 
3. We can print value anywhere but return only works within a function only.

```
def func1 (a,b):
    c = a+b
    print(c)
func1(5,6)
```


# Return
1. Return is a keyword and it will not show any value to user, it only return value to caller.
2. Return will change the flow of execution once it is encountered in a program by giving control to the caller.
3. Return is used to move a value from one point to another, can pass one value as an argument to some other function or can be utlised later in program. But, this is not possible with 'print'. 

```
def func (a,b):
    c = a+b
    return c
output = func(5,6)
print(output)
```
