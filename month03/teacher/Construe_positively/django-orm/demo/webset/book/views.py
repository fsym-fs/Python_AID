from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from book.models import Book,Author
from django.db.models import Avg,Count,Max,Min,Sum,F,Q
import json

def get_data(requset):
#1.示意 基本查詢 all()
    # books = Book.objects.all()
    # for book in books:
    #     print("id:%s,書名:%s,出版時間:%s"%(book.id,book.title,book.publisher_date))
    # # 查看 query 打印輸出SQL語句,Queryset对象才有此属性.
    # print(books.query)
    # SELECT  * FROM `book_book`
    #***************************************

#2.示意查詢返回部分列 values()
    # books = Book.objects.values("title","publisher_date")
    # for book in books:
    #     print("書名:%s,出版日期:%s"%(book.get("title"),book.get("publisher_date")))
    # print(books.query)
    # SELECT `book_book`.`title`, `book_book`.`publisher_date` FROM `book_book`
    #***************************************
    # 書名:零基础学Python（全彩版）,出版日期:2018-12-15
    # 書名:Python进行数据分析,出版日期:2018-02-01
    # 書名:Python网络编程,出版日期:2008-10-25
    # 書名:python爬虫,出版日期:2012-04-15
    # 書名:python算法,出版日期:2018-03-01
#3.示意 查詢返回部分列 返回值類型於2有所不同
    # books = Book.objects.values_list("title", "publisher_date")
    # print(books)
    # for book in books:
    #     print("書名:%s,出版日期:%s"%(book[0],book[1]))
    #***************************************

#4.示意 查詢只返回一條數據 get(),  只能使用等值做條件,查询出多条数据或者查询不到数据都会抛出异常.
    # book = Book.objects.get(id=10)
    # print("書名:%s,出版時間:%s"%(book.title,book.publisher_date))
    #***************************************

#5.示意 查詢根據條件查詢部分行數據 filter()
    #   1.查詢 id爲1 的 Book的信息
    # book = Book.objects.filter(id=10)
    # print("書名:%s,出版時間:%s"%(book[0].title,book[0].publisher_date))

    #   2.查詢 publisher_date爲2015-10-12的book信息
    # books = Book.objects.filter(publisher_date="2018-3-15")
    # for book in books:
    #     print("書名:%s,出版時間:%s" % (book.title, book.publisher_date))
    #   3.查詢 id=10 且 publisher_date爲 2015-10-12的信息
    # book = Book.objects.filter(id=10,publisher_date="2018-12-15")
    # print("書名:%s,出版時間:%s"%(book[0].title, book[0].publisher_date))
    # 書名:零基础学Python（全彩版）,出版時間:2018-12-15
    #******************************************

#6.示意 filter不等值查询 (屬性__謂詞)
    #   1.查詢2018年出版的書, 属性名(字段)__謂詞
    # books = Book.objects.filter(id__gt=10)
    # for book in books:
    #     print("書名:%s,出版時間:%s" % (book.title, book.publisher_date))
    #   2.查詢 2017之後出版的書
    # books = Book.objects.filter(publisher_date__year__lt=2018)
    # for book in books:
    #     print("書名:%s,出版時間:%s" % (book.title, book.publisher_date))
#7. 示意 做不等值查詢 exclude(條件)
    #    1. 查詢 Author中年齡不大於20的人的信息
    # authors = Author.objects.filter(age__lt=20)
    # authors = Author.objects.exclude(age__gt=20)
    # for author in authors:
    #     print("年齡不大於20的:%s"%author.name)
    # 年齡不大於20的:finka
    # 年齡不大於20的:mimi

#8. 示意排序查詢 order_by("列","-列")
    # authors = Author.objects.order_by("age")
    # for author in authors:
    #     print("年齡升序排列:%s"%author.name,author.age)

#9. 示意聚合查詢 不分組類型 aggregate(鍵名=聚合函數("列名"))
    from django.db.models import Avg,Count,Max,Min,Sum,F,Q
    # 1.查詢Author表中所有人的平均年齡
    # authors = Author.objects.aggregate(avg=Max("age"))
    # print(authors.query)
    # print("平均年齡:%s"%authors.get("avg"))
#10. 示意聚合查詢 帶分組類型 annotate()
    #    1.查詢Book表中每個publisher_date所發型的書籍的數量
    # list = Book.objects.values("publisher_date").annotate(count=Count("title")).values("publisher_date","count").all()
    # print(list)
    # <QuerySet [
    #            {'publisher_date': datetime.date(2018, 12, 15), 'count': 1}, 
    #            {'publisher_date': datetime.date(2018, 3, 15), 'count': 2}, 
    #            {'publisher_date': datetime.date(2008, 10, 25), 'count': 1}, 
    #            {'publisher_date': datetime.date(2012, 4, 15), 'count': 1}]
    # >
    #<QuerySet [
    #            {'publisher_date': datetime.date(2018, 12, 15), 'count': 1}, 
    #            {'publisher_date': datetime.date(2018, 3, 15), 'count': 1}, 
    #            {'publisher_date': datetime.date(2008, 10, 25), 'count': 1}, 
    #            {'publisher_date': datetime.date(2012, 4, 15), 'count': 1}, 
    #            {'publisher_date': datetime.date(2018, 3, 15), 'count': 1}]
    # >
    #    2.查詢 Book表中 id>1 的進行分組
    # list = Book.objects.filter(id__gt=1).values("publisher_date").annotate(count=Count("title")).filter(count__gt=1).values("publisher_date","count").all()
    # print(list)
#11. 示意F查询
    # authors = Author.objects.filter(id__gt = F('age'))
    # for author in authors:
    #     print(author.id,author.name)
    # 给mimi的年龄+20岁
    # Author.objects.filter(name='mimi').update(age=F('age')+20)
    # author = Author.objects.get(name='mimi')
    # print(author.id,author.name,author.age)
#12. 示意Q查询
    # 查询年龄30岁或者id为1的用户
    # authors = Author.objects.filter(Q(age=30) & Q(id=2))
    # for author in authors:
    #     print(author.id,author.name,author.age)
    # 1 mitono 25
    # 2 dokkaebi 30
    # # 查询书的出版年份不是2018年的书籍
    books = Book.objects.filter(~Q(publisher_date__year ='2018'))
    for book in books:
        print(book.title,book.publisher_date)
    # Python网络编程 2008-10-25 python爬虫 2012-04-15
    # # 查询d开头且年龄为岁的用户
    authors = Author.objects.filter(Q(name__istartswith='D')&Q(age=30))
    for author in authors:
        print(author.name,author.age)
    return HttpResponse("<script>alert('查詢成功')</script>")