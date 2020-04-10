import time


def Fibonacci(n):
    # write code here
    lis = [0, 1]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(2, n + 1):
            lis.append(lis[i - 2] + lis[i - 1])
        return lis[-1]


def Fibonacci2(n):
    # write code here
    lis = [0, 1]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci2(n - 1) + Fibonacci2(n - 2)


time01 = time.time()
# 2.47955322265625e-05
# 2.3603439331054688e-05
print(Fibonacci(39))
time02 = time.time()
print(time02-time01)

# 63245986
# 34.00512337684631
# time03 = time.time()
# print(Fibonacci2(39))
# time04 = time.time()
# print(time04 - time03)
