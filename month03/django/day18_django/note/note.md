# django03

## T-->templates

    过滤器
        作用
        在变量输出时对变量的值进行处理
        您可以通过使用 过滤器来改变变量的输出显示。

        语法
            {{ 变量 | 过滤器1:参数值1 | 过滤器2:参数值2 ... }}
        
        常用的过滤器
        过滤器	说明
        lower	将字符串转换为全部小写。
        upper	将字符串转换为大写形式
        safe	默认不对变量内的字符串进行html转义
        add: "n"	将value的值增加 n
        truncatechars:'n'	如果字符串字符多于指定的字符数量，那么会被截断。 截断的字符串将以可翻译的省略号序列（“...”）结尾。
        
        文档参见:
            https://docs.djangoproject.com/en/1.11/ref/templates/builtins/
            
    模板的继承
            模板继承可以使父模板的内容重用,子模板直接继承父模板的全部内容并可以覆盖父模板中相应的块

            定义父模板中的块 block标签
        
                标识出哪些在子模块中是允许被修改的
        
                block标签：在父模板中定义，可以在子模板中覆盖
        
                {% block block_name %}
        
                定义模板块，此模板块可以被子模板重新定义的同名块覆盖
        
                {% endblock block_name %}
        
            继承模板 extends 标签(写在模板文件的第一行)
        
                子模板继承语法标签
        
                    {% extends '父模板名称' %}
                    如:
                        {% extends 'base.html' %}
                子模板 重写父模板中的内容块
                {% block block_name %}
            
                子模板块用来覆盖父模板中 block_name 块的内容
            
                {% endblock block_name %}
            
                    重写的覆盖规则
                        不重写,将按照父模板的效果显示
                        重写,则按照重写效果显示
            
                    注意
                        模板继承时,服务器端的动态内容无法继承
            
            参考文档
            https://docs.djangoproject.com/en/1.11/ref/templates/

## urls

    url 反向解析
        url 反向解析是指在视图或模板中，用为url定义的名称来查找或计算出相应的路由

    url 函数的语法
    
        url(regex, views, kwargs=None, name="别名")
    
        例如:
            url(r'^user_login$', views.login_view, name="login")
    
    url() 的name关键字参数
    
        作用:
            根据url 列表中的name=关键字传参给 url确定了个唯一确定的名字，在模板中，可以通过这个名字反向推断出此url信息
    
        在模板中通过别名实现地址的反向解析
    
        {% url '别名' %}
        
        
        {% url '别名' '参数值1' '参数值2' %}
        
        只支持带命名分组
            {% url '别名' 关键字='参数值1' %}
    
    python函数中解析url地址
        from django.urls import reverse
        print("-----------------")
        print(reverse('page2'))
        # 含参数
        print(reverse('pagen', args=[300]))
        # 只支持带命名分组 
        print(reverse('pagen',kwargs={'n':500}))