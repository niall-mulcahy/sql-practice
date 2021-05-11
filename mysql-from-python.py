import os
import pymysql

username = os.getenv('username')

connection = pymysql.connect(host='localhost',
                             user='username',
                             password='passwd',
                             database='db',)

try:
    with connection.cursor() as cursor:
        sql = "select * from Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    connection.close()