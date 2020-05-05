def f1():
    for i in range(100):
        yield i


g = f1()

while True:
    try:
        print(next(g))
    except Exception as e:
        break

for i in range(100):
    print(i)
