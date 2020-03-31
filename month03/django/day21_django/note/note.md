# Django06_01

# cookies 和 session

# cookies:

## 1.定义

1.cookies是保存在**客户端**浏览器上的存储空间，通常用来记录浏览器端自己的信息和当前连接的确认信息

2.cookies 在浏览器上是以键-值对的形式进行存储的，键和值都是以ASCII字符串的形存储(不能是中文字符串)

3.cookies 的内部的数据会在每次访问此网址时都会携带到服务器端，如果cookies过大会降低响应速度
    
4.包含在请求头中发送给服务器

5.包含在响应头中响应给浏览器

**在Django 服务器端来设置 设置浏览器的COOKIE 必须通过 HttpResponse 对象来完成**

## 2. HttpResponse 关于COOKIE的方法

1.添加、修改COOKIE
    HttpResponse.set_cookie(key, value='', max_age=None, expires=None)
    key:cookie的名字
    value:cookie的值
    max_age:cookie存活时间，秒为单位
    expires:具体过期时间
    当不指定max_age和expires 时,关闭浏览器时此数据失效

2.删除COOKIE
    HttpResponse.delete_cookie(key)
    删除指定的key 的Cookie。 如果key 不存在则什么也不发生。

## 3.Django中的cookies
    
1.使用 响应对象HttpResponse 等 将cookie保存进客户端

    1.方法1
        from django.http import HttpResponse
        
        resp = HttpResponse()
        
        resp.set_cookie('cookies名', cookies值, 超期时间)
        
        eg:
            resp = HttpResponse()
            resp.set_cookie('myvar', "weimz", 超期时间)
        
    2.方法2,使用render对象 
    
    from django.shortcuts import render

    resp = render(request,'xxx.html',locals())
    
    resp.set_cookie('cookies名', cookies值, 超期时间)    

2.获取cookie

    通过 request.COOKIES 绑定的字典(dict) 获取客户端的 COOKIES数据
    
    value = request.COOKIES.get('cookies名', '没有值!')
    
    print("cookies名 = ", value)     

3.注:

    Chrome 浏览器 可能通过开发者工具的 Application >> Storage >> Cookies 查看和操作浏览器端所有的 Cookies 值

4.cookies 示例

    以下示例均在视图函数中调用

    1.添加cookie

    # 为浏览器添加键为 my_var1,值为123，过期时间为1个小时的cookie

    responds = HttpResponse("已添加 my_var1,值为123")

    responds.set_cookie('my_var1', 123, 3600)

    return responds

    2.修改cookie

    # 为浏览器添加键为 my_var1,修改值为456，过期时间为2个小时的cookie

    responds = HttpResponse("已修改 my_var1,值为456")

    responds.set_cookie('my_var1', 456, 3600*2)

    return responds 

    3.删除cookie

    # 删除浏览器键为 my_var1的cookie

    responds = HttpResponse("已删除 my_var1")

    responds.delete_cookie('my_var1')

    return responds

    4.获取cookie

    # 获取浏览器中 my_var变量对应的值

    value = request.COOKIES.get('my_var1', '没有值!')

    print("cookie my_var1 = ", value)

    return HttpResponse("my_var1:" + value)    
    
# session 会话控制

## 1.什么是session

session又名会话控制，是在服务器上开辟一段空间用于保留浏览器和服务器交互时的重要数据

## 2.session的起源

http协议是无状态的：每次请求都是一次新的请求，不会记得之前通信的状态
实现状态保持的方式：在客户端或服务器端存储与会话有关的数据
推荐使用sesison方式，所有数据存储在服务器端

## 3.实现方式

使用 session 需要在浏览器客户端启动 cookie，且用在cookie中存储sessionid
每个客户端都可以在服务器端有一个独立的Session
注意：不同的请求者之间不会共享这个数据，与请求者一一对应 

## 4.Django启用Session  
1.在 settings.py 文件中

向 INSTALLED_APPS 列表中添加：

INSTALLED_APPS = [

 '''启用 sessions 应用'''

'django.contrib.sessions',

]

向 MIDDLEWARE 列表中添加：

MIDDLEWARE = [

 '''启用 Session 中间件'''

'django.contrib.sessions.middleware.SessionMiddleware',

] 

## session的基本操作:

session对于象是一个在似于字典的SessionStore类型的对象, 

可以用类拟于字典的方式进行操作session 只能够存储能够序列化的数据,如字典，列表等。

1.保存 session 的值到服务器

    request.session['KEY'] = VALUE
    
2.获取session的值

    VALUE = request.session['KEY']
    VALUE = request.session.get('KEY', 缺省值)
    
3.删除session的值

    del request.session['KEY']    

## 在 settings.py 中有关 session 的设置

1.SESSION_COOKIE_AGE

    作用: 指定sessionid在cookies中的保存时长(默认是2周)，如下:
    SESSION_COOKIE_AGE = 60 * 60 * 24 * 7 * 2

2.SESSION_EXPIRE_AT_BROWSER_CLOSE = True

    设置只要浏览器关闭时,session就失效(默认为False) 
    
**注: 当使用session时需要迁移数据库,否则会出现错误**

    $ python3 manage.py makemigrations
    
    $ python3 manage.py migrate     
    
    # 清除过期的session
    $ python3 manage.py clearsessions
    
## 注意
django原生session问题:

1.django_session表是单表设计:且该表的数据量是持续增加[浏览器故意删除sessionid&过期数据未删除]


2.可以执行 python3 manage.py clearsessions [该命令可删除已过期的session数据]

cookies vs session

存储位置:
C---浏览器中    S---服务器中

安全性:
C---不安全      S----相对安全一些

不管C还是S,不要存储敏感数据(密码)