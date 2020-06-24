from flask import Flask, request, jsonify
import pymysql
from pymysql.constants.FIELD_TYPE import JSON, SET
import json


dataSignInDict = {}

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

@app.route('/student_data')
def main():
    # return "Hello turr %s!" % user
    cursor = conn.cursor()
    cursor.execute("select id,name,address,parentname,age from studentinfo")
    Data = cursor.fetchall()  # data from database
    cursor.close()
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


@app.route('/api/add_data', methods=['POST'])
def addStudent():
    """
    predicts requested text whether it is ham or spam
    :return: json
    """
    json = request.get_json()
    print("im received json data ", json)
    if len(json['name']) == 0:
        return jsonify({'error': 'invalid input'})
    cursor = conn.cursor()
    cursor.execute("insert into studentinfo(Name,Address,ParentName,Age)"
                   "values('{0}', '{1}', '{2}','{3}')".format(json['name']
                                                              , json['address']
                                                              , json['parentname']
                                                              , json['age']))
    conn.commit()
    cursor.close()
    return 'Added Suvccessfully'


@app.route('/api/edit_data', methods=['POST'])
def editStudent():
    json_edit = request.get_json()
    print("received json EDIT data ", json_edit)
    if len(json_edit['name']) == 0:
        return jsonify({'error': 'invalid input'})
    cursor = conn.cursor()
    cursor.execute("""UPDATE studentinfo SET Name = %s ,Age = %s ,ParentName = %s ,Address = %s WHERE id = %s """, (json_edit['name'], json_edit['age']
                                                           , json_edit['parentname']
                                                           , json_edit['address'], json_edit['id']))

    conn.commit()
    cursor.close()
    return 'Edited Suvccessfully'


@app.route('/api/sign_in_data',methods=['GET','POST'])
def signIn():
    json_SignIn = request.get_json()
    print("received json Sign in data ", json_SignIn)
    username = json_SignIn['username']
    password = json_SignIn['password']
    print(len(username))
    print(len(password))
    if len(username) == 0 or len(password)== 0:
        return jsonify('Please fill all the fields')
    cursor = conn.cursor()
    print(" passowrd -->",password)
    pwd = "select user_password from tbl_user where user_username = \"{}\"".format(username)
    print("pwd-------->", pwd)
    cursor.execute(pwd)
    records = cursor.fetchone()
    print("record------------->", records)
    print("password---->", password)
    if records != None:
        if records['user_password'] == password:
            return "Successfully signed in"
        else:
            return "Password wrong"
    else:
        return "User wrong"



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
