import execjs

# 921462.715847

with open('baidufanyi.js', 'r') as f:
    js_code = f.read()

loader = execjs.compile(js_code)
result = loader.call('e', 'hell')
# 921462.715847
print(result)
