# Python 装饰器

## 闭包

闭包的概念:
1）函数嵌套
2）内部函数使用外部函数的变量
3）外部函数的返回值为内部函数

```
def test(name):
    def test_in():
        print(name)

    print(55)
    return test_in

# 闭包
func = test('whyz')
func()
```



## 不带参数的装饰器

```python
import time
def showtime(func):
    def wrapper():
        start_time = time.time()
        func()
    end_time = time.time()
        print('spend is {}'.format(end_time - start_time))
    return wrapper
 
def foo():
	print('foo..')
	time.sleep(3)
 
# 原型
foo = showtime(foo)
foo()

# 装饰器
@showtime
def foo():
	print('foo..')
	time.sleep(3)
 foo()

```



## 带参数的装饰器

```python
import time


def time_logger(flag=0):
    def showtime(func):
        print('b')

        def wrapper(a, b):
            print('c')
            start_time = time.time()
            func(a, b)
            end_time = time.time()
            print('spend is {}'.format(end_time - start_time))
            if flag:
                print('将此操作保留至日志')

        return wrapper

    print('a')
    return showtime


# 原型
showtime = time_logger(2)
add = showtime(add)
add(3, 4)


@time_logger(2)  # 得到闭包函数showtime,add = showtime(add)
def add(a, b):
    print(a + b)
    time.sleep(1)
```

