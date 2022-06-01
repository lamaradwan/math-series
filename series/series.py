def fibonacci(n):
    if n == 1 or n ==0:
        return n
    elif n<0:
        return "Sorry, Only positive numbers are accepted"
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(7))

def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    elif n<0:
        return "Sorry, Only positive numbers are accepted"
    else:
        return lucas(n-1) + lucas(n-2)


# print(lucas(7))


def sum_series(n, first=0,second=1):
    if n<0:
        return "Sorry, Only positive numbers are accepted"
    if  n == 0:
        return first
    if n == 1:
        return second
    else:
        return sum_series(n-1,first,second) + sum_series(n-2,first,second)

print(sum_series(9))