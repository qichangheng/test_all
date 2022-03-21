
# 记录日志

# 第一步：创建一个日志收集器（笔记本:python日志收集器）
import logging

# 得到 root 收集器
root_logger = logging.getLogger('python29')
# 设置收集器的收集等级（）
root_logger.setLevel("DEBUG")

# handler 输出处理器, 流信息，
stream_handler = logging.StreamHandler()
stream_handler.setLevel("DEBUG")

# 把输出处理器添加到收集器上面。
root_logger.addHandler(stream_handler)


# 文件输出处理器
file_handler = logging.FileHandler('log.txt', encoding='utf8')
file_handler.setLevel('INFO')
root_logger.addHandler(file_handler)


# 设置日志格式
fmt = logging.Formatter('%(asctime)s--%(filename)s--hanghao:%(lineno)d--%(levelname)s:%(message)s')
file_handler.setFormatter(fmt)
stream_handler.setFormatter(fmt)


root_logger.debug("debug 等级的日志")
root_logger.info("info 等级的日志")
root_logger.warning("warning 等级的日志")
root_logger.error("error 等级的日志")



# 函数封装
# def get_logger():
#     """
#     参数， 等级， fmt , 文件：filename
#     :return:
#     """
#     logger = logging.getLogger()
#     return logger
#
# logger = get_logger()
# logger.debug()

# 类封装
class MyLogger(logging.Logger):

    def __init__(self):

        # 收集器
        logger = ''

        # handler = logging.FileHandler()

        # logger.addHandler
        pass


# print("记录日志")
# .info('')