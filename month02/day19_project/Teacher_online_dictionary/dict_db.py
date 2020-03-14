"""
服务端
数据处理部分
"""

import pymysql


class Database:
    def __init__(self):
        self.host = 'localhost'
        self.port = 3306
        self.user = 'hhh'
        self.password = '223751093'
        self.charset = 'utf8'
        self.database = 'dict'
        self.connect_database()

    def connect_database(self):
        self.db = pymysql.connect(host=self.host,
                                  port=self.port,
                                  user=self.user,
                                  password=self.password,
                                  database=self.database,
                                  charset=self.charset)

    def create_cursor(self):
        self.cur = self.db.cursor()

    # 帮 server 处理注册 成功 True 失败返回 False
    def register(self, name, passwd):
        # 判断这个姓名的用户是否存在
        sql = "select name from user where name=%s;"
        self.cur.execute(sql, [name])
        r = self.cur.fetchone()  # 如果查询到了说明该用户已经存在
        if r:
            return False  # 不可注册
        else:
            # 插入数据库
            try:
                sql = "insert into user (name,passwd) values (%s,%s);"
                self.cur.execute(sql, [name, passwd])
                self.db.commit()
                return True
            except:
                self.db.rollback()
                return False

    # 帮 server 处理登录 成功 True 失败返回 False
    def login(self, name, passwd):
        # 判断这个姓名的用户是否存在
        sql = "select name from user where name=%s and passwd =%s;"
        self.cur.execute(sql, [name, passwd])
        r = self.cur.fetchone()  # 如果查询到了说明该用户已经存在,且账号密码验证正确
        if r:
            return True  # 登录成功
        else:
            return False

    # 查找单词
    def query(self, word, name):
        self.insert_history(word, name)
        sql = "select mean from words where word = %s;"
        self.cur.execute(sql, [word])
        r = self.cur.fetchone()
        if r:
            return r[0]
        else:
            return "查无此单词!"

    # 插入历史记录
    def insert_history(self, word, name):
        sql1 = "insert into hist(name,word) values(%s,%s)"
        try:
            self.cur.execute(sql1, [name, word])
            self.db.commit()
        except:
            self.db.rollback()

    # 查询历史记录
    def history(self, name):
        sql = "select name,word,time from hist where name = %s order by time desc limit 10;"
        self.cur.execute(sql, [name])
        r = self.cur.fetchall()
        return r
