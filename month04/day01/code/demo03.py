from urllib import parse
params = parse.urlencode({'wd':'陈钰琪','pn':'10'})
# url = 'http://www.baidu.com/s?'+params
# url = 'http://www.baidu.com/s?%s'%(params)
url = 'http://www.baidu.com/s?{}'.format(params)
print(url)
# https://www.guazi.com/huaian/dazhong/o2/#bread
# https://www.guazi.com/huaian/dazhong/o3/#bread
for page in range(1,21):
    url = 'https://www.guazi.com/huaian/dazhong/o{}/#bread'.format(page)
    print(url)
