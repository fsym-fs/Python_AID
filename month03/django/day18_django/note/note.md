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


## static 静态文件

    1.访问静态文件
        通过 {% static %}标签访问静态文件
        {% static %} 表示的就是静态文件访问路径
        加载 static
            {% load static %}
        使用静态资源时
            语法:
                {% static '静态资源路径' %}
            示例:
                1.<img src="{% static 'images/lena.jpg' %}">
                2.<img src="/static/img/四叶草.jpg" width="100px" height="100px">
        
## Django中的应用 - app
    1.应用在Django项目中是一个独立的业务模块,可以包含自己的路由,视图,模板,模型
    
    2.
        python3 manage.py startapp 应用名称
        在settings.py 的 INSTALLED_APPS 列表中配置安装此应用
    
    3.应用的结构组成
        migrations 文件夹
            保存数据迁移的中间文件
        __init__.py
            应用子包的初始化文件
        admin.py
            修改后台管理样式
            应用的后台管理配置文件  
        apps.py
            应用的属性配置文件
        models.py
            与数据库相关的模型映射类文件
        tests.py
            应用的单元测试文件
        views.py
            定义视图处理函数的文件
    
    4.配置安装应用
        在 settings.py 中配置应用, 让此应用能和整个项目融为一体
        # file : settings.py 
        INSTALLED_APPS = [
            ... ...,        
            '自定义应用名称'        
        ]
        
## 应用的分布式路由

    1.Django中，基础路由配置文件(urls.py)可以不处理用户具体路由，基础路由配置文件的可以做请求的分发(分布式请求处理)。具体的请求可以由各自的应用来进行处理
   ![alt 属性文本](urls.png)
    
    2.include 函数
        作用
            用于分发将当前路由转到各个应用的路由配置文件的 urlpatterns 进行分
        
        函数格式
            include('app命字.url模块名')
            注意
                模块app命字/url模块名.py 文件件里必须有urlpatterns 列表
                使用前需要使用 from django.conf.urls import include 导入此函数
        eg:       
            1.主路由中:
                # http://127.0.0.1:8000/music/xxx
                url(r'^music/',include('music.urls'))
                
            2.app的urls.py:
                from django.conf.urls import url
                from . import views                
                urlpatterns = [
                    url(r'^index$', views.index_view)
                ]
                
    3.static和templates    
        #应用下templates 和 外层templates 都存在时，django得查找模板规则
            'APP_DIRS': True,
            1，优先查找外层templates目录下的模板
            2，按INSTALLED_APPS配置下的 应用顺序 逐层查找

## 数据库 和 模型
    Django下配置使用 mysql 数据库
    
        1.数据库的配置
            sqlite 数据库配置
            # file: settings.py
            DATABASES = {        
                'default': {        
                        'ENGINE': 'django.db.backends.sqlite3',        
                        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),        
                }        
            }

            mysql 数据库配置
            DATABASES = {        
                'default' : {        
                    'ENGINE': 'django.db.backends.mysql',        
                    'NAME': 'mywebdb',  # 数据库名称,需要自己定义        
                    'USER': 'root',        
                    'PASSWORD': '123456',  # 管理员密码        
                    'HOST': '127.0.0.1',        
                    'PORT': 3306,        
                }        
            }
            
        2.修改项目中init.py 加入如下内容来提供pymysql引擎的支持
            import pymysql
            pymysql.install_as_MySQLdb()
     
