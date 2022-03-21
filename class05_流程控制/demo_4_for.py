songs = ['爱转角', "晴天", '人来人往', '左手指月', "明明就","雨泽很帅"]

# print("正在播放歌曲：{}".format(songs[0]))
# print("正在播放歌曲：{}".format(songs[1]))
# print("正在播放歌曲：{}".format(songs[2]))
# print("正在播放歌曲：{}".format(songs[3]))


# for 循环，遍历，迭代， 是自动播放所有列表（序列）当中的元素
# for e in songs:
#     print("正在播放歌曲：{}".format(e))


# 元组可不可以使用 for 循环，可以。

# 字典可以使用 for 循环吗？？
# 对字典使用 for 循环，取到的默认是所有的 key
# 取所有的值？？ for e in yuz.values()
# 取 key, value,  for key, values in yuz.items()
yuz = {"name": "yuz", "age": 19, "hobby": "coding"}
# for e in yuz.values():
#     print(e)

for e in yuz:
    print(e) # "name"
    # yuz[e]  ==> yuz["name"]
    print(yuz[e])

# for key, value in yuz.items():
#     print("keys:{}, values:{}".format(key, value))