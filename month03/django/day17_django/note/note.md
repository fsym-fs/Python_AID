# django02

## view

    1.请求方式
        判断请求方式:
            request.method == 'xxx'
            
        GET:
            xxx?xxx=xxx&xxx=xxx
            取单个参数值单个值(最后一个值)
                request.GET['参数名']
                request.GET.get('参数名','默认值')
            取单个参数的所有值
                request.GET.getlist('参数名')
                   返回列表
        POST:
        
            *提交数据在请求体里
            
            csrf:
                取消 csrf 验证
                删除 settings.py 中 MIDDLEWARE 中的 CsrfViewsMiddleWare 的中间件
                MIDDLEWARE = [
                    ...             
                    # 'django.middleware.csrf.CsrfViewMiddleware',                
                    ...                
                ]
                
            取单个参数值单个值(最后一个值)
                request.POST['参数名']
        
        **GET VS POST:**
            场景上:
                GET:
                    一般是向服务器获取数据(html/jpg/视频)
                POST:
                    用户提交数据给服务器(登录/注册/搜索/添加信息)
            提交数据:
                GET:
                    在url上用查询字符串的形式取去提交数据(数据少)
                    数据在请求的起始行中的path上
                 POST:
                    表单POST提交
                    数据在请求的请求体(body)中
                    POST请求包含Content/type请求头