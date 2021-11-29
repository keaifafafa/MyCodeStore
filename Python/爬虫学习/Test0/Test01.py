import requests
import json
so = requests.get('https://www.baidu.com/')
print(so.text)
print(so.headers)
print(so.status_code)
print(so.cookies)
print(so)
print(type(so.status_code))
print(type(so))
print(so.content)


#循环测试*******************************
n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
print("1 到 %d 之和为: %d" % (n, sum))
