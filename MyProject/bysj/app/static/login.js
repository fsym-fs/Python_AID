layui.define(['element'],function(exports){

    var $ = layui.$;
    $('.input-field').on('change',function(){
        var $this = $(this),
            value = $.trim($this.val()),
            $parent = $this.parent();

        if(value !== '' && !$parent.hasClass('field-focus')){
            $parent.addClass('field-focus');
        }else{
            $parent.removeClass('field-focus');
        }
    })
    $('.login-button').click(function(){
        uname = $('#username').val();
        pwd = $('#password').val();
        console.log(uname,pwd);
        $.ajax({
            type:'post',
            url:'http://127.0.0.1:5000/admin/login',
            contentType:'application/json',
            dataType:'json',
            data:JSON.stringify({
                'uname':uname,
                'pwd':pwd,
            }),
            success:function(data){
                if(data.code == 200){
                    alert('欢迎您的登录!');
                    window.location.href='http://127.0.0.1:5000/admin/index';
                }
                else{
                    alert(data.error);
                }
            },
        });
    });
    exports('login');
});