import os
import pymysql
from flask import Flask, render_template, request
from datetime import datetime


app = Flask(__name__)


connection = pymysql.connect(host='localhost', user='root', passwd='', db='Chinook')


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/", methods=['POST'])
def getvalue():
    Fname = request.form['FirstName']
    Lname = request.form['LastName']
    mail = request.form['Email']
    row = (Fname, Lname, mail)
    connection = pymysql.connect(host='localhost', user='root', passwd='', db='Chinook')
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO Customer (FirstName, LastName, Email) Values (%s, %s, %s);", row)
        connection.commit()
        connection.close()
    return render_template("index.html")



if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)



