from flask import Flask, render_template
import pymysql

app = Flask(__name__)

conn = pymysql.connect(host='localhost',
                                     user='root',
                                     password='',
                                     charset='utf8mb4',
                                     db='studentdb',
                                     cursorclass=pymysql.cursors.DictCursor)
cursor = conn.cursor()
def getData():
    cursor.execute("select * from studentinfo")
    data = cursor.fetchall() #data from database
    return data


@app.route("/")
def main():
    data = getData()
    print("data====---------->", data)
    return render_template('index.html',value=data)


# @app.route("/studentinfo",methods=['GET','POST'])
# def showTable():
#     data = getData()
#     print("data====---------->", data)
#     return data


if __name__ == "__main__":
    app.run()