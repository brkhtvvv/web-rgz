# # from flask import Flask, request, render_template, redirect, url_for, session, flash
# # from werkzeug.security import generate_password_hash, check_password_hash
# # import psycopg2
# # from psycopg2.extras import RealDictCursor
# # import os

# # # Настройка приложения Flask
# # app = Flask(__name__)
# # app.secret_key = 'секретно-секретный секрет'  # Замените на свой секретный ключ
# # app.config['DB_TYPE'] = os.getenv('DB_TYPE', 'postgres')

# # # del
# # @app.route("/")
# # @app.route("/index")
# # def start():
# #     return redirect("/menu", code=302)

# # @app.route("/menu")
# # def menu():
# #     return """
# # <!DOCTYPE html>
# # <html lang="ru">
# # <head>
# #     <title>НГТУ ФБ, Лабораторные работы</title>
# # </head>
# # <body>
# #     <header>
# #         НГТУ ФБ, WEB-программирование, часть 2. Список лабораторных  
# #     </header>

# #     <h1>web-сервер на flask</h1>
# #     <li><a href="http://127.0.0.1:5000/lab1">Первая лабораторная</a></li>
# #     <li><a href="http://127.0.0.1:5000/lab2">Вторая лабораторная</a></li>
# #     <li><a href="http://127.0.0.1:5000/lab3">Третья лабораторная</a></li>
# #     <li><a href="http://127.0.0.1:5000/lab4">Четвертая лабораторная</a></li>
# #     <li><a href="http://127.0.0.1:5000/lab5">Пятая лабораторная</a></li>  
# #     <li><a href="http://127.0.0.1:5000/lab6">Шестая лабораторная</a></li> 
# #     <li><a href="http://127.0.0.1:5000/lab7">Седьмая лабораторная</a></li> 
# #     <footer>
# #         &copy: Бархатова Ольга, ФБИ-24, 3 курс, 2024
# #     </footer>
# # </body>
# # </html>
# # """

# # @app.errorhandler(404)
# # def not_found_404(err):
# #     return '''
# # <!doctype html>
# # <html>
# #     <head>
# #         <title>НГТУ, ФБ, Лабораторные работы</title>
# #         <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
# #     </head>
# #     <body>
# #         <header>
# #             НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
# #         </header>
# #         <h2>Ошибка 404 - такой страницы не существует</h2>
# #         <footer>
# #             &copy; Бархатова Ольга, ФБИ-24, 3 курс, 2024
# #         </footer>
# #     </body>
# # </html>
# # '''


# # @app.errorhandler(500)
# # def not_found_500(err):
# #     return '''
# # <!doctype html>
# # <html>
# #     <head>
# #         <title>НГТУ, ФБ, Лабораторные работы</title>
# #         <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
# #     </head>
# #     <body>
# #         <header>
# #             НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
# #         </header>
# #         <h2>Ошибка 500 - сервер не смог обработать запрос</h2>
# #         <footer>
# #             &copy; Бархатова Ольга, ФБИ-24, 3 курс, 2024
# #         </footer>
# #     </body>
# # </html>
# # '''

# # # del 

# # # # Путь для загрузки аватарок
# # # UPLOAD_FOLDER = 'static/avatars'
# # # os.makedirs(UPLOAD_FOLDER, exist_ok=True)
# # # app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# # # def db_connect():
# # #     if current_app.config['DB_TYPE'] == 'postgres':
# # #         conn = psycopg2.connect (
# # #             host = '127.0.0.1',
# # #             database = 'olya_barkhatova_knowledge_base',
# # #             user = 'olya_barkhatova_knowledge_base',
# # #             password = '123'
# # #     )
# # #         cur = conn.cursor(cursor_factory=RealDictCursor)
# # #     else:
# # #         dir_path = path.dirname(path.realpath(__file__))
# # #         db_path = path.join(dir_path, "database.db")
# # #         conn = sqlite3.connect(db_path)
# # #         conn.row_factory = sqlite3.Row
# # #         cur = conn.cursor*()


# # #     return conn, cur

# # # def db_close(conn, cur):
# # #     conn.commit()
# # #     cur.close()
# # #     conn.close()
# # # # Функция подключения к базе данных
# # # def db_connect():
# # #     conn = psycopg2.connect(
# # #         host='127.0.0.1',
# # #         database='olga_barkhatova_knowledge_bace',
# # #         user='olga_barkhatova_knowledge_bace',  # Укажите ваше имя пользователя БД
# # #         password='123'  # Укажите ваш пароль
# # #     )
# # #     cur = conn.cursor(cursor_factory=RealDictCursor)
# # #     return conn, cur

