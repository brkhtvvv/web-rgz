from flask import Flask, request, render_template, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
import psycopg2
from psycopg2.extras import RealDictCursor
import os

print('kkkkkkkkkkkkkkkkkkkkkkkkkkk')
# Настройка приложения Flask
app = Flask(__name__)
app.secret_key = 'секретно-секретный секрет'  # Замените на свой секретный ключ

# Путь для загрузки аватарок
UPLOAD_FOLDER = 'static/avatars'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# # Функция подключения к базе данных
# def db_connect():
#     conn = psycopg2.connect(
#         host='127.0.0.1',
#         database='olga_barkhatova_knowledge_bace',
#         user='olga_barkhatova_knowledge_bace',  # Укажите ваше имя пользователя БД
#         password='123'  # Укажите ваш пароль
#     )
#     cur = conn.cursor(cursor_factory=RealDictCursor)
#     return conn, cur

# # Главная страница
# @app.route('/')
# def index():
#     conn, cur = db_connect()
#     cur.execute("""
#         SELECT ads.id, ads.title, ads.content, users.fullname AS author
#         FROM ads
#         JOIN users ON ads.user_id = users.id
#     """)
#     ads = cur.fetchall()
#     conn.close()
#     return render_template('index.html', ads=ads, logged_in='user_id' in session)

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
#             return redirect(url_for('index'))
#         else:
#             flash('Неправильный логин или пароль.', 'error')

#     return render_template('login.html')

# # Выход из системы
# @app.route('/logout')
# def logout():
#     session.clear()
#     flash('Вы вышли из системы.', 'success')
#     return redirect(url_for('index'))

if __name__ == '__main__':
    app.debug = True
    app.run()
