# django-ORM查询

## 说明:

通過 Entry.objects 的屬性調用查詢接口,例如:

```python
querys = Entry.objects.all()
query = Entry.objects.filter()
```

## 1.基本查詢操作

语法:

```python
Entry.objects.all()
```

作用:

將Entry實體的所有記錄查詢出來 select * from table;

返回值:

QuerySet 查询结果集list。

## COOKIES:

QuerySet 对象有一个query属性，它可以返回查询方法所用的sql语句.

## 2.指定列查询

语法:

```python
Entry.objects.values('列1','列2')
Entry.objects.all().values('列1','列2')
```

作用:

返回的是每个元素为字典的QuerSet 对象

返回值:

QuerySet 會將查詢出來的部分列封裝到字典中,再封裝到列表中

## 3.指定列查询

语法:

```python
Entry.objects.values_list("列1","列2")
```

作用:

返回的是每个元素为元组的QuerSet 对象

返回值:

QuerySet            會將查詢出來的部分列封裝到元組中,再封裝到列表中

## 4.只查詢一條數據出來

语法:

```python
Entry.objects.get()
```

作用:

查詢只能返回一條數據

返回值:

QuerySet            

注意:

該方法只能返回一條數據,查詢結果多餘一條(多个结果)或沒有查詢到結果(0)的話都會拋出異常

## 5.根據條件查詢部分行數據

语法:

```python
 Entry.objects.filter(参数)
```

作用:

筛选出与所给筛选条件相匹配的对象，多个条件是and的关系.

返回值:

QuerySet            會將查詢結果封裝到列表裏     

参数:

可以指定多个条件  

## 6.根據條件查詢部分行數據(非等值)

语法:

```python
Entry.objects.filter(屬性__謂詞 = 值)
```

查询谓词:

```shell
_gt     			大于
__gte   			大于等于
__lt      			小于
__lte    			小于等于
__in     			存在于一个list范围内
__startswith    	以...开头
__istartswith   	以...开头忽略大小写
__endswith     		以...结尾
__iendswith    		以...结尾，忽略大小写
__range   			在...范围内
__year      		日期字段的年份
__month   			日期字段的月份
__day        		日期字段的日
__overlap      		集合至少有一个元素重合
__contains     		集合包含
__regex          	匹配正则表达式
```

示例:

```python
# 年龄大于10岁的数据
Entry.objects.filter(age__gt=10)
# 姓郭的老师有哪些
Entry.objects.filter(name__startswith='D')
# 00年出生的老师
Entry.objects.filter(borthday__year='2000')
```

## 7.做不等的條件篩選

语法:

```python
Author.objects.exclude(條件)
```

作用:

筛选出与所给筛选条件不匹配的对象，多个条件是and的关系

示例:

```python
# 不姓郭的老师
Entry.objects.exclude(name__startswith='郭')
```

## 8.排序查詢 

语法:

```
Entry.objects.order_by("列","-列")
```

作用:

默認是升序排序,如果想要降序則在列名前加 - 號即可

返回值:

queryset 对选哪个

## 9.聚合操作

语法:

```python
import django.db.models import Avg,Max,Min
Enrty.objects.aggregate(Avg('age'),Max('age'),Mix('age'))
```

功能:

对筛选的结果进行聚合

返回值:

字典

## 10.分组聚合

语法:

```python
Entry.objects.annotate(num=Count('id'))
```

作用:

对筛选的结果进行分组聚合

注意:

如果annotate前写values，则values内的字段即分组条件，得到的结果是一个个字典组成的QuerySet对象

如果annotate前不写values，则默认以该表的id分组，得到的是一个个表的对象组成的QuerySet对象

## 11.F查询

语法:

```python
Entry.object.filter(id__gt=F('age'))
```

作用:

F() 的实例可以在查询中引用字段，来比较同一个 model 实例中两个不同字段的值。

说明:

支持 F() 对象之间以及 F() 对象和常数之间的加减乘除和取模的操作。

```python
Entry.object.filter(id__gt=F('age')/2)
```

修改操作也可以使用F函数,比如将每位作者的年龄+1岁

```python
Entry.objects.all().update(age=F("age")+1)
```

## 12.Q查询

作用:

ilter() 等方法中的关键字参数查询都是一起进行“AND” 的。 如果你需要执行更复杂的查询（例如OR语句），你可以使用Q对象

你可以组合& 和| 操作符以及使用括号进行分组来编写任意复杂的Q 对象。同时，Q 对象可以使用~ 操作符取反，这允许组合正常的查询和取反(NOT) 查询

语法示例:

```python
# 查询年龄30岁或者id为1的用户
Entry.objects.filter(Q(age=30)|Q(id=1))
# 查询出生年份不是1991年的用户
Entry.objects.filter(~Q(borthday__year ='1991'))
# 查询姓王且年龄为33岁的用户
Entry.objects.filter(Q(name__startswith='王')&Q(age=30))
```