# # # # Главная страница
# # # @app.route('/')
# # # def index():
# # #     conn, cur = db_connect()
# # #     cur.execute("""
# # #         SELECT ads.id, ads.title, ads.content, users.fullname AS author
# # #         FROM ads
# # #         JOIN users ON ads.user_id = users.id
# # #     """)
# # #     ads = cur.fetchall()
# # #     conn.close()
# # #     return render_template('index.html', ads=ads, logged_in='user_id' in session)

# # # # Страница регистрации
# # # @app.route('/register', methods=['GET', 'POST'])
# # # def register():
# # #     if request.method == 'POST':
# # #         login = request.form['login']
# # #         password = request.form['password']
# # #         fullname = request.form['fullname']
# # #         email = request.form['email']
# # #         about = request.form.get('about', '')
# # #         avatar = request.files.get('avatar')

# # #         # Проверка на заполненность полей
# # #         if not (login and password and fullname and email):
# # #             flash('Пожалуйста, заполните все обязательные поля.', 'error')
# # #             return redirect(url_for('register'))

# # #         # Обработка аватарки
# # #         avatar_filename = None
# # #         if avatar and avatar.filename:
# # #             avatar_filename = os.path.join(app.config['UPLOAD_FOLDER'], avatar.filename)
# # #             avatar.save(avatar_filename)

# # #         # Хеширование пароля
# # #         hashed_password = generate_password_hash(password)

# # #         # Вставка данных в БД
# # #         conn, cur = db_connect()
# # #         try:
# # #             cur.execute("""
# # #                 INSERT INTO users (login, password, fullname, email, about, avatar)
# # #                 VALUES (%s, %s, %s, %s, %s, %s)
# # #             """, (login, hashed_password, fullname, email, about, avatar_filename))
# # #             conn.commit()
# # #             flash('Регистрация прошла успешно!', 'success')
# # #             return redirect(url_for('login'))
# # #         except psycopg2.Error as e:
# # #             flash(f'Ошибка регистрации: {e.pgerror}', 'error')
# # #             return redirect(url_for('register'))
# # #         finally:
# # #             conn.close()

# # #     return render_template('register.html')

# # # # Страница авторизации
# # # @app.route('/login', methods=['GET', 'POST'])
# # # def login():
# # #     if request.method == 'POST':
# # #         login = request.form['login']
# # #         password = request.form['password']

# # #         # Проверка заполненности полей
# # #         if not (login and password):
# # #             flash('Заполните все поля.', 'error')
# # #             return redirect(url_for('login'))

# # #         # Проверка пользователя в базе данных
# # #         conn, cur = db_connect()
# # #         cur.execute("SELECT * FROM users WHERE login = %s;", (login,))
# # #         user = cur.fetchone()
# # #         conn.close()

# # #         if user and check_password_hash(user['password'], password):
# # #             session['user_id'] = user['id']
# # #             session['fullname'] = user['fullname']
# # #             flash('Вы успешно вошли в систему!', 'success')
# # #             return redirect(url_for('index'))
# # #         else:
# # #             flash('Неправильный логин или пароль.', 'error')

# # #     return render_template('login.html')

# # # # Выход из системы
# # # @app.route('/logout')
# # # def logout():
# # #     session.clear()
# # #     flash('Вы вышли из системы.', 'success')
# # #     return redirect(url_for('index'))

# # # if __name__ == '__main__':
# # #     app.debug = True
# # #     app.run()

# from flask import Flask, request, render_template, redirect, url_for, session, flash
# from werkzeug.security import generate_password_hash, check_password_hash
# import psycopg2
# from psycopg2.extras import RealDictCursor
# import os

# # Настройка приложения Flask
# app = Flask(__name__)
# app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'секретно-секретный секрет')
# app.config['DB_TYPE'] = os.getenv('DB_TYPE', 'postgres')
# # Путь для загрузки аватарок
# UPLOAD_FOLDER = 'static/avatars'
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



# # Функция подключения к базе данных
# def db_connect():
#     try:
#         conn = psycopg2.connect(
#             host='127.0.0.1',
#             database='olga_barkhatova_knowledge_bace',
#             user='olga_barkhatova_knowledge_bace',
#             password='123'
#         )
#         cur = conn.cursor(cursor_factory=RealDictCursor)

#         return conn, cur
#     except Exception as e:
#         print(f"Ошибка подключения к базе данных: {e}")
#         return None, None

# def db_close(conn, cur):
#     conn.commit()
#     cur.close()
#     conn.close()


