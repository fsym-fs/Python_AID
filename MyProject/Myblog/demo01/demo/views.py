from django.shortcuts import render, HttpResponse,redirect,Http404#导入http接收和输出的模块
from demo.models import Aritcle, Comment, Person   #导入定义数据库模块
from django.template import Context, Template#导入模板用于渲染，添加到网页中
from demo.form import CommentForm, LoginForm, Person_loginForm,Person_registerForm,PersonForm,consumerForm,writeForm
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
# from demo.people import consum

# str_name=""
# str_pass=""
# print("name:"+str_name)
# print("password:"+str_pass)
# Create your views here.
# cc= {}
# us = Person.objects.filter(status = '1')
# if us:
#     cc['us'] = us[0]
# print("123"+us[0])
# print("123")
# print(consum.aa)
# consum.aa=2
# print(consum.aa)
def index(request):
    #退出
    if request.method == 'GET':
        form_consumer = consumerForm()
    if request.method == 'POST':
        form_consumer = consumerForm(request.POST)#表单绑定，将post里的数据绑定到CommentForm
        Person.objects.filter(status='1').update(status='0')
        return redirect(to = 'login')#重定向到url中的name为detial的网页
    context={}
    context['form_consumer'] = form_consumer

    queryset = request.GET.get('tag')
    # print(queruset)
    if queryset:
        article_list = Aritcle.objects.filter(tag = queryset)#查找出所有tag为所要的参数的文章
    else:
        article_list = Aritcle.objects.all()#变量article_list储存Article所有的文章
    context = {}#新建字典
    page_robot = Paginator(article_list,3)#创建一个分页器，每页3个内容
    num = request.GET.get('page')
    # article_list = page_robot.page(request.GET.get('page'))#传递一个页数以跳转到想要的页数

    try:
        article_list = page_robot.page(num)
    except EmptyPage:
        article_list = page_robot.page(page_robot.num_pages)
        # raise Http404("没有本页!")
    except PageNotAnInteger:
        article_list = page_robot.page(1)
    context['article_list'] = article_list #字典context中的article_list键（html中通过检索键提取文章内容）对应article_list变量的值
    massage_list = Person.objects.filter(status = '1')
    # print(consum.consumer_id)
    if massage_list:
        context['massage_list'] = massage_list[0]
    index_page = render(request, 'index.html', context)
    return index_page

def personal(request):
    if request.method == 'GET':
        consumer_form = consumerForm()
        form = PersonForm()
    if request.method == 'POST':
        if 'exit' in request.POST:
            consumer_form = consumerForm(request.POST)
            Person.objects.filter(status='1').update(status='0')
            form = PersonForm()
            return redirect(to = 'login')#重定向到url中的name为detial的网页
        # elif 'input' in request.POST:
        #     form = PersonForm(request.POST)
        #     if form.is_valid():
        #         name = form.cleaned_data['name']
        #         Email = form.cleaned_data['Email']
        #         birth = form.cleaned_data['birth']
        #         个性签名 = form.cleaned_data['个性签名']
        #         Person.objects.filter(status='1').update(name = name, Email = Email, birth=birth,个性签名=个性签名)
        #         consumer_form = consumerForm()
        #         return redirect(to = 'about_me')#重定向到url中的name为detial的网页
    context = {}#新建字典
    context['form'] = form
    massage_list = Person.objects.filter(status = '1')
    if massage_list:
        context['massage_list'] = massage_list[0]
        title_all = Aritcle.objects.filter(name = massage_list[0].name)
        title_Tech = Aritcle.objects.filter(name = massage_list[0].name,tag='tech')
        title_Life = Aritcle.objects.filter(name = massage_list[0].name,tag='life')
        context['title_all'] = title_all
        context['title_Tech'] = title_Tech
        context['title_Life'] = title_Life
        page_robot_all = Paginator(title_all,3)#创建一个分页器，每页3个内容
        page_robot_Tech = Paginator(title_Tech,3)#创建一个分页器，每页3个内容
        page_robot_Life = Paginator(title_Life,3)#创建一个分页器，每页3个内容
        num = request.GET.get('page')
        try:
            title_all = page_robot_all.page(num)
            title_Tech = page_robot_Tech.page(num)
            title_Life = page_robot_Life.page(num)
        except EmptyPage:
            title_all = page_robot_all.page(page_robot_all.num_pages)
            title_Tech = page_robot_Tech.page(page_robot_all.num_pages)
            title_Life = page_robot_Life.page(page_robot_all.num_pages)
            # raise Http404("没有本页!")
        except PageNotAnInteger:
            title_all = page_robot_all.page(1)
            title_Tech = page_robot_Tech.page(1)
            title_Life = page_robot_Life.page(1)
    return render(request,'personal.html',context)

