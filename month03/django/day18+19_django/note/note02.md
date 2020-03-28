# Django04

# MOdels -> 数据库的使用

# 注意:
    建立一个表，添加一个is_active字段，将is_active bool 默认设置为True
    
   ##1.管理器对象 
        每个继承自 models.Model 的模型类，都会有一个 objects 对象被同样继承下来。这个对象叫管理器对象
        数据库的增删改查可以通过模型的管理器实现
        eg:
            class MyModel(models.Model):
            
                ...
            
            MyModel.objects.create(...) # objects 是管理器对象
            
   ##2.创建数据对象
        Django 使用一种直观的方式把数据库表中的数据表示成Python对象    
        创建数据中每一条记录就是创建一个数据对象        
            1.MyModel.objects.create(属性1=值1, 属性2=值1,...)
                成功: 返回创建好的实体对象
                失败: 抛出异常        
            2.创建 MyModel 实例对象,并调用save()进行保存        
                obj = MyModel(属性=值,属性=值)        
                obj.属性=值        
                obj.save()
                
   ## 3.Django shell 的使用
        在Django提供了一个交互式的操作项目叫 Django Shell 它能够在交互模式用项目工程的代码执行相应的操作    
        利用 Django Shell 可以代替编写View的代码来进行直接操作    
        在Django Shell 下只能进行简单的操作，不能运行远程调式    
        启动方式:    
            $ python3 manage.py shell
    
## 4.查询数据    
    数据库的查询需要使用管理器对象进行     
    通过 MyModel.objects 管理器方法调用查询接口
    返回值是queryset的对象可以使用.query()查看数据库语音
        
|  方法   | 说明  | 返回值类型 |
|  ----  | ----  | ----  |
| all()  | 查询全部记录,返回QuerySet查询对象 | queryset  |
| values('列1')  | 查询指定列的数据并返回字典形式 | queryset  |
| values_list('列1','列2')  | 查询指定列的数据并返回元组形式的查询结果,返回QuerySet查询对象 | queryset  |
| order_by('列')  | 对查询结果进行根据某个字段选择性的进行排序 | queryset  |
| filter(条件)  | 根据条件查询多条记录 | queryset  |
| get()  | 查询符合条件的单一记录 |  models对象 |
| exclude()  | 查询符合条件之外的全部记录 | queryset  |
| ...  | ... |

1.all()方法

    方法: all()
    用法: MyModel.objects.all()
    作用: 查询MyModel实体中所有的数据
          等同于
            select * from tabel
    返回值: QuerySet容器对象,内部存放 MyModel 实例
    示例:
        from bookstore import models
        books = models.Book.objects.all()
        for book in books:
            print("书名", book.title, '出版社:', book.pub)

2.在模型类中定义 def __str__(self): 方法可以返回自定义默认的字符串

    class Book(models.Model):    
        title = ...    
        def __str__(self):    
            return "书名: %s, 出版社: %s, 定价: %s" % (self.title, self.pub, self.price)

3.查询返回指定列(字典表示)

    方法: values('列1', '列2')
    用法: MyModel.objects.values(...)
    作用: 查询部分列的数据并返回
        select 列1,列2 from xxx
    返回值: QuerySet
        返回查询结果容器，容器内存字典，每个字典代表一条数据,
        格式为: {'列1': 值1, '列2': 值2}
    示例:
        from bookstore import models
        books = models.Book.objects.values("title", "pub")
        for book in books:
            print("书名", book["title"], '出版社:', book['pub'])
            print("book=", book)

4.查询返回指定列（元组表示)

    方法:values_list('列1','列2')
    用法:MyModel.objects.values_list(...)
    作用:
        返回元组形式的查询结果
    返回值: QuerySet容器对象,内部存放 元组
        会将查询出来的数据封装到元组中,再封装到查询集合QuerySet中
    示例:
        from bookstore import models
        books = models.Book.objects.values_list("title", "pub")
        for book in books:
            print("book=", book)  # ('Python', '清华大学出版社')...

5.排序查询

    方法:order_by
    用法:MyModel.objects.order_by('-列','列')
    作用:
        与all()方法不同，它会用SQL 语句的ORDER BY 子句对查询结果进行根据某个字段选择性的进行排序
    说明:
        默认是按照升序排序,降序排序则需要在列前增加'-'表示
    示例: 
        from bookstore import models
        books = models.Book.objects.order_by("price")
        for book in books:
            print("书名:", book.title, '定价:', book.price)

6.根据条件查询多条记录

    方法: filter(条件)
    语法: MyModel.objects.filter(属性1=值1, 属性2=值2)
    返回值:
        QuerySet容器对象,内部存放 MyModel 实例
    说明:
        当多个属性在一起时为"与"关系，即当Books.objects.filter(price=20, pub="清华大学出版社") 返回定价为20 且 出版社为"清华大学出版社"的全部图书
    示例:
        # 查询书中出版社为"清华大学出版社"的图书
        from bookstore import models
        books = models.Book.objects.filter(pub="清华大学出版社")
        for book in books:
            print("书名:", book.title)   ​ 
               
        # 查询Author实体中id为1并且isActive为True的
            authors=Author.objects.filter(id=1,isActive=True)
            
