#正则表达式练习

import requests as es
import re
s = es.get('http://www.bilibili.com')
print(s)
ccc = 'hello 1234567 world is cool'
#非贪婪匹配
result = re.match('^he.*?(\d+).*cool$',ccc)#贪婪匹配需要去掉问号，结果为‘7’
print(result)
print(result.group(1))#输出的是‘1234567’
#含有换行符的
ddd = '''hello 541111111 is
         nice cool'''
result = re.match('he.*?(\d+).*?cool$',ddd,re.S)
print(result)
print(result.group(1))

html = '''<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君">但愿人长久</a>
        </li>
    </ul>
</div>'''
results = re.findall('<li.*?.singer=(.*?)</a>',html,re.S)
print(results)
for i in results:
    print(i)