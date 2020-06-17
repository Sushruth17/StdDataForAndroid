from flask import Flask, request, jsonify
import pymysql
from pymysql.constants.FIELD_TYPE import JSON
import json

app = Flask(__name__)

conn = pymysql.connect(host='localhost',
                       user='root',
                       password='',
                       charset='utf8mb4',
                       db='studentdb',
                       cursorclass=pymysql.cursors.DictCursor)
cursor = conn.cursor()


# root
@app.route("/")
def index():
    """
    this is a root dir of my server
    :return: str
    """
    return "This is my root!!!!"


def getData():
    cursor.execute("select * from studentinfo")
    data = cursor.fetchall()  # data from database
    return data


@app.route('/student_data')
def main():
    # return "Hello turr %s!" % user
    data = getData()
    sendData = JSON()
    sendData = sendData["info", data]
    print("send data====---------->", sendData)
    # data = {k.lower(): v for k, v in data.items()}
    newData = []
    for i in sendData:
        newData.append({k.lower(): v for k, v in i.items()})
    # newData ={"info:{0}".format(newData)}
    print("new data--->", str(newData))
    return str(newData)


# @app.route("/studentinfo",methods=['GET','POST'])
# def showTable():
#     data = getData()
#     print("data====---------->", data)
#     return data


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
