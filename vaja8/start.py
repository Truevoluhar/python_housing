import pymysql

db_config = {
    'host': '34.89.130.215',
    'user': 'magdbuser',
    'password': 'Kjesijaro1',
    'database': 'python_housing',
    'port': 3306,
    'cursorclass': pymysql.cursors.DictCursor
}

def create_database():
    try:
        connection = pymysql.connect(**db_config)
        with connection.cursor() as cursor:
            guest_name = "Jon"
            guest_address = "Log"
            sql = "INSERT INTO guests (guest_name, guest_address) VALUES (%s, %s)"
            values = (guest_name, guest_address)
            cursor.execute(sql, values)
            connection.commit()

    except pymysql.MySQLError as e:
        print(e)
    finally:
        if "connection" in locals() and connection.open:
            connection.close()
            print("connection closed")

create_database()