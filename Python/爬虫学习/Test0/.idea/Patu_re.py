#用正则表达式批量爬取图片
#有漏洞，还在完善

import re
import requests
import urllib.parse
url = 'https://www.duitang.com/search/?kw=%E9%B9%BF%E6%99%97&type=feed'
text = requests.get(url).text
'''
kw = '鹿晗'
kw = urllib.parse.quote(kw)
print(kw)
date = requests.get(url,kw).text
'''
download = re.findall('<a target.*?src="(.*?)".*?</a>',text,re.S)
num = 1
for i in download:
    print(i)
    a = requests.get(i)
    with open(r'C:\Users\64811\Desktop\鹿晗\{}.jpg'.format(num),'wb')as f:
        f.write(a.content)
        num   += 1