## 字段查找
    字段查询是指如何指定SQL语句中 WHERE 子句的内容。
    
    字段查询需要通过QuerySet的filter(), exclude() and get()的关键字参数指定。
    
    非等值条件的构建,需要使用字段查询
    
    示例:
    
        # 查询作者中年龄大于30
        
        Author.objects.filter(age__gt=30)
        
        # __get是查询谓词
        
        # 对应
        
        # SELECT .... WHERE AGE > 35;
        
## 查询谓词

    每一个查询谓词是一个独立的查询功能

    1.__exact : 等值匹配

        Author.objects.filter(id__exact=1)

        # 等同于select * from author where id = 1

    2.__contains : 包含指定值

        Author.objects.filter(name__contains='w')

        # 等同于 select * from author where name like '%w%'

    3.__startswith : 以 XXX 开始

    4.__endswith : 以 XXX 开始

    5.__gt : 大于指定值

        Author.objects.filer(age__gt=50)

        # 等同于 select * from author where age > 50

    6.__gte : 大于等于

    7.__lt : 小于

    8.__lte : 小于等于

    9.__in : 查找数据是否在指定范围内    
        示例
            Author.objects.filter(country__in=['中国','日本','韩国'])
        
            # 等同于 select * from author where country in ('中国','日本','韩国')

    10.__range: 查找数据是否在指定的区间范围内

        # 查找年龄在某一区间内的所有作者
    
        Author.objects.filter(age__range=(35,50))

        # 等同于 SELECT ... WHERE Author BETWEEN 35 and 50;

   详细内容参见: https://docs.djangoproject.com/en/1.11/ref/models/querysets/#field-lookups

```python
    MyModel.objects.filter(id__gt=4)

    # 等同于 SELECT ... WHERE id > 4    ;
```

## 不等的条件筛选
    语法:
    MyModel.objects.exclude(条件)
    
    作用:
    
        返回不包含此 条件 的 全部的数据集
    
    示例:
    
        查询 清华大学出版社，定价大于50 以外的全部图书
    
        books = models.Book.objects.exclude(pub="清华大学出版社", price__gt=50)
        
        for book in books:
        
            print(book)
          
## 查询指定的一条数据

    语法:
    MyModel.objects.get(条件)

    作用：
        返回满足条件的唯一一条数据

    返回值:
        MyModel 对象

    说明:
        该方法只能返回一条数据
        查询结果多余一条数据则抛出,Model.MultipleObjectsReturned异常
        查询结果如果没有数据则抛出Model.DoesNotExist异常

    示例:

        from bookstore import models
    
        book = models.Book.objects.get(id=1)

        print(book.title)  

## 修改数据记录

**orm的惰性现象:以下操作会执行sql语句**
        
        s = book[0]
        print(book)
        books.update(price=0)
        for k in books:
            print(k)

1.修改单个实体的某些字段值的步骤:

    查
        通过 get() 得到要修改的实体对象

    改
        通过 对象.属性 的方式修改数据 

    保存
        通过 对象.save() 保存数据

    如:
        from bookstore import models
    
        abook = models.Book.objects.get(id=10)
    
        abook.market_price = "10.5"
    
        abook.save()

2.通过 QuerySet 批量修改 对应的全部字段

    直接调用QuerySet的update(属性=值) 实现批量修改

    如:

        # 将 id大于3的所有图书价格定为0元
    
        books = Book.objects.filter(id__gt=3)
        
        # 以下操作会执行sql语句
        
        s = book[0]
        print(book)
        books.update(price=0)
        for k in books:
            print(k)
    
        # 将所有书的零售价定为100元
    
        books = Book.objects.all()
    
        books.update(market_price=100)
       
## 删除记录
**伪删除 :在删除操作时，将 is_active bool 设置为False**

**建立一个表，添加一个is_active字段，将is_active bool 默认设置为True**

```python
    from django.db import models
    class Book(models.Model):
    title = models.CharField("书名", max_length=50, default='', unique=True)
    price = models.DecimalField("图书定价", max_digits=7, decimal_places=2, default=0.0)
    market_price = models.DecimalField('图书零售价', max_digits=7, decimal_places=2, default=0.0)
    pub = models.CharField('出版社', max_length=200, default='')
    is_active = models.BooleanField('是否活跃',default=True)

    def __str__(self):
        return '%s_%s_%s_%s' % (self.title, self.price, self.pub, self.market_price)
```

    删除记录是指删除数据库中的一条或多条记录
    删除单个MyModel对象或删除一个查询结果集(QuerySet)中的全部对象
    都是调用 delete()方法
    
    删除单个对象
        步骤
            查找查询结果对应的一个数据对象
            调用这个数据对象的delete()方法实现删除  
        示例:    
            try:    
                auth = Author.objects.get(id=1)    
                auth.delete()    
            except:    
                print(删除失败)