#随心说
def write(request):
    if request.method == 'GET':
        consumer_form = consumerForm()
        writeform = writeForm()
    if request.method == 'POST':
        if 'exit' in request.POST:
            consumer_form = consumerForm(request.POST)
            Person.objects.filter(status='1').update(status='0')
            writeform = writeForm()
            return redirect(to = 'login')#重定向到url中的name为detial的网页
        elif 'input' in request.POST:
            writeform = writeForm(request.POST)
            if writeform.is_valid():
                headline = writeform.cleaned_data['head']
                detail = writeform.cleaned_data['detail']
                tag = writeform.cleaned_data['tag']
                m = Person.objects.filter(status='1')
                if m:
                    c = Aritcle(name = m[0].name,headline = headline,content = detail,tag=tag)#将数据载入实例对象
                    c.save()
                    return redirect(to = 'index')#重定向到url中的name为detial的网页       
    context={}
    context['writeform'] = writeform
    massage_list = Person.objects.filter(status = '1')
    if massage_list:
        context['massage_list'] = massage_list[0]
        title_all = Aritcle.objects.filter(name = massage_list[0].name)
        title_Tech = Aritcle.objects.filter(name = massage_list[0].name,tag='tech')
        title_Life = Aritcle.objects.filter(name = massage_list[0].name,tag='life')
        context['title_all'] = title_all
        context['title_Tech'] = title_Tech
        context['title_Life'] = title_Life
    return render(request,'write.html',context)

#关于我
def about_me(request):
    # person_form={""}
    # consumer_form={''}
    if request.method == 'GET':
        consumer_form = consumerForm()
        form = PersonForm()
    if request.method == 'POST':
        if 'exit' in request.POST:
            consumer_form = consumerForm(request.POST)
            Person.objects.filter(status='1').update(status='0')
            form = PersonForm()
            return redirect(to = 'login')#重定向到url中的name为detial的网页
        elif 'input' in request.POST:
            form = PersonForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                Email = form.cleaned_data['Email']
                birth = form.cleaned_data['birth']
                个性签名 = form.cleaned_data['个性签名']
                Person.objects.filter(status='1').update(name = name, Email = Email, birth=birth,个性签名=个性签名)
                consumer_form = consumerForm()
                return redirect(to = 'about_me')#重定向到url中的name为detial的网页
    context = {}#新建字典
    context['form'] = form
    massage_list = Person.objects.filter(status = '1')
    if massage_list:
        context['massage_list'] = massage_list[0]
    return render(request,'about_me.html',context)


def index_login(request):
    context = {}
    if request.method == 'GET':
        form = Person_loginForm
    if request.method == 'POST':
        form = Person_loginForm(data=request.POST)
        if form.is_valid():
            nam = form.cleaned_data['name']#取出name
            pas = form.cleaned_data['password']#取出name
            if Person.objects.filter(password=pas,name=nam):
                # cc = Person.objects.filter(password=pas,name=nam)
                # m = Person.objects.filter(password=pas,name=nam)
                Person.objects.filter(password=pas,name=nam).update(status='1')
                # m[0].update(status='1')
                # print(m[0].id)
                # consum.consumer_name = nam
                # consum.consumer_pass = pas
                # consum.consumer_id = m[0].id
                return redirect(to = 'index')
            # else:
            #     raise ValidationError(message='用户名已存在', code='invalid')
    context['form'] = form
    return render(request,'login.html', context)

def index_register(request):
    context = {}
    if request.method == 'GET':
        form = Person_registerForm
    if request.method == 'POST':
        form = Person_registerForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']#取出name
            pas1 = form.cleaned_data['密码']#取出comment
            pas2 = form.cleaned_data['确认密码']#取出comment
            Email = form.cleaned_data['Email']
            birth = form.cleaned_data['Email']
            # 个性签名 = form.cleaned_data['个性签名']
            实名 = form.cleaned_data['实名']
            if pas1 == pas2:
                c = Person(name = name, password = pas1, Email=Email, birth=birth,实名=实名)#将数据载入实例对象
                c.save()
                return redirect(to='login')
    context['form'] = form
    return render(request,'login.html', context)

