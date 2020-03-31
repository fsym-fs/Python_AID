# django05_02

# admin

## 1.admin后台数据库管理
使用步骤:

    1.创建后台管理帐号:

        后台管理--创建管理员帐号
            $ python3 manage.py createsuperuser            
            根据提示完成注册,参考如下:

        $ python3 manage.py createsuperuser

        Username (leave blank to use 'tarena'): tarena  # 此处输入用户名

        Email address: laowei@tedu.cn  # 此处输入邮箱

        Password: # 此处输入密码(密码要复杂些，否则会提示密码太简单)

        Password (again): # 再次输入重复密码

        Superuser created successfully.

        $ 

    2.用注册的帐号登陆后台管理界面
        后台管理的登录地址:
            http://127.0.0.1:8000/admin
## 2.自定义后台管理数据表

若要自己定义的模型类也能在 /admin 后台管理界中显示和管理，需要将自己的类注册到后台管理界面

添加自己定义模型类的后台管理数据表的,需要用admin.site.register(自定义模型类) 方法进行注册

    配置步骤如下:

        1.在应用app中的admin.py中导入注册要管理的模型models类, 如:

        from . import models

        2.调用 admin.site.register 方法进行注册,如:

        from django.contrib import admin

        admin.site.register(自定义模型类)

    如: 在 bookstore/admin.py 添加如下代码对Book类进行管理

    示例:

        # file: bookstore/admin.py
    
        from django.contrib import admin
    
        # Register your models here.
    
        ​
    
        from . import models
    
        ...
    
        admin.site.register(models.Book)  # 将Book类注册为可管理页面
        
##  3.修改后台Models的展现形式

    在admin后台管理数据库中对自定义的数据记录都展示为 XXXX object 类型的记录，不便于阅读和判断

    在用户自定义的模型类中可以重写 def __str__(self): 方法解决显示问题,如:
        在 自定义模型类中重写 str(self) 方法返回显示文字内容:

    class Book(models.Model):
        ...

        def __str__(self):

            return "书名" + self.title

## 4.模型管理器类(一个类一个管理器类)

1.作用:

    为后台管理界面添加便于操作的新功能。

2.说明:

    后台管理器类须继承自 django.contrib.admin 里的 ModelAdmin 类

3.模型管理器的使用方法:

    1.在 <应用app>/admin.py 里定义模型管理器类

        class XXXXManager(admin.ModelAdmin):

            ......

    2.注册管理器与模型类关联

        from django.contrib import admin

        from . import models

        admin.site.register(models.YYYY, XXXXManager) # 注册models.YYYY 模型类与 管理器类 XXXXManager 关联

    示例:

        # file : bookstore/admin.py

        from django.contrib import admin

        from . import models

        ​

        class BookManager(admin.ModelAdmin):

            list_display = ['id', 'title', 'price', 'market_price']

        ​

        admin.site.register(models.Book, BookManager)

            进入http://127.0.0.1:8000/admin/bookstore/book/ 查看显示方式和以前有所不同

**4.模型管理器类ModelAdmin中实现的高级管理功能**

    1.list_display 去控制哪些字段会显示在Admin 的修改列表页面中。
    2.list_display_links 可以控制list_display中的字段是否应该链接到对象的“更改”页面。
    3.list_filter 设置激活Admin 修改列表页面右侧栏中的过滤器 
    4.search_fields 设置启用Admin 更改列表页面上的搜索框。      
    5.list_editable 设置为模型上的字段名称列表，这将允许在更改列表页面上进行编辑。

其它参见https://docs.djangoproject.com/en/1.11/ref/contrib/admin/

## 5.数据库表管理

1.修改模型类字段的显示名字

    模型类各字段的第一个参数为 verbose_name,此字段显示的名字会在后台数据库管理页面显示

    通过 verbose_name 字段选项,修改显示名称示例如下：

    title = models.CharField(

        max_length = 30,

        verbose_name='显示名称'

    )

2.通过Meta内嵌类 定义模型类的属性及展现形式

    模型类可以通过定义内部类class Meta 来重新定义当前模型类和数据表的一些属性信息

    用法格式如下:

    class Book(models.Model):

        title = CharField(....)

        class Meta:

            1. db_table = '数据表名'

                - 该模型所用的数据表的名称。(设置完成后需要立马更新同步数据库)

            2. verbose_name = '单数名'

                - 给模型对象的一个易于理解的名称(单数),用于显示在/admin管理界面中

            3. verbose_name_plural = '复数名'

                - 该对象复数形式的名称(复数),用于显示在/admin管理界面中
                
## 数据表关联关系映射

