import pytesseract
# Python图片处理库
from PIL import Image
import cv2

# 创建图片对象
img = Image.open('timg2.jpg')
# 图片转字符串
result = pytesseract.image_to_string(img)
s = ''
s.strip()
print(result)

# https://search.jd.com/Search?keyword=%E5%86%9C%E4%BA%A7%E5%93%81&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E5%86%9C%E4%BA%A7%E5%93%81&stock=1&page=1&s=1&click=0
# https://search.jd.com/Search?keyword=%E5%86%9C%E4%BA%A7%E5%93%81&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E5%86%9C%E4%BA%A7%E5%93%81&stock=1&page=3&s=61&click=0
# https://search.jd.com/Search?keyword=%E5%86%9C%E4%BA%A7%E5%93%81&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E5%86%9C%E4%BA%A7%E5%93%81&stock=1&page=5&s=121&click=0

# https://search.jd.com/Search?keyword=%E5%86%9C%E4%BA%A7%E5%93%81&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E5%86%9C%E4
# %BA%A7%E5%93%81&stock=1&page={}&s={}&click=0
# 1 1
# 2 61
# 3 121
