import pymysql

db_config = {
    'host': '34.89.130.215',
    'user': 'magdbuser',
    'password': 'Kjesijaro1',
    'database': 'python_housing',
    'port': 3306,
    'cursorclass': pymysql.cursors.DictCursor
}

def read_all_students():
    try:
        connection = pymysql.connect(**db_config)
        with connection.cursor() as cursor:
            sql = "SELECT * FROM Students"
            cursor.execute(sql)
            results = cursor.fetchall()
            print(results)

    except pymysql.MySQLError as e:
        print(e)
    finally:
        if "connection" in locals() and connection.open:
            connection.close()
            print("connection closed")

def find_student(name):
    try:
        connection = pymysql.connect(**db_config)
        with connection.cursor() as cursor:
            sql = "SELECT * FROM Students WHERE name = %s"
            params = (name,)
            cursor.execute(sql, params)
            result = cursor.fetchone()
            print(result)
            if result == None:
                print("No student found")
    except pymysql.MySQLError as e:
        print(e)
    finally:
        if "connection" in locals() and connection.open:
            connection.close()
            print("connection closed")

def insert_student(name, age, grade):
    try:
        connection = pymysql.connect(**db_config)
        with connection.cursor() as cursor:
            sql = "INSERT INTO Students (name, age, grade) VALUES (%s, %s, %s)"
            params = (name, age, grade)
            cursor.execute(sql, params)
            connection.commit()
            inserted_id = cursor.lastrowid
            print("Student successfuly inserted, id: " + str(inserted_id))
    except pymysql.MySQLError as e:
        print(e)
    finally:
        if "connection" in locals() and connection.open:
            connection.close()
            print("connection closed")

def delete_student(id):
    try:
        connection = pymysql.connect(**db_config)
        with connection.cursor() as cursor:
            sql = "DELETE FROM Students where ID = %s"
            params = (id,)
            cursor.execute(sql, params)
            connection.commit()
            print(f"Deleted student with id = {id}")
    except pymysql.MySQLError as e:
        print(e)
    finally:
        if "connection" in locals() and connection.open:
            connection.close()
            print("connection closed")

insert_student("Miha", 64, "B+")
read_all_students()
find_student("Jon")