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

# # from flask import Flask, request, render_template, redirect, url_for, session, flash
# # from werkzeug.security import generate_password_hash, check_password_hash
# # import psycopg2
# # from psycopg2.extras import RealDictCursor
# # import os

# # # Настройка приложения Flask
# # app = Flask(__name__)
# # app.secret_key = 'секретно-секретный секрет'  # Замените на свой секретный ключ

# # # Путь для загрузки аватарок
# # UPLOAD_FOLDER = 'static/avatars'
# # os.makedirs(UPLOAD_FOLDER, exist_ok=True)
# # app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# # # Функция подключения к базе данных
# # def db_connect():
# #     try:
# #         conn = psycopg2.connect(
# #             host='127.0.0.1',
# #             database='olga_barkhatova_knowledge_bace',
# #             user='olga_barkhatova_knowledge_bace',
# #             password='123'
# #         )
# #         cur = conn.cursor(cursor_factory=RealDictCursor)
# #         flash('connected')
# #         return conn, cur
# #     except Exception as e:
# #         print(f"Ошибка подключения к базе данных: {e}")
# #         return None, None

# # def db_close(conn, cur):
# #     conn.commit()
# #     cur.close()
# #     conn.close()


# # # Главная страница перенаправляет на страницу входа
# # @app.route("/")
# # def index():
# #     return redirect(url_for('login'))

# # # Страница регистрации
# # @app.route('/register', methods=['GET', 'POST'])
# # def register():
# #     if request.method == 'POST':
# #         login = request.form['login']
# #         password = request.form['password']
# #         fullname = request.form['fullname']
# #         email = request.form['email']
# #         about = request.form.get('about', '')
# #         avatar = request.files.get('avatar')

# #         # Проверка на заполненность полей
# #         if not (login and password and fullname and email):
# #             flash('Пожалуйста, заполните все обязательные поля.', 'error')
# #             return redirect(url_for('register'))

# #         # Обработка аватарки
# #         avatar_filename = None
# #         if avatar and avatar.filename:
# #             avatar_filename = os.path.join(app.config['UPLOAD_FOLDER'], avatar.filename)
# #             avatar.save(avatar_filename)

# #         # Хеширование пароля
# #         hashed_password = generate_password_hash(password)

# #         # Вставка данных в БД
# #         conn, cur = db_connect()
# #         try:
# #             cur.execute("""
# #                 INSERT INTO users (login, password, fullname, email, about, avatar)
# #                 VALUES (%s, %s, %s, %s, %s, %s)
# #             """, (login, hashed_password, fullname, email, about, avatar_filename))
# #             conn.commit()
# #             flash('Регистрация прошла успешно!', 'success')
# #             return redirect(url_for('login'))
# #         except psycopg2.Error as e:
# #             flash(f'Ошибка регистрации: {e.pgerror}', 'error')
# #             return redirect(url_for('register'))
# #         finally:
# #             conn.close()

# #     return render_template('register.html')

# # # Страница авторизации
# # @app.route('/login', methods=['GET', 'POST'])
# # def login():
# #     if request.method == 'POST':
# #         login = request.form['login']
# #         password = request.form['password']

# #         # Проверка заполненности полей
# #         if not (login and password):
# #             flash('Заполните все поля.', 'error')
# #             return redirect(url_for('login'))

# #         # Проверка пользователя в базе данных
# #         conn, cur = db_connect()
# #         cur.execute("SELECT * FROM users WHERE login = %s;", (login,))
# #         user = cur.fetchone()
# #         conn.close()

# #         if user and check_password_hash(user['password'], password):
# #             session['user_id'] = user['id']
# #             session['fullname'] = user['fullname']
# #             flash('Вы успешно вошли в систему!', 'success')
# #             return redirect(url_for('profile'))
# #         else:
# #             flash('Неправильный логин или пароль.', 'error')

# #     return render_template('login.html')

# # # Страница профиля пользователя
# # @app.route('/profile')
# # def profile():
# #     if 'user_id' not in session:
# #         flash('Сначала войдите в систему.', 'error')
# #         return redirect(url_for('login'))

