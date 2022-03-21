

# config = read_yaml()
# config = {
#     "log": {
#         "name": "python29",
#         "file": "python19log.txt",
#         "logger_level": "DEBUG",
#         "stream_level": "DEBUG",
#         "file_level": "INFO",
#     },
#
#     "mysql": {
#         "port": 3306,
#         "db_name": "demo"
#     },
#
#     "excel": {
#         "file": "cases.xlsx"
#     }
# }
#
# print(config["log"]["name"])


# 读取yaml
# 安装 pyyaml : pip install pyyaml
import yaml

with open("config.yaml", encoding='utf8') as f:
    conf = yaml.load(f, Loader=yaml.SafeLoader)
    print(conf)


# 写入yaml
with open("another.yaml", 'w', encoding='utf8') as f:
    yaml.dump({"log": "logdemo"}, f)