1.常用的表关联方式有三种:

    一对一映射
        如: 一个身份证对应一个人
    
    一对多映射
        如: 一个班级可以有多个学生
    
    多对多映射
        如: 一个学生可以报多个课程，一个课程可以有多个学生学习        

2.一对一映射

**属性 = models.OneToOneField(类名)**

**外键自动为类的id**

    一对一是表示现实事物间存在的一对一的对应关系。
    如:一个家庭只有一个户主，一个男人有一个妻子，一个人有一个唯一的指纹信息等

    1.语法
    
    class A(model.Model):
    
        ...
    
    class B(model.Model):
        
        #类名
        属性 = models.OneToOneField(A)
    
    2.外键类字段选项
    
        1.特殊字段参数:
            on_delete
                models.CASCADE  级联删除。 Django模拟SQL约束ON DELETE CASCADE的行为，并删除包含ForeignKey的对象。
                models.PROTECT 抛出ProtectedError 以阻止被引用对象的删除;[等同于mysql默认的RESTRICT]
                SET_NULL 设置ForeignKey null；需要指定null=True
                SET_DEFAULT  将ForeignKey设置为其默认值；必须设置ForeignKey的默认值。
                ... 其它参请参考文档 https://docs.djangoproject.com/en/1.11/ref/models/fields/#foreignkey ForeignKey部分
    
        2.其余常用的字段选项如:
            null
            unique 等
    
    3.用法示例
    
        1.创建作家和作家妻子类
    
        # file : xxxxxxxx/models.py
    
        from django.db import models
    
        ​
    
        class Author(models.Model):
    
            '''作家模型类'''
    
            name = models.CharField('作家', max_length=50)
    
        ​
    
        class Wife(models.Model):
    
            '''作家妻子模型类'''
    
            name = models.CharField("妻子", max_length=50)
    
            author = models.OneToOneField(Author)  # 增加一对一属性 
    
        2.创建一对一的数据记录
    
        from . import models
        
        # 法一
        author1 = models.Author.objects.create(name='王老师')
    
        wife1 = models.Wife.objects.create(name='王夫人', author=author1)  # 关联王老师
    
        # 法二
        wife2 = models.Wife.objects.create(name='qqq',author_id=2)
        
        author2 = models.Author.objects.create(name='小泽老师')  # 一对一可以没有数据对应的数据 
    
        3.数据查询
    
            1.正向查询
                直接通过关联属性查询即可
    
            # 通过 wife 找 author
    
            from . import models
    
            wife = models.Wife.objects.get(name='王夫人')
    
            print(wife.name, '的老公是', wife.author.name)
    
            2.反向查询 author->wife
                通过反向关联属性查询
                反向关联属性为实例对象.引用类名(小写)，如作家的反向引用为作家对象.wife
                当反向引用不存在时，则会触发异常
    
            # 通过 author.wife 关联属性 找 wife,如果没有对应的wife则触发异常
    
            author1 = models.Author.objects.get(name='王老师')
    
            print(author1.name, '的妻子是', author1.wife.name)
    
            author2 = models.Author.objects.get(name='小泽老师')
    
            try:
    
                print(author2.name, '的妻子是', author2.wife.name)
    
            except:
    
                print(author2.name, '还没有妻子')
    
    4.作用:

    主要是解决常用数据不常用数据的存储问题,把经常加载的一个数据放在主表中，不常用数据放在另一个副表中，这样在访问主表数据时不需要加载副表中的数据以提高访问速度提高效率和节省内存空间,如经常把书的内容和书名建成两张表，因为在网站上经常访问书名等信息，但不需要得到书的内容。
    
    5.应用场景
        1.授权登录
        2.数据分离
        3.开发过程->新手问题
  
3.一对多映射   

**属性 = models.ForeignKey(类名)**

