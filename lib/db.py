import pymysql
import sys
sys.path.append('..')  # 提升一级到项目更目录下
from config.config import *  # 从项目根目录下导入


# 获取连接方法
def get_db_conn():
    conn = pymysql.connect(host=db_host,
                           port=db_port,
                           user=db_user,
                           passwd=db_passwd,  # passwd 不是 password
                           db=db)

    return conn #返回数据库连接对象


# 封装数据库查询操作
def query_db(sql):
    logging.debug(sql)
    conn = get_db_conn()  # 获取连接
    cur = conn.cursor()  # 建立游标
    cur.execute(sql)  # 执行sql
    conn.commit()
    result = cur.fetchall()  # 获取所有查询结果
    logging.debug(result)
    cur.close()  # 关闭游标
    conn.close()  # 关闭连接
    return result  # 返回结果


# 封装更改数据库操作
def change_db(sql):
    logging.debug(sql)
    conn = get_db_conn()  # 获取连接
    cur = conn.cursor()  # 建立游标
    try:
        cur.execute(sql)  # 执行sql
        conn.commit()  # 提交更改，插入，删除，更新操作都需要conn.commit()
    except Exception as e:
        conn.rollback()  # 回滚
        logging.error(str(e))
    finally:
        cur.close()  # 关闭游标
        conn.close()  # 关闭连接


# 封装常用数据库操作
def check_user(name):
    # 注意sql中''号嵌套的问题
    sql = "select * from user where name = '{}'".format(name)
    result = query_db(sql)
    return True if result else False
    # if result:  #result非空
    #     return  True
    # else:
    #     return  False


def add_user(name, password):
    sql = "insert into user (name, passwd) values ('{}','{}')".format(name, password)
    change_db(sql) #调用封装更改数据库操作函数


def del_user(name):
    sql = "delete from user where name='{}'".format(name)
    change_db(sql) #调用封装更改数据库操作函数


