
# try:
#     f = open('demo.txt')
#     f.read()
# except:
#     print("hello.")
#     pass
# finally:
#     f.close()
#
# # with open()


# 可不可以把异常分组
# 分组有什么好处！！！
# 如果你们发现了一个验证级别 为阻塞级别的bug, :短信通知所有相关人员马上集合。
# 轻微级别的 bug,
try:
    1 / 0
    ['yuz'][8]
    {"name": "yuz"}['age']

except (IndexError) as e:
    # 短信通知。
    print("可以同时捕获 indexerro, 和 keyerror")
except KeyError as e:
    print("eoof")
# except KeyError as e:
#     print()
except ZeroDivisionError as e:
    # 记录日志，
    print("除法出错了。")



# 对你的代码不负责任
# except Exception as e:
#     print("其他错误类型。")

if 2 == 2:
    pass

elif 2 == 2:
    pass

if 2 == 2:
    pass

