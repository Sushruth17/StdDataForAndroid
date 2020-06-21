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

# # GET
# @app.route('/Edit/<edit_std>')
# def delete_student(edit_std):
#     cursor = conn.cursor()
#     print("im inside edit student--->", edit_std)
#     id22 = cursor.execute("Update studentinfo "
#                           "set name = '{0}', address = '{1}', parentname = '{2}',"
#                           " age = '{3}' "
#                           "where id ='{4}'".format(name, address, parentname, age, id))
#     # qry = "DELETE FROM `studentinfo` WHERE `studentinfo`.`id` = {0}".format(delstd)
#     # id2 = cursor.execute(qry)
#     # print("query--> ", qry)
#     conn.commit()
#     cursor.close()
#     print("edited----->",id22)
#     return " Edited "


@app.route('/api/post_some_data', methods=['POST'])
def get_text_prediction():
    """
    predicts requested text whether it is ham or spam
    :return: json
    """
    json = request.get_json()
    print("im received json data ",json)
    if len(json['name']) == 0:
         return jsonify({'error': 'invalid input'})
    cursor = conn.cursor()
    cursor.execute("insert into studentinfo(Name,Address,ParentName,Age)"
                   "values('{0}', '{1}', '{2}','{3}')".format(json['name']
                                                               ,json['address']
                                                               ,json['parentname']
                                                               ,json['age']))
    conn.commit()
    cursor.close()
    return 'Added Suvccessfully'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
