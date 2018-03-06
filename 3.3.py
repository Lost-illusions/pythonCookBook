'''
保留最后 N 个元素
1.生成器
2.collections.deque高效实现插入和删除操作的双向列表，适合用于队列和栈
'''

#1.两种生成器，可迭代
if __name__ == '1':
    g1 = (x for x in range(10))

    def odd():
        print('step 1')
        yield 1
        print('step 2')
        yield(3)
        print('step 3')
        yield(5)

    #使用
    next(g1)
    for n in g1:
        print(n)

    g2 = odd()
    next(g2)
    for i in g2:
        print(i)

#
if __name__ == '__main__':
    from collections import deque

    def search(lines, pattern, history=5):
        privious_lines  = deque(maxlen=history)
        for li in lines:
            if pattern in li:
                yield li, privious_lines
            privious_lines.append(li)

    with open(r'1.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-'*20)

    #有限队列
    q1 = deque(maxlen=3)
    #无限队列
    q2 = deque()

