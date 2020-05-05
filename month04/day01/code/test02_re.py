"""
    贪婪匹配和非贪婪匹配
"""
import re

html = """
<div class="animal">
    <p class="name">
			<a title="Tiger"></a>
    </p>
    <p class="content">
			Two tigers two tigers run fast
    </p>
</div>

<div class="animal">
    <p class="name">
			<a title="Rabbit"></a>
    </p>

    <p class="content">
			Small white rabbit white and white
    </p>
</div>
"""
patterns = re.compile('<a title="(.*?)"></a>.*?</p>.*?<p class="content">(.*?)</p>', re.S)
r_list = patterns.findall(html)
print(r_list)
str = ''
for i in r_list:
    str += """
    动物名称 ：%s
	动物描述 ：%s
    **********************************************
    """ % (i[0], i[1].strip())
print(str)
