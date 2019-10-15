import logging
import os

# 项目路径
prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 当前文件的上一级的上一级目录（增加一级）
# print(prj_path)
# print(os.path.abspath(__file__))
# print(os.path.dirname(os.path.abspath(__file__)))
# print(os.pardir)
data_path = os.path.join(prj_path, 'data','test_user_data.xlsx')  # 数据目录,拼接路径
# print(data_path)

test_path = os.path.join(prj_path, 'test')   # 用例目录
# print(test_path)

log_file = os.path.join(prj_path, 'log', 'log.txt')  # 更改路径到log目录下
# print(log_file)
report_file = os.path.join(prj_path, 'report', 'report.html')  # 更改路径到report目录下
# print(report_file)

# log配置
logging.basicConfig(level=logging.DEBUG,  # log level
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',  # log格式
                    datefmt='%Y-%m-%d %H:%M:%S',  # 日期格式
                    filename=log_file,  # 日志输出文件
                    filemode='a')  # 追加模式


# 数据库配置,存储用户名（user）和密码(password)
db_host = 'localhost'
db_port = 3306
db_user = 'root'
db_passwd = '666888'
db = 'api_test'

# 邮件配置
smtp_server = 'smtp.163.com'
smtp_user = '18986032799@163.com'
smtp_password = 'yujian900424'

sender = smtp_user  # 发件人
receiver = '18986032799@163.com'  # 收件人
subject = '接口测试报告'  # 邮件主题
