import heapq
'''
heapq库，取最小的N个元素，参数可以使用lambda，适合数量较小时
'''

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(4, nums))
print(heapq.nsmallest(2, nums))

portfolio = [
    {'name':'a','price':91.3},
    {'name':'b','price':90.2},
    {'name':'c','price':89.3},
    {'name':'d','price':100.3}
]

cheap = heapq.nlargest(3, portfolio, key=lambda s:s['price'])
print(cheap)

#排序
heapq.heapify(nums)
print(nums)


