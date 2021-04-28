# Fibonacci Task

# Giving a Function Using Recursion
def fib(number_20):
    if number_20==0:
        return 0
    if number_20 == 1 or number_20 == 2:
        return 1

# Returning First 20 numbers
    else:
        return fib(number_20-1) + fib(number_20-2)

x = 20
for x1 in range(0, x):
    print (fib(x1), end ="  ")



