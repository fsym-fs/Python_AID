
$(function () {
    //加载页面内容到指定元素
    // $('#show').load('/load_server')
    //加载远程页面某一个元素
    // $('#show').load('/load_server #btn2')
    //传输数据(字符串/对象)
    //字符串为get方式传输
    // $('#show').load('/load_server', 'uname=Tom&age=18')
    //对象为post方式传输
    $('#login_nav').load('/public #public_header');
    $('#login_footer').load('/public #public_footer')
});