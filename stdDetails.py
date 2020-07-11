import json
import re
from copy import deepcopy

import pymysql
from flask import Flask, request, jsonify

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
    cursor.close()
    searched_student = {'info': searched_student}
    print("searched student====---------->", searched_student)
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
    cursor.execute("""UPDATE studentinfo SET Name = %s ,Age = %s ,ParentName = %s ,Address = %s WHERE id = %s """,
                   (json_edit['name'], json_edit['age']
                    , json_edit['parentname']
                    , json_edit['address'], json_edit['id']))

    conn.commit()
    cursor.close()
    return 'Edited Suvccessfully'


@app.route('/api/sign_in_data', methods=['POST'])
def signIn():
    print("sign_in_data method called ")
    json_SignIn = request.get_json()
    print("received json Sign in data ", json_SignIn)
    username = json_SignIn['username']
    password = json_SignIn['password']
    print(len(username))
    print(len(password))
    if len(username) == 0 or len(password) == 0:
        return 'Please fill all the fields'
    cursor = conn.cursor()
    print(" passowrd -->", password)
    pwd = "select user_password from tbl_user where user_username = \"{}\"".format(username)
    print("pwd-------->", pwd)
    cursor.execute(pwd)
    records = cursor.fetchone()
    cursor.close()
    print("record------------->", records)
    print("password---->", password)

    if records != None:
        if records['user_password'] == password:
            return "Successfully signed in"
        else:
            return "Password wrong"
    else:
        return "User wrong"


@app.route('/api/sign_up_data', methods=['GET', 'POST'])
def signUp():
    json_SignIn = request.get_json()
    print("received json Sign in data ", json_SignIn)
    name = json_SignIn['name']
    username = json_SignIn['username']
    email_id = json_SignIn['email id']
    password = json_SignIn['password']
    confirm_password = json_SignIn['confirm password']
    if password != confirm_password:
            return "Password Does Not Match"
    print(len(username))
    print(len(password))
    if len(username) == 0 or len(password) == 0:
        return 'Please fill all the fields'
    cursor = conn.cursor()
    cursor.execute("""select user_email_id from tbl_user where user_role = "teacher" and user_status = "not created" """)
    email_froom_db = cursor.fetchall()
    email_froom_db = [sub['user_email_id'] for sub in email_froom_db]
    print("----email from db----",email_froom_db)
    print("-----eamilid from app----",email_id)
    if email_id == email_froom_db[0]:
        cursor.callproc('sp_createUser', (name, username, password))
        data = cursor.fetchall()
        print(data)
        if len(data) is 0:
            conn.commit()
            cursor.close()
            return "User Created Successfully"
        else:
            cursor.close()
            return json.dumps({'error': str(data[0])})
    else:
        return "you are not allowed to sign up"


@app.route('/marks/<studentid>')
def get_student_marks(studentid):
    cursor = conn.cursor()
    print("im inside get marks student")
    cursor.execute("select id,marks,subid from marksinfo where sid = '{0}'".format(studentid))
    marks_data = cursor.fetchall()
    print("marksdata---->",marks_data)
    if marks_data != ():
        subid = [sub['subid'] for sub in marks_data]

        cursor.execute("SELECT id,name FROM `subjectinfo` WHERE id IN {0}".format(tuple(subid)))
        sub_data = cursor.fetchall()
        # sub_name = [sub['name'] for sub in sub_data]
        print("marks_data====---------->", str(marks_data))
        print("sub_data====---------->", str(sub_data))
        subMraks = []
        for i in marks_data:
            for j in sub_data:
                if i['subid'] == j['id']:
                    dic = deepcopy(i)  # creates a deepcopy of row, so that the
                    dic.update(j)  # update operation doesn't affects the original object
                    subMraks.append(dic)
        print("--sub marks", subMraks)
        newData = {'infoMarks': subMraks}
        print("new data--->", str(newData))
        cursor.close()
        return str(newData)
    return ""

