import execjs

with open('hello.js','r') as f:
    js_data = f.read()

# js_data = """
#     function test(name){
#         return "Hello, " + name
#     }
# """
loader = execjs.compile(js_data)
result = loader.call("test", "张三丰")
print(result)