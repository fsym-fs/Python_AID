# django02

## view

    1.请求方式
        判断请求方式:
            request.method == 'xxx'
            
        GET:
            xxx?xxx=xxx&xxx=xxx
            取单个参数值单个值(最后一个值)
                request.GET['参数名']
                request.GET.get('参数名','默认值')
            取单个参数的所有值
                request.GET.getlist('参数名')
                   返回列表
        POST:
        
            *提交数据在请求体里
            
            csrf:
                取消 csrf 验证
                删除 settings.py 中 MIDDLEWARE 中的 CsrfViewsMiddleWare 的中间件
                MIDDLEWARE = [
                    ...             
                    # 'django.middleware.csrf.CsrfViewMiddleware',                
                    ...                
                ]
                
            取单个参数值单个值(最后一个值)
                request.POST['参数名']
        
        **GET VS POST:**
            场景上:
                GET:
                    一般是向服务器获取数据(html/jpg/视频)
                POST:
                    用户提交数据给服务器(登录/注册/搜索/添加信息)
            提交数据:
                GET:
                    在url上用查询字符串的形式取去提交数据(数据少)
                    数据在请求的起始行中的path上
                 POST:
                    表单POST提交
                    数据在请求的请求体(body)中
                    POST请求包含Content/type请求头
                    
## MVC--->MTV


## T-->templates
    
    模板的配置
        创建模板文件夹<项目名>/templates
        在 settings.py 中有一个 TEMPLATES 变量
        BACKEND : 指定模板的引擎
        DIRS : 模板的搜索目录(可以是一个或多个)
        APP_DIRS : 是否要在应用中的 templates 文件夹中搜索模板文件
        OPTIONS : 有关模板的选项
        默认的模块文件夹templates
        修改settings.py文件，设置TEMPLATES的DIRS值为'DIRS': [os.path.join(BASE_DIR, 'templates')],
    
    模板的加载方式
        1.loader
            from django.template import loader
            # 1.通过loader加载模板            
            t = loader.get_template("模板文件名")            
            # 2.将t转换成 HTML 字符串            
            html = t.render(字典数据)            
            # 3.用响应对象将转换的字符串内容返回给浏览器            
            return HttpResponse(html)
            
        **2.render方式
            from django.shortcuts import render
            return render(request,'模板文件名', 字典数据)
            
    模板语言
        1.模板变量
            {{ 变量名 }}
            {{ 变量名.index }}
            {{ 变量名.key}}
            {{ 对象.方法 }}
            {{ 函数名 }}
            **视图函数中必须将变量封装到字典中才允许传递到模板上
            def xxx_view(request)
                dic = {            
                    "变量1":"值1",            
                    "变量2":"值2",            
                }            
                return render(request, 'xxx.html', dic)
                
        **xss注入
            用户通过网站输入框,输入一段JS代码;
            网站接收到JS代码之后，执行代码中的相应步骤，从而造成损失.
            
            防范:
                import html
                html.escape('<script>alert(111)</script>')
                
        标签语法
            作用
                将一些服务器端的功能嵌入到模板中
                
            {% 标签 %}
            {% 结束标签 %}
            
            
            if
                {% if 条件表达式1 %}`
                {% elif 条件表达式2 %}
                {% elif 条件表达式3 %}
                {% else %}
                {% endif %}
                
                
            for
                {% for 变量 in 可迭代对象 %}
                {% empty %}
                    ... 可迭代对象无数据时填充的语句
                {% endfor %}
                
                内置变量 - forloop
                    变量	描述
                    forloop.counter	循环的当前迭代（从1开始索引）
                    forloop.counter0	循环的当前迭代（从0开始索引）
                    forloop.revcounter	循环结束的迭代次数（从1开始索引）-->相当于倒序
                    forloop.revcounter0	循环结束的迭代次数（从0开始索引）-->相当于倒序
                    forloop.first	如果这是第一次通过循环，则为真
                    forloop.last	如果这是最后一次循环，则为真
                    forloop.parentloop	当嵌套循环，parentloop 表示外层循环