# # Главная страница перенаправляет на страницу входа
# @app.route("/")
# def index():
#     return redirect(url_for('login'))

# # Страница регистрации
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         login = request.form['login']
#         password = request.form['password']
#         fullname = request.form['fullname']
#         email = request.form['email']
#         about = request.form.get('about', '')
#         avatar = request.files.get('avatar')

#         # Проверка на заполненность полей
#         if not (login and password and fullname and email):
#             flash('Пожалуйста, заполните все обязательные поля.', 'error')
#             return redirect(url_for('register'))

#         # Обработка аватарки
#         avatar_filename = None
#         if avatar and avatar.filename:
#             avatar_filename = os.path.join(app.config['UPLOAD_FOLDER'], avatar.filename)
#             avatar.save(avatar_filename)

#         # Хеширование пароля
#         hashed_password = generate_password_hash(password)

#         # Вставка данных в БД
#         conn, cur = db_connect()
#         try:
#             cur.execute("""
#                 INSERT INTO users (login, password, fullname, email, about, avatar)
#                 VALUES (%s, %s, %s, %s, %s, %s)
#             """, (login, hashed_password, fullname, email, about, avatar_filename))
#             conn.commit()
#             flash('Регистрация прошла успешно!', 'success')
#             return redirect(url_for('login'))
#         except psycopg2.Error as e:
#             flash(f'Ошибка регистрации: {e.pgerror}', 'error')
#             return redirect(url_for('register'))
#         finally:
#             conn.close()

#     return render_template('register.html')

# # Страница авторизации
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         login = request.form['login']
#         password = request.form['password']

#         # Проверка заполненности полей
#         if not (login and password):
#             flash('Заполните все поля.', 'error')
#             return redirect(url_for('login'))

#         # Проверка пользователя в базе данных
#         conn, cur = db_connect()
#         cur.execute("SELECT * FROM users WHERE login = %s;", (login,))
#         user = cur.fetchone()
#         conn.close()

#         if user and check_password_hash(user['password'], password):
#             session['user_id'] = user['id']
#             session['fullname'] = user['fullname']
#             flash('Вы успешно вошли в систему!', 'success')
#             return redirect(url_for('profile'))
#         else:
#             flash('Неправильный логин или пароль.', 'error')

#     return render_template('login.html')

# # Страница профиля пользователя
# @app.route('/profile')
# def profile():
#     if 'user_id' not in session:
#         flash('Сначала войдите в систему.', 'error')
#         return redirect(url_for('login'))

#     return f"""
# <!DOCTYPE html>
# <html lang="ru">
# <head>
#     <title>Профиль пользователя</title>
# </head>
# <body>
#     <h1>Добро пожаловать, {session['fullname']}!</h1>
#     <p>Это ваша страница профиля.</p>
#     <a href="{url_for('logout')}">Выйти из системы</a>
# </body>
# </html>
# """

# # Выход из системы
# @app.route('/logout')
# def logout():
#     session.clear()
#     flash('Вы вышли из системы.', 'success')
#     return redirect(url_for('login'))

# # Обработчики ошибок
# @app.errorhandler(404)
# def not_found_404(err):
#     return '''
# <!doctype html>
# <html>
#     <head>
#         <title>Ошибка 404</title>
#     </head>
#     <body>
#         <h2>Ошибка 404 - такой страницы не существует</h2>
#     </body>
# </html>
# '''

# @app.errorhandler(500)
# def not_found_500(err):
#     return '''
# <!doctype html>
# <html>
#     <head>
#         <title>Ошибка 500</title>
#     </head>
#     <body>
#         <h2>Ошибка 500 - сервер не смог обработать запрос</h2>
#     </body>
# </html>
# '''

# if __name__ == '__main__':
#     app.debug = True
#     app.run()

from flask import Flask, request, render_template, redirect, url_for, session, flash, jsonify, current_app
from werkzeug.security import generate_password_hash, check_password_hash
import psycopg2
import sqlite3
from psycopg2.extras import RealDictCursor
import os
from os import path

# Настройка приложения Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'секретно-секретный секрет')
app.config['DB_TYPE'] = os.getenv('DB_TYPE', 'postgres')
# Путь для загрузки аватарок
UPLOAD_FOLDER = 'static/avatars'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Конфигурация базы данных
# app.config['DB_TYPE'] = 'postgres'  # Можно переключить на 'sqlite', если потребуется

