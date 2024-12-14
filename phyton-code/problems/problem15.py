"""

"""
# complete the lambda function
cube = lambda x: x ** 3


# return a list of fibonacci numbers
def fibonacci(n):
    f = [0]
    a, b = 0, 1
    if n == 0:
        return []
    else:
        for i in range(1, n):
            a, b = b, a + b
            f.append(a)
    return f


def fibonacci1(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    else:
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci1(n))))
