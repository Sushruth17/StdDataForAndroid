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



# root
@app.route("/")
def index():
    """
    this is a root dir of my server
    :return: str
    """
    return "This is my root!!!!"


def getData():
    cursor = conn.cursor()
    cursor.execute("select id,name,address,parentname,age from studentinfo")
    data = cursor.fetchall()  # data from database
    cursor.close()
    return data


@app.route('/student_data')
def main():
    # return "Hello turr %s!" % user
    Data = getData()
    print("send data====---------->", Data)
    newData = {'info': Data}
    print("new data--->", str(newData))

    return str(newData)

# GET
@app.route('/student_data/<name>')
def search_student(name):
    cursor = conn.cursor()
    print("im inside search student")
    cursor.execute("select id,name,address,parentname,age from studentinfo where name = '{0}'".format(name))
    searched_student = cursor.fetchall()
    searched_student = {'info': searched_student}
    print("searched student====---------->", searched_student)
    cursor.close()
    return str(searched_student)

# GET
@app.route('/<delstd>')
def delete_student(delstd):
    cursor = conn.cursor()
    print("im inside delete student--->", delstd)
    id22 = cursor.execute("delete from marksinfo where Sid = '{0}'".format(delstd))
    qry = "DELETE FROM `studentinfo` WHERE `studentinfo`.`id` = {0}".format(delstd)
    id2 = cursor.execute(qry)
    print("query--> ", qry)
    conn.commit()
    cursor.close()
    print("deleted id - > ", id22, " and --> ", id2)
    return " Deleted "

@app.route('/api/post_some_data', methods=['POST'])
def get_text_prediction():
    """
    predicts requested text whether it is ham or spam
    :return: json
    """
    json = request.get_json()
    print(json)
    if len(json['text']) == 0:
        return jsonify({'error': 'invalid input'})
    cursor = conn.cursor()
    cursor.execute("insert into studentinfo(name,address,age,parentname) values()")
    cursor.close()
    return jsonify({'Added Suvccessfully'})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
