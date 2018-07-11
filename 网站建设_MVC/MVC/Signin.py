from flask import Flask, request, render_template
import mysql.connector
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('Home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('signin.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    conn = mysql.connector.connect(user='root', password='123456', database='test')
    # 运行查询:
    cursor = conn.cursor()
    cursor.execute('select users.username from users where username = %s', (username,))
    values1 = cursor.fetchall()
    cursor.execute('select users.password from users where password = %s', (password,))
    values2 = cursor.fetchall()
    # 关闭Cursor和Connection:
    cursor.close()
    conn.close()
    if values1 !=[] and values2 !=[]:
        return render_template('Index.html', username=username)
    return render_template('Signin.html', message='用户不存在或密码不对', username=username)

if __name__ == '__main__':
    app.run()