# Models

   ## 1.定义
    模型是一个Python类，它是由django.db.models.Model派生出的子类。
    一个模型类代表数据库中的一张数据表
    模型类中每一个类属性都代表数据库中的一个字段。
    模型是数据交互的接口，是表示和操作数据库的方法和方式
    
   ## 2.ORM框架(对象关系映射)
    1.作用
        建立模型类和表之间的对应关系，允许我们通过面向对象的方式来操作数据库。
        根据设计的模型类生成数据库中的表格。
        通过简单的配置就可以进行数据库的切换。
    2.好处:
        只需要面向对象编程, 不需要面向数据库编写代码.
        对数据库的操作都转化成对类属性和方法的操作.
        不用编写各种数据库的sql语句.    
        实现了数据模型与数据库的解耦, 屏蔽了不同数据库操作上的差异.
        不在关注用的是mysql、oracle...等数据库的内部细节.
        通过简单的配置就可以轻松更换数据库, 而不需要修改代码.
    3.缺点
        相比较直接使用SQL语句操作数据库,有性能损失.
        在更新时，需要先查询。
        根据对象的操作转换成SQL语句,根据查询的结果转化成对象, 在映射过程中有性能损失.  
   ![alt 属性文本](orm.png)
   
    4.实例
        # file : bookstore/models.py
        
        from django.db import models
        class Book(models.Model): 
        title = models.CharField("书名", max_length=50, default='')
        price = models.DecimalField('定价', max_digits=7, decimal_places=2, default=0.0)
    
    5.数据库的迁移
        迁移是Django同步您对模型所做更改（添加字段，删除模型等） 到您的数据库模式的方式
        
        1.生成或更新迁移文件
            将每个应用下的models.py文件生成一个中间文件,并保存在migrations文件夹中
            python3 manage.py makemigrations

        2.执行迁移脚本程序
            执行迁移程序实现迁移。将每个应用下的migrations目录中的中间文件同步回数据库
            python3 manage.py migrate
            
   **注:每次修改完模型类再对服务程序运行之前都需要做以上两步迁移操作**
   
    6.编写模型类Models
        1.模型类需继承自django.db.models.Model
        
        2.Models的语法规范
        
            from django.db import models        
            class 模型类名(models.Model):        
                字段名 = models.字段类型(字段选项)
                
            1.建议类名首字母大写
                
            2.字段类型(第一个参数是在admin后台显示的名字)
                BooleanField()
                    数据库类型:tinyint(1)
                    编程语言中:使用True或False来表示值
                    在数据库中:使用1或0来表示具体的值            
                CharField()            
                    数据库类型:varchar            
                    注意:
                        必须要指定max_length参数值            
                DateField()            
                    数据库类型:date            
                    作用:表示日期            
                    编程语言中:使用字符串来表示具体值            
                    参数:
                        DateField.auto_now: 每次保存对象时，自动设置该字段为当前时间(取值:True/False)。
                        DateField.auto_now_add: 当对象第一次被创建时自动设置当前时间(取值:True/False)。
                        DateField.default: 设置当前时间(取值:字符串格式时间如: '2019-6-1')。
                        以上三个参数只能多选一            
                DateTimeField()
                    数据库类型:datetime(6)
                    作用:表示日期和时间
                    auto_now_add=True            
                DecimalField()            
                    数据库类型:decimal(x,y)            
                    编程语言中:使用小数表示该列的值            
                    在数据库中:使用小数            
                    参数:
                        DecimalField.max_digits: 位数总数，包括小数点后的位数。 该值必须大于等于decimal_places.
                        DecimalField.decimal_places: 小数点后的数字数量            
                    示例:            
                    money=models.DecimalField(            
                        max_digits=7,            
                        decimal_places=2,            
                        default=0.0            
                    )            
                FloatField()
                    数据库类型:double
                    编程语言中和数据库中都使用小数表示值            
                EmailField()
                    数据库类型:varchar
                    编程语言和数据库中使用字符串            
                IntegerField()
                    数据库类型:int
                    编程语言和数据库中使用整数            
                URLField()
                    数据库类型:varchar(200)
                    编程语言和数据库中使用字符串            
                ImageField()            
                    数据库类型:varchar(100)            
                    作用:在数据库中为了保存图片的路径            
                    编程语言和数据库中使用字符串            
                    示例:            
                    image=models.ImageField(            
                        upload_to="static/images"            
                    )            
                    upload_to:指定图片的上传路径
                    在后台上传时会自动的将文件保存在指定的目录下            
                TextField()
                    数据库类型:longtext
                    作用:表示不定长的字符数据
            3.
                