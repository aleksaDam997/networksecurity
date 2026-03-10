import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="inventory_managment_db"
    )


def get_users():
    conn = get_connection()

    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users")

        return cursor.fetchall()

    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    users = get_users()

    for user in users:
        print(user)