import logging


class LoggerHandler():
    def __init__(self,
                 name=None,
                 file=None,
                 logger_level='DEBUG',
                 stream_level='DEBUG',
                 file_level='INFO',
                 fmt='%(asctime)s--%(filename)s--hanghao:%(lineno)d--%(levelname)s:%(message)s',
                 ):
        logger = logging.getLogger(name)
        # 设置收集器的级别
        logger.setLevel(logger_level)

        # 输出管理器
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(stream_level)
        logger.addHandler(stream_handler)

        # 格式
        fmt = logging.Formatter(fmt)
        stream_handler.setFormatter(fmt)

        if file:
            file_handler = logging.FileHandler(file, encoding='utf8')
            file_handler.setLevel(file_level)
            logger.addHandler(file_handler)
            file_handler.setFormatter(fmt)
        self.logger = logger


class LoggerHandler2(logging.Logger):
    def __init__(self,
                 name=None,
                 file=None,
                 logger_level='DEBUG',
                 stream_level='DEBUG',
                 file_level='INFO',
                 fmt='%(asctime)s--%(filename)s--hanghao:%(lineno)d--%(levelname)s:%(message)s',
                 ):

        super().__init__(name, logger_level)


        # 设置收集器的级别
        self.setLevel(logger_level)

        # 输出管理器
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(stream_level)
        self.addHandler(stream_handler)

        # 格式
        fmt = logging.Formatter(fmt)
        stream_handler.setFormatter(fmt)

        if file:
            file_handler = logging.FileHandler(file, encoding='utf8')
            file_handler.setLevel(file_level)
            self.addHandler(file_handler)
            file_handler.setFormatter(fmt)




if __name__ == '__main__':

    logger = LoggerHandler2()
    logger.info("info 信息")

