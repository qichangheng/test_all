# a = []
#
# if type(a) == list:
#     print("hello world")
#
#
# if isinstance((1,2), (list, tuple )):
#     print("hello world")


# 不太可能出现 3 层 for
lst = [
    ["yuz", "wuming", "tt"],
    [16, 18, 18],
    ["男", "女", "不知道"]
]

# for 循环的执行，是从内到外的
for group in lst:
    # group = ["yuz", "wuming", "tt"]
    for e in group:
        print(e)



lst = [
    ['name', 'age', 'gender'],
    ["yuz", 16, "男"],
    ['tt', 18, '女'],
    ["wuming", 19, "不知道"]
]

new_lst = []

title = lst[0]
for column in lst[1:]:
    dic = {}
    for idx, e in enumerate(column):
        key = title[idx]
        dic[key] = e
    new_lst.append(dic)

print(new_lst)

# 封装（编程思维）
# 封装（抽象）
# 1，


