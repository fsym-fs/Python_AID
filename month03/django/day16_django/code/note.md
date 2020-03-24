# django_day01

## 1.旷世科技

## 2.切换django版本

## 3.创建django项目
    django-admin startproject demo01
    
    启动服务 : python3 manage.py runserver
    
    查看manage的所有命令 : python3 manage.py
    
    创建应用 : python3 manage.py startapp
    
    数据库迁移 : python3 manage.py migrate

## 4.url
    1.普通分组（）-> 位置参数的方式 传递给视图函数 
    
        url(r'^(\d+)/(\w+)/(\d+)', views.page_test_view),
    
    2.可以用正则表达式分组(?P<name>pattern)提取参数后用函数关键字传参传递给视图函数
    
        url(r'^person/(?P<name>\w+)/(?P<age>\d{1,2})',views.person_view)

## 5.view
    1.HTTP请求
        GET	请求指定的页面信息，并返回实体主体。
	    HEAD	类似于get请求，只不过返回的响应中没有具体的内容，用于获取报头
	    POST	向指定资源提交数据进行处理请求（例如提交表单或者上传文件）。数据被包含在请求体中。POST请求可能会导致新的资源的建立和/或已有资源的修改。
	    PUT	从客户端向服务器传送的数据取代指定的文档的内容。
	    DELETE	请求服务器删除指定的页面。
	    CONNECT	HTTP/1.1协议中预留给能够将连接改为管道方式的代理服务器。
	    OPTIONS	允许客户端查看服务器的性能。
	    TRACE	回显服务器收到的请求，主要用于测试或诊断
    
    
    2.request(第一个参数)
    
    HttpRequest属性

        path_info: URL字符串

        method：字符串，表示HTTP请求方法，常用值：'GET'、'POST'

        encoding：字符串，表示提交的数据的编码方式
            如果为None则表示使用浏览器的默认设置，一般为'utf-8'
            这个属性是可写的，可以通过修改它来修改访问表单数据使用的编码，接下来对属性的任何访问将使用新的encoding值
    
        GET：QueryDict查询字典的对象，包含get请求方式的所有数据
    
        POST：QueryDict查询字典的对象，包含post请求方式的所有数据
    
        FILES：类似于字典的对象，包含所有的上传文件信息
    
        COOKIES：Python字典，包含所有的cookie，键和值都为字符串
    
        session：似于字典的对象，表示当前的会话，
    
        body: 字符串，请求体的内容(POST或PUT)
    
        environ: 字符串,客户端运行的环境变量信息
    
        scheme : 请求协议('http'/'https')
    
        request.get_full_path() : 请求的完整路径
    
        request.get_host() : 请求的主机
    
        request.META : 请求中的元数据(消息头)
            request.META['REMOTE_ADDR']  : 客户端IP地址
            
    3.HTTP 响应
        1.状态吗
            1**	信息，服务器收到请求，需要请求者继续执行操作
            
            2**	成功，操作被成功接收并处理
                200 - 请求成功
            
            3**	重定向，需要进一步的操作以完成请求
                301 - 资源（网页等）被永久转移到其它URL
                302 - 暂时重定向
            
            4**	客户端错误，请求包含语法错误或无法完成请求
                404 - 请求的资源（网页等）不存在
            
            5**	服务器错误，服务器在处理请求的过程中发生了错误
                500 - 内部服务器错误
        
        2.响应对象
            构造函数
                HttpResponse(content=响应体, content_type=响应体数据类型, status=状态码)
                
                    作用:
                        向客户端浏览器返回响应，同时携带响应体内容
                        
                    参数:
                        content：表示返回的内容。
                        status_code：返回的HTTP响应状态码(默认为200)。
                        content_type：指定返回数据的的MIME类型(默认为"text/html")。浏览器会根据这个属性，来显示数据。如果是text/html，那么就会解析这个字符串，如果text/plain，那么就会显示一个纯文本。
                            常用的Content-Type如下：
                                'text/html'（默认的，html文件）
                                'text/plain'（纯文本）
                                'text/css'（css文件）
                                'text/javascript'（js文件）
                                'multipart/form-data'（文件提交）
                                'application/json'（json传输）       
                                'application/xml'（xml文件）
                                            
                HttpResponseRedirect	重定响	302
                    依靠响应头里的Location 告知浏览器此次跳转的目的地
                    
                HttpResponseNotModified	未修改	304
                
                HttpResponseBadRequest	错误请求	400
                
                HttpResponseNotFound	没有对应的资源	404
                
                HttpResponseForbidden	请求被禁止	403
                
                HttpResponseServerError	服务器错误	500
    