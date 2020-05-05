import execjs

js_data = """
    function test(name){
        return "Hello, " + name
    }
"""
loader = execjs.compile(js_data)
result = loader.call("test", "张三丰")
print(result)