import pymysql


class Server_Models:
    def __init__(self, db_host='localhost', port=3306, user="hhh",
                 password="223751093",
                 database="dict",
                 charset="utf8"):
        self.host = db_host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset
        self.db = pymysql.connect(host=self.host, port=self.port,
                                  user=self.user,
                                  password=self.password, database=self.database,
                                  charset=self.charset)

    # 创建数据库游标
    def create_cursor(self):
        self.cur = self.db.cursor()

    # 登录功能
    def login(self, name, password):
        sql = "select name from user where name=%s and passwd=%s;"
        self.cur.execute(sql, [name, password])
        r = self.cur.fetchone()
        if r:
            return True
        else:
            return False

    # 注册功能
    def register(self, name, password):
        sql = "select name from user where name=%s;"
        self.cur.execute(sql, [name])
        r = self.cur.fetchone()
        if r:
            return False
        else:
            sql = "insert into user(name,passwd) values(%s,%s);"
            try:
                self.cur.execute(sql, [name, password])
                self.db.commit()
                return True
            except:
                self.db.rollback()
                return False

    # 查看单词功能
    def find_words(self, name, word):
        self.insert_history(name, word)
        sql = "select word,mean from words where word=%s;"
        self.cur.execute(sql, [word])
        r = self.cur.fetchone()
        if r:
            return r
        else:
            return False

    # 插入历史记录
    def insert_history(self, name, word):
        sql = "insert into hist(name,word) values(%s,%s)"
        try:
            self.cur.execute(sql, [name, word])
            self.db.commit()
        except:
            self.db.rollback()

    # 查询历史记录
    def history(self, name):
        sql = "select name,word,time from hist where name = %s order by time desc limit 10;"
        self.cur.execute(sql, [name])
        r = self.cur.fetchall()
        return r