# Функция подключения к базе данных
def db_connect():
    try:
        if app.config['DB_TYPE'] == 'postgres':
            conn = psycopg2.connect(
                host='127.0.0.1',
                database='olga_barkhatova_knowledge_bace',
                user='olga_barkhatova_knowledge_bace',
                password='123'
            )
            cur = conn.cursor(cursor_factory=RealDictCursor)
        else:
            dir_path = path.dirname(path.realpath(__file__))
            db_path = path.join(dir_path, "database.db")
            conn = sqlite3.connect(db_path)
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
        return conn, cur
    except Exception as e:
        print(f"Ошибка подключения к базе данных: {e}")
        return None, None

def db_close(conn, cur):
    if conn and cur:
        conn.commit()
        cur.close()
        conn.close()

# Главная страница
@app.route("/")
def index():
    return redirect(url_for('register'))

# Регистрация
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        login = request.form.get('login', '')
        password = request.form.get('password', '')
        fullname = request.form.get('fullname', '')
        email = request.form.get('email', '')
        about = request.form.get('about', '')
        avatar = request.files.get('avatar')

        errors = {}
        if not login:
            errors['login'] = 'Поле "Логин" обязательно.'
        if not password:
            errors['password'] = 'Поле "Пароль" обязательно.'
        if not fullname:
            errors['fullname'] = 'Поле "Имя" обязательно.'
        if errors:
            flash(errors, 'error')
            return render_template('register.html', errors=errors)

        # Обработка аватарки
        avatar_filename = None
        if avatar and avatar.filename:
            avatar_filename = os.path.join(app.config['UPLOAD_FOLDER'], avatar.filename)
            avatar.save(avatar_filename)

        hashed_password = generate_password_hash(password)

        # Проверка существующего пользователя и регистрация
        conn, cur = db_connect()
        try:
            if current_app.config['DB_TYPE'] == 'postgres':
                cur.execute("SELECT login FROM users WHERE login=%s;", (login,))
            else:
                cur.execute("SELECT login_user FROM users WHERE login_user=?;", (login, ))
            if cur.fetchone():
                flash('Такой пользователь уже существует.', 'error')
                return redirect(url_for('register'))
            if current_app.config['DB_TYPE'] == 'postgres':
                cur.execute("""
                    INSERT INTO users (login, password, fullname, email, about, avatar)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """, (login, hashed_password, fullname, email, about, avatar_filename))
            else:
                                cur.execute("""
                    INSERT INTO users (login, password, fullname, email, about, avatar)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (login, hashed_password, fullname, email, about, avatar_filename))
            conn.commit()
            flash('Регистрация прошла успешно!', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            print(f"Ошибка регистрации: {e}")
            flash('Ошибка при регистрации.', 'error')
        finally:
            db_close(conn, cur)

    return render_template('register.html')

# Авторизация
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form.get('login', '')
        password = request.form.get('password', '')

        if not login or not password:
            flash('Заполните все поля.', 'error')
            return redirect(url_for('login'))

        conn, cur = db_connect()
        try:
            if current_app.config['DB_TYPE'] == 'postgres':
                cur.execute("SELECT * FROM users WHERE login = %s;", (login,))
            else:
                cur.execute("SELECT * FROM users WHERE login_user=?;", (login,))
            user = cur.fetchone()
            if user and check_password_hash(user['password'], password):
                session['user_id'] = user['id']
                session['fullname'] = user['fullname']
                flash('Вы успешно вошли в систему!', 'success')
                return redirect(url_for('profile'))
            else:
                flash('Неправильный логин или пароль.', 'error')
        except Exception as e:
            print(f"Ошибка авторизации: {e}")
            flash('Ошибка при входе.', 'error')
        finally:
            db_close(conn, cur)

    return render_template('login.html')

# Профиль пользователя
@app.route('/profile')
def profile():
    if 'user_id' not in session:
        flash('Сначала войдите в систему.', 'error')
        return redirect(url_for('login'))
    return f"""
    <h1>Добро пожаловать, {session['fullname']}!</h1>
    <p>Это ваша страница профиля.</p>
    <a href="{url_for('logout')}">Выйти из системы</a>
    """

# Выход из системы
@app.route('/logout')
def logout():
    session.clear()
    flash('Вы вышли из системы.', 'success')
    return redirect(url_for('login'))

# Обработчики ошибок
@app.errorhandler(404)
def not_found_404(err):
    return '<h2>Ошибка 404 - такой страницы не существует</h2>', 404

@app.errorhandler(500)
def not_found_500(err):
    return '<h2>Ошибка 500 - сервер не смог обработать запрос</h2>', 500

if __name__ == '__main__':
    app.debug = True
    app.run()
