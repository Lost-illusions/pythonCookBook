'''
3.1解压序列赋值给多个变量
3.2解压可迭代对象赋值给多个变量
'''

data = ['lhy', 30 ,(2012 ,1 ,21)]
name, age, date = data

record = ('Dave', '458656120@qq.com', '111111', '2222222')
name, email, *phone = record
#phone 为列表
print(phone)

#字符串分割
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname, homedir, sh)


def sum(items):
    head, *tail = items
    #if tail 为True， 返回head + sum(tail)，否则返回head
    return head + sum(tail) if tail else head

print(sum([1,2,3,4,5]))
