# Django05

# 数据库:

## 直接执行原生SQL语句
1.raw()方法执行原生sql语句：

    # raw()方法执行原生sql(调用的类名不区分是谁，只要存在均可执行)
    
     ret=models.Book.objects.raw('select * from app01_book')
    
     # ret=models.Publish.objects.raw('select * from app01_book')
    
     for book in ret:
    
         print(book.book_name)
    
          # print(book.__dict__)
2.直接执行自定义原生sql语句：

    #直接执行自定义原生sql（完全避开模型层，类似pymysql操作）
    
     from django.db import connection
    
     cursor=connection.cursor()
    
     cursor.execute('select * from app01_book')
    
     ret=cursor.fetchall()
    
     print(ret)#((2, '小时光', Decimal('10.00'), 2), (3, '未来可期', Decimal('33.00'), 1), (4, '打破思维里的墙', Decimal('11.00'), 2), (5, '时光不散', Decimal('11.00'), 3))

       

## 1.聚合查询
定义:

    聚合查询是指对一个数据表中的一个字段的数据进行部分或全部进行统计查询
1.不带分组聚合

    不带分组的聚合查询是指导将全部数据进行集中统计查询

    聚合函数:

        定义模块: django.db.models

        用法: from django.db.models import *

        聚合函数: 
            Sum, Avg, Count, Max, Min

    语法: 
        MyModel.objects.aggregate(结果变量名=聚合函数('列'))

    返回结果:

        由 结果变量名和值组成的字典

        格式为:
            `{"结果变量名": 值}
    示例:    

        # 得到所有书的平均价格
        
        from bookstore import models
        
        from django.db.models import Avg
        
        result = models.Book.objects.aggregate(myAvg=Avg('price'))
        
        print("平均价格是:", result['myAvg'])
        
        print("result=", result)  # {"myAvg": 58.2}
        
        ​
        
        # 得到数据表里有多少本书
        
        from django.db.models import Count
        
        result = models.Book.objects.aggregate(mycnt=Count('title'))
        
        print("数据记录总个数是:", result['mycnt'])
        
        print("result=", result)  # {"mycnt": 10}
    
2.分组聚合

    分组聚合是指通过计算查询结果中每一个对象所关联的对象集合，从而得出总计值(也可以是平均值或总和)，即为查询集的每一项生成聚合。

    语法: 
        QuerySet.annotate(结果变量名=聚合函数('列'))

    用法步骤:

        1.通过先用查询结果MyModel.objects.values 查找查询要分组聚合的列

            MyModel.objects.values('列1', '列2')

            如: 

            pub_set = models.Book.objects.values('pub')

            print(pub_set)  # <QuerySet [{'pub': '清华大学出版社'}, {'pub': '清华大学出版社'}, {'pub_hou {'pub': '机械工业出版社'}, {'pub': '清华大学出版社'}]>

            ​

        2.通过返回结果的 QuerySet.annotate 方法分组聚合得到分组结果

            QuerySet.annotate(名=聚合函数('列'))

            返回 QuerySet 结果集,内部存储结果的字典

            如:

            pub_count_set = pub_set.annotate(myCount=Count('pub'))

            print(pub_count_set)  # <QuerySet [{'pub': '清华大学出版社', 'myCount': 7}, {'pub': '机械工业出版社', 'myCount': 3}]>

        .values('查询列名')

    示例:
        得到哪儿个出版社共出版多少本书

        def test_annotate(request):
    
           from django.db.models import Count
    
           from . import models

        # 得到所有出版社的查询集合QuerySet

        pub_set = models.Book.objects.values('pub')

        # 根据出版社查询分组，出版社和Count的分组聚合查询集合

        # pub_count_set = pub_set.annotate(myCount=Count('pub')).filter(..)
        
        pub_count_set = pub_set.annotate(myCount=Count('pub'))  # 返回查询集合

        for item in pub_count_set:

            print("出版社:", item['pub'], "图书有：", item['myCount'])

        return HttpResponse('请查看服务器端控制台获取结果')
        
3.F对象

    一个F对象代表数据库中某条记录的字段的信息

    作用:
        通常是对数据库中的字段值在不获取的情况下进行操作
        用于类属性(字段)之间的比较。

    用法

        F对象在数据包 django.db.models 中，使用时需要先导入
            from django.db.models import F

    语法:

    from django.db.models import F

    F('列名')  

    说明:
        一个 F() 对象代表了一个model的字段的值
        F对象通常是对数据库中的字段值在不加载到内存中的情况下直接在数据库服务器端进行操作

 

    示例1
        更新Book实例中所有的零售价涨10元

        models.Book.objects.all().update(market_price=F('market_price')+10)
    
        'UPDATE `bookstore_book` SET `market_price` = (`bookstore_book`.`market_price` + 1) 
    
        # 以上做法好于如下代码
    
        books = models.Book.objects.all()
    
        for book in books:
    
            book.update(market_price=book.marget_price+10)
    
            book.save()

    示例2
        对数据库中两个字段的值进行比较，列出哪儿些书的零售价高于定价?

        from django.db.models import F
    
        from bookstore import models
    
        books = models.Book.objects.filter(market_price__gt=F('price'))
    
        'SELECT * FROM `bookstore_book` WHERE `bookstore_book`.`market_price` > (`bookstore_book`.`price`)
    
        for book in books:
    
            print(book.title, '定价:', book.price, '现价:', book.market_price)

4.Q对象 - Q()

    当在获取查询结果集 使用复杂的逻辑或  | 、 逻辑非 ~ 等操作时可以借助于 Q对象进行操作

    如: 想找出定价低于20元 或 清华大学出版社的全部书，可以写成

    models.Book.objects.filter(Q(price__lt=20)|Q(pub="清华大学出版社"))

    Q对象在 数据包 django.db.models 中。需要先导入再使用
        from django.db.models import Q

    作用
        在条件中用来实现除 and(&) 以外的 or(|) 或 not(~) 操作

    运算符:
        & 与操作
        | 或操作
        〜 非操作

    语法

    from django.db.models import Q

    Q(条件1)|Q(条件2)  # 条件1成立或条件2成立

    Q(条件1)&Q(条件2)  # 条件1和条件2同时成立

    Q(条件1)&~Q(条件2)  # 条件1成立且条件2不成立

    ...

    示例

        from django.db.models import Q
    
        # 查找清华大学出版社的书或价格低于50的书
    
        models.Book.objects.filter(Q(market_price__lt=50) | Q(pub_house='清华大学出版社'))
    
        # 查找不是机械工业出版社的书且价格低于50的书
    
        models.Book.objects.filter(Q(market_price__lt=50) & ~Q(pub_house='机械工业出版社'))
    
   
## 原生的数据库操作方法

1.使用MyModel.objects.raw()进行 数据库查询操作查询.在django中，可以使用模型管理器的raw方法来执行select语句进行数据查询

        语法: 
            MyModel.objects.raw(sql语句)

        用法
            MyModel.objects.raw('sql语句')

        返回值:
            RawQuerySet 集合对象 【只支持基础操作，比如循环】

        示例

            books = models.Book.objects.raw('select * from bookstore_book')

            for book in books:
            
                print(book)
    ​
            
            #sql注入问题
            
            s1 = Book.objects.raw('select * from bookstore_book where id=%s'%('1 or 1=1'))
            
            #解决
            s2 = Book.objects.raw('select * from bookstore_book where id=%s',['1 or 1=1'])
            
                

2.使用django中的游标cursor对数据库进行 增删改操作

        在Django中可以使用 如UPDATE,DELETE等SQL语句对数据库进行操作。

        在Django中使用上述非查询语句必须使用游标进行操作

        使用步骤:

            导入cursor所在的包

                Django中的游标cursor定义在 django.db.connection包中，使用前需要先导入

                如：
                    from django.db import connection

            用创建cursor类的构造函数创建cursor对象，再使用cursor对象,为保证在出现异常时能释放cursor资源,通常使用with语句进行创建操作

                如:

                from django.db import connection

                with connection.cursor() as cur:

                    cur.execute('执行SQL语句')

            示例

            # 用SQL语句将id 为 10的 书的出版社改为 "XXX出版社"

            from django.db import connection

            with connection.cursor() as cur: 

                cur.execute('update bookstore_book set pub_house="XXX出版社" where id=10;')

            with connection.cursor() as cur:

                # 删除 id为1的一条记录

                cur.execute('delete from bookstore_book where id=10;')        

## sql注入问题  
**int型通过此方法可以解决注入，其他类型则无法查出任何内容**
1.select * from bookstore_book where id=%s'%('1 or 1=1')
解决:select * from bookstore_book where id=%s',['1 or 1=1']           