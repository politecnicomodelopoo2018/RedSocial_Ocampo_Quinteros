import pymysql

class DB (object):
    __instance = None
    __host = None
    __user = None
    __passwd = None
    __db = None

    def __new__(cls, *args, **kwargs):
        if DB.__instance is None:
            DB.__instance = object.__new__(cls)
        return DB.__instance

    def SetConnection (self, host, user, passwd, db):
        self.__host = host
        self.__user = user
        self.__passwd = passwd
        self.__db = db

    def run(self, query):
        db = pymysql.connect(host=self.__host, user=self.__user, passwd=self.__passwd, db=self.__db, charset="utf8", autocommit=True)
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute(query)
        db.close()
        return cursor