# #     return f"""
# # <!DOCTYPE html>
# # <html lang="ru">
# # <head>
# #     <title>Профиль пользователя</title>
# # </head>
# # <body>
# #     <h1>Добро пожаловать, {session['fullname']}!</h1>
# #     <p>Это ваша страница профиля.</p>
# #     <a href="{url_for('logout')}">Выйти из системы</a>
# # </body>
# # </html>
# # """

# # # Выход из системы
# # @app.route('/logout')
# # def logout():
# #     session.clear()
# #     flash('Вы вышли из системы.', 'success')
# #     return redirect(url_for('login'))

# # # Обработчики ошибок
# # @app.errorhandler(404)
# # def not_found_404(err):
# #     return '''
# # <!doctype html>
# # <html>
# #     <head>
# #         <title>Ошибка 404</title>
# #     </head>
# #     <body>
# #         <h2>Ошибка 404 - такой страницы не существует</h2>
# #     </body>
# # </html>
# # '''

# # @app.errorhandler(500)
# # def not_found_500(err):
# #     return '''
# # <!doctype html>
# # <html>
# #     <head>
# #         <title>Ошибка 500</title>
# #     </head>
# #     <body>
# #         <h2>Ошибка 500 - сервер не смог обработать запрос</h2>
# #     </body>
# # </html>
# # '''

# # if __name__ == '__main__':
# #     app.debug = True
# #     app.run()


# from flask import Flask, request, jsonify
# from werkzeug.security import generate_password_hash, check_password_hash
# from jsonrpcserver import method, serve, Success, Error
# import psycopg2
# from psycopg2.extras import RealDictCursor
# # import jwt # type: ignore
# import datetime

# app = Flask(__name__)
# app.secret_key = 'super_secret_key'

# # # JWT секретный ключ
# # JWT_SECRET = 'jwt_secret_key'

# # Подключение к базе данных
# def db_connect():
#     conn = psycopg2.connect(
#         host='127.0.0.1',
#         database='olga_barkhatova_knowledge_bace',
#         user='postgres',
#         password='password'
#     )
#     cur = conn.cursor(cursor_factory=RealDictCursor)
#     return conn, cur

# def db_close(conn, cur):
#     conn.commit()
#     cur.close()
#     conn.close()

# # # Генерация JWT токена
# # def generate_token(user_id, is_admin):
# #     payload = {
# #         'user_id': user_id,
# #         'is_admin': is_admin,
# #         'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=2)
# #     }
# #     return jwt.encode(payload, JWT_SECRET, algorithm='HS256')

# # # Декодирование JWT токена
# # def decode_token(token):
# #     try:
# #         payload = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
# #         return payload
# #     except jwt.ExpiredSignatureError:
# #         return None
# #     except jwt.InvalidTokenError:
# #         return None

# # Регистрация пользователя
# @method
# def register(login: str, password: str, fullname: str, avatar: str, email: str, about: str = None):
#     if not (login and password and fullname and email):
#         return Error('Заполните обязательные поля')

#     conn, cur = db_connect()
#     cur.execute("SELECT id FROM users WHERE login=%s OR email=%s;", (login, email))
#     if cur.fetchone():
#         db_close(conn, cur)
#         return Error('Пользователь с таким логином или email уже существует')

#     password_hash = generate_password_hash(password)
#     cur.execute("INSERT INTO users (login, password, fullname, avatar, email, about) VALUES (%s, %s, %s, %s, %s, %s);",
#                 (login, password_hash, fullname, avatar, email, about))
#     db_close(conn, cur)
#     return Success('Пользователь успешно зарегистрирован')

# # Авторизация пользователя
# @method
# def login(login: str, password: str):
#     conn, cur = db_connect()
#     cur.execute("SELECT * FROM users WHERE login=%s;", (login,))
#     user = cur.fetchone()
#     db_close(conn, cur)

#     if not user or not check_password_hash(user['password'], password):
#         return Error('Неверный логин или пароль')

#     token = generate_token(user['id'], False)
#     return Success({'token': token})

