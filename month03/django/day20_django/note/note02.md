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
           