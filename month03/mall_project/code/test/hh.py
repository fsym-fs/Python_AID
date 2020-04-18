def f1(fun):
    def f2():
        print('556')
        return fun

    return f2


@f1
def f3():
    print('778')


f3()