# # Создание объявления
# @method
# def create_ad(token: str, title: str, content: str):
#     user = decode_token(token)
#     if not user:
#         return Error('Неавторизованный пользователь')


from flask import Flask, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
from jsonrpcserver import method, serve, Success, Error
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)
app.secret_key = 'super_secret_key'

# Подключение к базе данных
def db_connect():
    conn = psycopg2.connect(
        host='127.0.0.1',
        database='olga_barkhatova_knowledge_bace',
        user='olga_barkhatova_knowledge_bace',
        password='123'
    )
    cur = conn.cursor(cursor_factory=RealDictCursor)
    return conn, cur

def db_close(conn, cur):
    conn.commit()
    cur.close()
    conn.close()

# Регистрация пользователя
@method
def register(login: str, password: str, fullname: str, avatar: str, email: str, about: str = None):
    if not (login and password and fullname and email):
        return Error('Заполните обязательные поля')

    conn, cur = db_connect()
    cur.execute("SELECT id FROM users WHERE login=%s OR email=%s;", (login, email))
    if cur.fetchone():
        db_close(conn, cur)
        return Error('Пользователь с таким логином или email уже существует')

    password_hash = generate_password_hash(password)
    cur.execute("INSERT INTO users (login, password, fullname, avatar, email, about) VALUES (%s, %s, %s, %s, %s, %s);",
                (login, password_hash, fullname, avatar, email, about))
    db_close(conn, cur)
    return Success('Пользователь успешно зарегистрирован')

# Авторизация пользователя
@method
def login(login: str, password: str):
    conn, cur = db_connect()
    cur.execute("SELECT * FROM users WHERE login=%s;", (login,))
    user = cur.fetchone()
    db_close(conn, cur)

    if not user or not check_password_hash(user['password'], password):
        return Error('Неверный логин или пароль')

    session['user_id'] = user['id']
    session['is_admin'] = False
    return Success('Пользователь успешно авторизован')

# Создание объявления
@method
def create_ad(title: str, content: str):
    if 'user_id' not in session:
        return Error('Неавторизованный пользователь')

    conn, cur = db_connect()
    cur.execute("INSERT INTO ads (title, content, user_id) VALUES (%s, %s, %s);", (title, content, session['user_id']))
    db_close(conn, cur)
    return Success('Объявление успешно создано')

# Получение списка объявлений
@method
def list_ads():
    conn, cur = db_connect()
    cur.execute("""
        SELECT ads.id, ads.title, ads.content, users.fullname, users.email
        FROM ads
        JOIN users ON ads.user_id = users.id;
    """)
    ads = cur.fetchall()
    db_close(conn, cur)

    # Если пользователь не авторизован, скрываем email
    if 'user_id' not in session:
        for ad in ads:
            ad['email'] = 'Скрыт'

    return Success(ads)

# Редактирование объявления
@method
def edit_ad(ad_id: int, title: str, content: str):
    if 'user_id' not in session:
        return Error('Неавторизованный пользователь')

    conn, cur = db_connect()
    cur.execute("UPDATE ads SET title=%s, content=%s WHERE id=%s AND user_id=%s;",
                (title, content, ad_id, session['user_id']))
    db_close(conn, cur)
    return Success('Объявление успешно отредактировано')

# Удаление объявления
@method
def delete_ad(ad_id: int):
    if 'user_id' not in session:
        return Error('Неавторизованный пользователь')

    conn, cur = db_connect()
    cur.execute("DELETE FROM ads WHERE id=%s AND user_id=%s;", (ad_id, session['user_id']))
    db_close(conn, cur)
    return Success('Объявление удалено')

# Администратор: удаление пользователя
@method
def admin_delete_user(user_id: int):
    if 'user_id' not in session or not session.get('is_admin'):
        return Error('Доступ запрещен')

    conn, cur = db_connect()
    cur.execute("DELETE FROM users WHERE id=%s;", (user_id,))
    db_close(conn, cur)
    return Success('Пользователь удален администратором')

# Точка входа для JSON-RPC
@app.route('/api', methods=['POST'])
def api():
    return jsonify(serve(request.get_json()))

if __name__ == '__main__':
    app.run(debug=True)
