"""
    csv
            writerow([])
            writerows([()])
            http://mirrors.aliyun.com/ubuntu
"""
import csv
with open('spider.csv','w',encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['步惊云','绝世好剑'])
with open('spider.csv','a',encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows([('聂风','血影狂刀'),('星矢','天马流星拳')])
