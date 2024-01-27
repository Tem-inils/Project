import sqlite3

connection = sqlite3.connect('mydatabase.db')
sqlite = connection.cursor()
sqlite.execute(
    'CREATE TABLE IF NOT EXISTS users (user_id INTEGER, name TEXT, age INTEGER, phone_number TEXT, location TEXT);')
sqlite.close()
connection.close()


# Checker Users [SELECT]
def check_users(user_id: int) -> [tuple, None]:
    conect = sqlite3.connect('mydatabase.db')
    sql_lite = conect.cursor()

    user = sql_lite.execute('SELECT * FROM users WHERE user_id = ?;', (user_id,)).fetchone()

    return user


# Register Users [INSERT]
def register_users(user_id: int, name: str, age: int, phn: str, location: str) -> [bool, None]:
    conect = sqlite3.connect('mydatabase.db')
    sql_lite = conect.cursor()

    try:
        sql_lite.execute('INSERT INTO users (user_id, name, age, phone_number, location) VALUES (?,?,?,?,?);',
                         (user_id, name, age, phn, location))

        conect.commit()
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        conect.close()
