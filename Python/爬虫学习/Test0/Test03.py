import requests
'''
url = 'https://www.bilibili.com/'
response = requests.get(url)

print(response.status_code)
print(response.text)
print(type(response.cookies))
#选择语句练习

i = 68
if(i == 6):
    print('6666')
elif(i < 6):
    print('low')
else:
    print('high')
#循环语句练习
#while循环练习
a = 1
while a <= 10:
    if (a == 6):
        continue
    print(a)
    a += 1
    
#无限循环代码
m = 1
while(m):print('sire')
#for循环
language = ['c','c++','python','java','易语言']
for q in language:
    print(q)
    '''

#range()函数的遍历
for t in range(6):
    print('nice!!!')
#也可以使range以指定数字开始并指定不同的增量(甚至可以是负数，有时这也叫做'步长'):
for s in range(0,13,3):
    print(s)
