import os
import pymysql

connection = pymysql.connect(host='localhost', user='root', passwd='', db='Chinook')

try:
    with connection.cursor() as cursor:
        sql = "select * from Employee where EmployeeId = 5;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    connection.close()