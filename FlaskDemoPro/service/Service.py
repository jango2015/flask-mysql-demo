__author__ = " jango "

import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             db='mvcdemo',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


class DbService:
    @staticmethod
    def insert():
        try:
            with connection.cursor() as cursor:
                sql = " insert into `users` (`ID`,`Name`, `Mobile`)VALUES (%s,%s,%s)"
                cursor.execute(sql, ('7', 'flaskDemo7', '16988888888'))
            connection.commit()

        finally:
            connection.close()
    @staticmethod           
    def getall():
        try:
            with connection.cursor() as cursor:
                sql = " Select `ID` ,`Name`,`Mobile` From  `Users` where `ID`>=%s"
                cursor.execute(sql, ('1',))
            connection.commit()
            result = cursor.fetchall()
            print(result)
            return result
        except Exception:
            raise
            cursor.close()
        # finally:
        #     connection.close()