**外键自动为类的id**

    1.一对多是表示现实事物间存在的一对多的对应关系。
    如:一个学校有多个班级,一个班级有多个学生, 一本图书只能属于一个出版社,一个出版社允许出版多本图书
        
    2.用法语法

    当一个A类对象可以关联多个B类对象时

    class A(model.Model):
        ...
    
    class B(model.Model):
    
        属性 = models.ForeignKey("一"的模型类, ...)  
    
    3. 用法示例

    有二个出版社对应五本书的情况.

        清华大学出版社 有书
            C++
            Java
            Python

        北京大学出版社 有书
            西游记
            水浒    
    
    4.创建数据

        # file: one2many/models.py
        
        from django.db import models
        
        class Publisher(models.Model):
        
            '''出版社'''
        
            name = models.CharField('名称', max_length=50, unique=True)
        
        ​
        
        class Book(models.Model):
        
            title = models.CharField('书名', max_length=50)
        
            publisher = ForeignKey(Publisher)
        
            
        
        #创建数据
        
        from . import models
        
        pub1 = models.Publisher.objects.create(name='清华大学出版社')
        
        models.Book.objects.create(title='C++', publisher=pub1)
        
        models.Book.objects.create(title='Java', publisher=pub1)
        
        models.Book.objects.create(title='Python', publisher=pub1) 

        pub2 = models.Publisher.objects.create(name='北京大学出版社')
        
        models.Book.objects.create(title='西游记', publisher=pub2)
        
        models.Book.objects.create(title='水浒', publisher=pub2)
    
    5.数据查询
        1.通过 Book 查询 Publisher【正向】
    
            通过 publisher 属性查询即可
            
            book.publisher
    
            abook = models.Book.objects.get(id=1)
            
            print(abook.title, '的出版社是:', abook.publisher.name)
        
        2.通过 Publisher 查询 对应的所有的 Books 【反向】
            
            Django会在Publisher中增加一个属性来表示对对应的Book们的查询引用

            属性:book_set  等价于 objects

            # 通过出版社查询对应的书
            
            pub1 = models.Publisher.objects.get(name='清华大学出版社')
            
            books = pub1.book_set.all()  # 通过book_set 获取pub1对应的多个Book数据对象
            
            #books = models.Book.objects.filter(publisher=pub1)  # 也可以采用此方式获取
            
            print("清华大学出版社的书有:")
            
            for book in books:
               print(book.title)
               
4.多对多映射 
  
    1.多对多表达对象之间多对多复杂关系
    如: 每个人都有不同的学校(小学，初中，高中,...),每个学校都有不同的学生... 
    
    2.语法
    在关联的两个类中的任意一个类中,增加:
    属性 = models.ManyToManyField(MyModel) 
    
    3.示例

    一个作者可以出版多本图书
    一本图书可以被多名作者同时编写

    class Author(models.Model):
        ...
    
    class Book(models.Model):
        ...
        authors = models.ManyToManyField(Author)
    
    4.数据查询

    1.通过 Book 查询对应的所有的 Authors【正向】

        book.authors.all() -> 获取 book 对应的所有的author的信息
    
        book.authors.filter(age__gt=80) -> 获取book对应的作者中年龄大于80岁的作者的信息

    2.通过 Author 查询对应的所有的Books【反向】
        Django会生成一个关联属性 book_set 用于表示对对应的book的查询对象相关操作

        author.book_set.all()
    
        author.book_set.filter()
    
        author.book_set.create(...)  # 创建新书并关联author
    
        author.book_set.add(book)   # 添加已有的书给当前作者author
    
        author.book_set.clear()  # 删除author所有并联的书  
    
    3.用法示例:

        1.多对多模型
    
        class Author(models.Model):
        
            '''作家模型类'''
        
            name = models.CharField('作家', max_length=50)
        
            def __str__(self):
        
                return self.name
    
        class Book(models.Model):
        
            title = models.CharField('书名', max_length=50)
        
            author = models.ManyToManyField(Author)
        
            def __str__(self):
        
                return self.title 
    
        2.多对多视图操作
    
        from django.http import HttpResponse
        
        from . import models
        
        def many2many_init(request):
        
            # 创建两人个作者
        
            author1 = models.Author.objects.create(name='吕泽')
        
            author2 = models.Author.objects.create(name='王老师') ​
        
            # 吕择和王老师同时写了一本Python
        
            book11 = author1.book_set.create(title="Python")
        
            author2.book_set.add(book11)  #
        
            # 王老师还写了两本书
        
            book21 = author2.book_set.create(title="C")  # 创建一本新书"C"   
        
            book22 = author2.book_set.create(title="C++")  # 创建一本新书"C++"
        
            return HttpResponse("初始化成功")
            
            # 通过书创建并绑定作者
            
            b2.authors.create(name='lvze')
        
        ​
        
        def show_many2many(request):
        
            authors = models.Author.objects.all()
        
            for auth in authors:
        
                print("作者:", auth.name, '发出版了', auth.book_set.count(), '本书: ')
        
                for book in books:
        
                    print('    ', book.title)
        
            print("----显示书和作者的关系----")
        
            books = models.Book.objects.all()
        
            for book in books:
        
                auths = book.author.all()
        
                print(book.title, '的作者是:', '、'.join([str(x.name) for x in auths]))
        
            return HttpResponse("显示成功，请查看服务器端控制台终端")