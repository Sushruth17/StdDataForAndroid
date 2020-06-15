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
    # data = {k.lower(): v for k, v in data.items()}
    newData = []
    for i in data:
        newData.append({k.lower(): v for k, v in i.items()})
    print("new--->",newData)
    return render_template('index.html',value=newData)


# @app.route("/studentinfo",methods=['GET','POST'])
# def showTable():
#     data = getData()
#     print("data====---------->", data)
#     return data


if __name__ == "__main__":
    app.run(host='127.0.0.1')