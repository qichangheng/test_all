import logging

from class19_logging封装.yaml_handler import read_yaml

# 是所有的配置
config = read_yaml("config.yaml")
log_config = config['log']


def get_logger(
        name=log_config['name'],
        file=log_config['file'],
        logger_level=log_config["logger_level"],
        stream_level=log_config["stream_level"],
        file_level=log_config["file_level"],
        fmt='%(asctime)s--%(filename)s--hanghao:%(lineno)d--%(levelname)s:%(message)s',
):
    """获取到收集器"""
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
    return logger


if __name__ == '__main__':
    logger = get_logger()
    logger.info("hello")
