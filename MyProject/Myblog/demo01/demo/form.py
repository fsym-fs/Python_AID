from django import forms
from django.core.exceptions import ValidationError
def words(comment):
    if len(comment) < 10:
        raise ValidationError('评论字数不能小于10')
def notusewords(comment):
    if '操' in comment:
        raise ValidationError('错误字符')

def pas(password1,password2):
    if password1 != password2:
        raise ValidationError('用户名或密码错误！')

class CommentForm(forms.Form):
    # name = forms.CharField(max_length=50)
    comment = forms.CharField(
        widget = forms.Textarea(),
        error_messages = { 'required':"评论的内容不能为空!" },#设置为空时的报错信息
        validators=[words, notusewords],#自定义错误类型
    )#设置表单的的样式为Textarea

class PersonForm(forms.Form):
    name = forms.CharField(max_length=17)
    password = forms.CharField(max_length=17,widget=forms.PasswordInput)
    Email = forms.EmailField(max_length=50)
    birth = forms.CharField(max_length=50)
    个性签名 = forms.CharField(max_length=50)

class Person_loginForm(forms.Form):
    name = forms.CharField(max_length=17)
    password = forms.CharField(max_length=17,widget=forms.PasswordInput)
    # Email = forms.CharField(max_length=50)
    # birth = forms.CharField(max_length=50)
    # 个性签名 = forms.CharField(max_length=50)

class Person_registerForm(forms.Form):
    name = forms.CharField(max_length=17)
    密码 = forms.CharField(max_length=17,widget=forms.PasswordInput,validators=[notusewords],)
    确认密码 = forms.CharField(max_length=17,widget=forms.PasswordInput,validators=[pas, notusewords],)
    Email = forms.CharField(max_length=50)
    birth = forms.CharField(max_length=50)
    # 个性签名 = forms.CharField(max_length=50)
    实名 = forms.CharField(max_length=50)

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class consumerForm(forms.Form):
    # print("123")
    pass

class writeForm(forms.Form):
    head = forms.CharField(max_length=50,label='标题',strip=True)
    detail = forms.CharField(widget=forms.Textarea,label='内容',strip=True)
    tag = forms.ChoiceField(label='类别',choices=(('tech', 'Tech'), ('life', 'Life')))
    # BIRTH_YEAR_CHOICES = ('1980', '1981', '1982')
    # birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))