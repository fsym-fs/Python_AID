import json

from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.core.paginator import Paginator
from django.views import View

from .models import Goods, User


# Create your views here.
def ajaxme(request):
    return render(request,'alipay.html')


def ajaxpost(request):




    goods=Goods.objects.filter(is_active=True)


    p = Paginator(goods, 3)         #每次展示几个商品
    i=int(request.GET.get('id',1))
    if i <1:
        i=p.num_pages
    if i>p.num_pages:
        i=1
    q = p.page(i)
    data = []
    for i in q:
        item={}

        item['img']=str(i.picture)
        item['title']=i.name
        item['msg']=i.introduce
        item['price']=i.price
        item['page']=p.num_pages
        item['GoodId']=i.id
        data.append(item)


    # a = {'w': '123'}
    # a = json.dumps(a, separators=(',', ':'))
    return JsonResponse({'code':200,'data':data,"page":p.num_pages})


def kjlt(request):
    return render(request,'index.html')




class Goods_good(View):

    def get(self,request):
        return render(request, 'goods.html')
    def post(self,request):
        base_dir='/home/tarena/桌面/kjlt/kjlt/static/images/thumb/'
        id=request.POST.get('token','meiyou')
        # token=request.POST.get('token','meiyou') 获取用户token
        try:
            pic_obj=request.FILES['myfile']
        except:
            return render(request,'goodspost404.html')

        title=request.POST.get('title')
        pic_name=pic_obj.name
        picture="/static/images/thumb/"+pic_name
        price=request.POST.get('price')
        key=request.POST.get('key')
        introduce=request.POST.get('introduce')
        # number=request.POST.get('number')
        if not title or not price  or  not introduce:
            return render(request,'goodspost404.html')

        with open(base_dir +pic_name,'wb') as f:
            data=pic_obj.file.read()
            f.write(data)
        try:
            Goods.objects.create(name=title,price=price,introduce=introduce,picture=picture,user_id=1)
            return render(request,'goodspost200.html')
        except Exception as e:


            return render(request,'goodspost404.html')


class update_good(View):
    def get(self,request):

        return render(request,'update_good.html')
    def post(self,request,*args,**kwargs):
        new_title=request.POST.get('title')
        new_price=request.POST.get('price')
        new_key=request.POST.get('key')
        new_introduce=request.POST.get('introduce')
        good_id=request.POST.get('GoodId')#获取商品id
        user_id=request.POST.get('token')#获取用户id
        good=Goods.objects.get(id=good_id)
        try:
            if new_title:
                good.name=new_title
            if new_price:
                good.price=float(new_price)
            if new_introduce:
                good.introduce=new_introduce
            good.save()
            return render(request,'goodupdate200.html')
        except:
            return HttpResponse('error')


class Goods_buy(View):

    def get(self,request):

        return render(request,'goodsbuy.html')

class goods_buy_view(View):
    def get(self,request,*args,**kwargs):
        good_id=int(request.GET.get('id'))
        user_id=int(request.GET.get('userid'))

        good=Goods.objects.get(id=good_id)
        uesr=User.objects.get(id=user_id)
        data={}
        data['good']=good.name
        data['address']=uesr.address
        return JsonResponse(data)