@app.route('/topperStudent',methods=['GET', 'POST'])
def acedamic_topper():
    cursor = conn.cursor()
    json_Data = request.get_json()
    print("received json data ", json_Data)
    year = json_Data['year']
    branch = json_Data['branch']
    print("---------BRANCH------------",branch)
    print("im inside achedamic topper student")
            # cursor.execute("select sid,Sum(marks) from marksinfo where year = '{0}'"
            #                "group by sid order by Sum(marks) desc".format(year))
            # sid_marks = cursor.fetchone()
            # print("sid_marks====---------->", sid_marks)
            # sid = sid_marks.get("sid")
            # print("sid",sid)
            # cursor.execute("select name from studentinfo where id = '{0}'".format(sid))
            # topper = cursor.fetchall()
            # print("topper name====---------->", topper)

    if (branch != 'ECE') and (branch != 'CSE') and (branch != 'ISE'):
        print("cursor executing without branch")
        cursor.execute("""select studentinfo.name,marksinfo.sid,year,Sum(marksinfo.marks) as total
        from marksinfo inner join studentinfo ON marksinfo.sid=studentinfo.id 
        where year = %s group by sid order by Sum(marksinfo.marks) DESC""",(year))
    else :
        print("cursor executing with branch")
        cursor.execute("""select studentinfo.name,marksinfo.sid,branchinfo.Name,year,Sum(marksinfo.marks) as total
        from marksinfo inner join studentinfo ON marksinfo.sid=studentinfo.id
        join branchinfo ON branchinfo.id=studentinfo.Bid
        where year = %s and branchinfo.Name = %s group by sid order by Sum(marksinfo.marks) DESC""",(year,branch))
    topper = cursor.fetchone()
    if topper!= None:
        print("topper_====---------->", topper)
        cursor.close()
        total = topper.get("total")
        print("total==---------->", total)
        topper["total"] = str(total)
        new_topper = []
        new_topper.append(topper)
        print("sid_marks====---------->", new_topper)
        new_topper = {'infoTopper': new_topper}
        print("sid_marks====---------->", new_topper)
        return str(new_topper)
    else:
        return "No Data Found"

@app.route('/topper')
def any_year_topper():
    cursor = conn.cursor()
    cursor.execute("""select studentinfo.name,marksinfo.sid,year,Sum(marksinfo.marks) as total
        from marksinfo inner join studentinfo ON marksinfo.sid=studentinfo.id 
        group by sid order by Sum(marksinfo.marks) DESC""")
    anyYearTopper = cursor.fetchone()
    anyYearTopperList = []
    anyYearTopperList.append(anyYearTopper)
    anyYearTopperList = {'infoTopper': anyYearTopperList}
    print("Any year topper",anyYearTopperList)
    regex = "[A-Za-z0-9 ',:{}\[\]]*(Decimal+\('([0-9]*)'\))[A-Za-z0-9 ',:{}\[\]]"
    # for i in anyYearTopper:
    #         # print(i)
    #         strr = i.get('total')
    #         print("strrrrrrrrrrrrrrrrr",str)
    #         match = re.match(regex,strr)
    #         strr = strr.replace(match.group(1),match.group(3))
    #         print("numm"+strr)

    newstrr = ""
    i = 1
    anyYearTopperList = str(anyYearTopperList)
    while 1:
        # strr = "ybuyg97gDecimal('344')"
        # print("string json",strr)
        matchedResult = re.match(regex,anyYearTopperList)
        print("match", matchedResult)
        if matchedResult != None:
            anyYearTopperList = anyYearTopperList.replace(matchedResult.group(1),matchedResult.group(2))
            print("numm",anyYearTopperList)

        # return newstrr
        else:
            print("NO match found in ----->")
            print("Final aresutl - > ", anyYearTopperList)
            break

    return anyYearTopperList

# """select studentinfo.name,marksinfo.sid,branchinfo.Name,year,Sum(marksinfo.marks) as total
# from marksinfo inner join studentinfo ON marksinfo.sid=studentinfo.id
# join branchinfo ON branchinfo.id=studentinfo.Bid
# where year = 20172018 and branchinfo.Name = "ECE" group by sid order by Sum(marksinfo.marks) DESC"""


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)


