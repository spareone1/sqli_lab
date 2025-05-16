import os
import mysql.connector
from flask import Flask, request, render_template

app = Flask(__name__)

def get_db():
    return mysql.connector.connect(
        host=os.environ.get("DB_HOST", "localhost"),
        user=os.environ.get("DB_USER", "root"),
        password=os.environ.get("DB_PASSWORD", "1234"),
        database=os.environ.get("DB_NAME", "sqli_lab")
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    message = None
    if request.method == 'POST':
        username = request.form['userid']
        password = request.form['userpw']
        try:
            conn = get_db()
            cursor = conn.cursor(dictionary=True)
            query = f"SELECT * FROM users WHERE userid = '{username}' AND userpw = '{password}'"
            cursor.execute(query)
            user = cursor.fetchone()
            message = '로그인 성공' if user else '로그인 실패'
        except mysql.connector.Error as err:
            message = f"MySQL 에러: {err}"
        except Exception as e:
            message = f"예외 발생: {str(e)}"
        finally:
            try:
                cursor.close()
                conn.close()
            except:
                pass
    return render_template('login.html', message=message)

@app.route('/board', methods=['GET'])
def board():
    keyword = request.args.get('q', '')
    results = []
    error = None
    try:
        conn = get_db()
        cursor = conn.cursor(dictionary=True)
        if keyword:
            # ❗ SQL Injection 실습을 위해 쿼리에 직접 삽입
            query = f"SELECT title, content, author FROM posts WHERE title LIKE '%{keyword}%'"
        else:
            query = "SELECT title, content, author FROM posts"
        cursor.execute(query)
        results = cursor.fetchall()
    except Exception as e:
        error = str(e)
    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass
    return render_template('board.html', results=results, error=error)

@app.route('/find', methods=['GET'])
def find():
    result = None
    userid = request.args.get('userid')
    if userid:
        try:
            conn = get_db()
            cursor = conn.cursor(dictionary=True)
            query = f"SELECT * FROM users WHERE userid = '{userid}'"
            cursor.execute(query)
            user = cursor.fetchone()
            result = "사용자 존재" if user else "존재하지 않음"
        except Exception as e:
            result = f"에러 발생: {str(e)}"
        finally:
            try:
                cursor.close()
                conn.close()
            except:
                pass
    return render_template('find.html', result=result)

@app.route('/find/payload')
def payload():
    return render_template('payload.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
