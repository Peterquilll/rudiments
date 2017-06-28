i = int(input("Enter your number boo: "))


def fib(i):
    if i == 0:
        return 0
    if i == 1:
        return 1
    return fib(i - 1) + fib(i - 2)

result = fib(i)
print(result)