def detail(request, page_num):
    a = Aritcle.objects.get(id = page_num)
    # print(page_num)
    if request.method == 'GET':
        consumer_form = consumerForm()
        form = CommentForm()
    if request.method == 'POST':
        if 'exit' in request.POST:
            form_consumer = consumerForm(request.POST)#表单绑定，将post里的数据绑定到CommentForm
            Person.objects.filter(status='1').update(status='0')
            # print("123")
            form = CommentForm()
            return redirect(to = 'login')#重定向到url中的name为detial的网页
        elif 'input' in request.POST:
            form = CommentForm(request.POST)#表单绑定，将post里的数据绑定到CommentForm
            #判断表单里的数据是否校验通过
            if form.is_valid():#校验通过的数据会存储在form.cleaned_data中
                # name = form.cleaned_data['name']#取出name
                comment = form.cleaned_data['comment']#取出comment
                us = Person.objects.filter(status='1')
                if us:
                    c = Comment(name = us[0].name, comment = comment, belong_to=a)#将数据载入实例对象
                else:
                    c = Comment(name = '游客', comment = comment, belong_to=a)#将数据载入实例对象
                # print(us[0].name)
                # c = Comment(name = us[0].name, comment = comment, belong_to=a)#将数据载入实例对象
                c.save()#储存实例对象，但不添加进数据库
                return redirect(to = 'detail', page_num=page_num)#重定向到url中的name为detial的网页
    context = {}
    context['form'] = form
    best_comment = Comment.objects.filter(best_comment=True, belong_to=a)
    if best_comment:
        context['best_comment'] = best_comment[0]
    aritcle = Aritcle.objects.get(id = page_num)
    context['article'] = aritcle
    massage_list = Person.objects.filter(status = '1')
    # print(consum.consumer_id)
    if massage_list:
        context['massage_list'] = massage_list[0]
    # context['comment_list'] = comment_list
    # #退出
    # if request.method == 'GET':
    #     form_consumer = consumerForm()
    # if request.method == 'POST':
    #     form_consumer = consumerForm(request.POST)#表单绑定，将post里的数据绑定到CommentForm
    #     Person.objects.filter(status='1').update(status='0')
    #     print("123")
    #     return redirect(to = 'login')#重定向到url中的name为detial的网页
    # con={}
    # con['form_consumer'] = form_consumer
    return render(request,'detail.html',context)

# def index_login(request):
#     context = {}
#     if request.method == 'GET':
#         form = AuthenticationForm
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             login(request,form.get_user())
#             return redirect(to='index')
#     context['form'] = form
#     return render(request,'login.html', context)

# def index_register(request):
#     context = {}
#     if request.method == 'GET':
#         form = UserCreationForm
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(to='login')
#     context['form'] = form
#     return render(request,'login.html', context)
# def detail(request, page_num):
#     context = {}
#     form = CommentForm()
#     a = Aritcle.objects.get(id = page_num)
#     best_comment = Comment.objects.filter(best_comment=True, belong_to=a)
#     if best_comment:
#         context['best_comment'] = best_comment[0]
#     aritcle = Aritcle.objects.get(id = page_num)
#     context['article'] = aritcle
#     # context['comment_list'] = comment_list
#     context['form'] = form
#     return render(request,'detail.html',context)

# def detail_comment(request, page_num):
#     form = CommentForm(request.POST)#表单绑定，将post里的数据绑定到CommentForm
#     if form.is_valid():#校验通过的数据会存储在form.cleaned_data中
#         a = Aritcle.objects.get(id = page_num)
#         name = form.cleaned_data['name']#取出name
#         comment = form.cleaned_data['comment']#取出comment
#         c = Comment(name = name, comment = comment, belong_to=a)#将数据载入实例对象
#         c.save()#储存实例对象，但不添加进数据库
#         return redirect(to = 'detail', page_num=page_num)#重定向到url中的name为detial的网页

# def about_me(request):
#     # print(cc)
#     # print('name:'+consum.consumer_name)
#     if request.method == 'GET':
#         form = PersonForm()
#     if request.method == 'POST':
#         form = PersonForm(request.POST)#表单绑定，将post里的数据绑定到CommentForm
#         #判断表单里的数据是否校验通过
#         if form.is_valid():#校验通过的数据会存储在form.cleaned_data中
#             name = form.cleaned_data['name']#取出name
#             Email = form.cleaned_data['Email']#取出comment
#             birth = form.cleaned_data['birth']#取出name
#             个性签名 = form.cleaned_data['个性签名']#取出comment
#             Person.objects.filter(status='1').update(name = name, Email = Email, birth=birth,个性签名=个性签名)
#             # c = Person(name = name, Email = Email, birth=birth,个性签名=个性签名)#将数据载入实例对象
#             # c.save()#储存实例对象，但不添加进数据库
#             return redirect(to = 'about_me')#重定向到url中的name为detial的网页
#     context = {}#新建字典
#     context['form'] = form
#     # str1=consum.consumer_name
#     # str2=consum.consumer_pass
#     # print("str1:"+str1+"   str2:"+str2)
#     massage_list = Person.objects.filter(status = '1')
#     # print(consum.consumer_id)
#     if massage_list:
#         context['massage_list'] = massage_list[0]
#     # print(user_massage.name)
#     return render(request,'about_me.html',context)

