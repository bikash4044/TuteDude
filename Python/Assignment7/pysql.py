import psycopg2

def create_table():
    connect = psycopg2.connect(dbname="postgres", user="postgres", password="postgres", host="localhost", port="5432")
    print("connected")

    cursor = connect.cursor()
    cursor.execute('''create table employees(name text, id int, age int);''')

    connect.commit()
    connect.close()
    print("operation successful")

def insert_data():
    connect = psycopg2.connect(dbname="postgres", user="postgres", password="postgres", host="localhost", port="5432")
    print("connected")

    cursor = connect.cursor()
    cursor.execute('''insert into employees(name, id, age) values('Sam',01,30)''')

    connect.commit()
    connect.close()
    print("data adding successful")



def view_data():
    connect = psycopg2.connect(dbname="postgres", user="postgres", password="postgres", host="localhost", port="5432")
    print("connected")

    cursor = connect.cursor()
    cursor.execute('''select * from employees;''')
    show = cursor.fetchall()
    print(show)

    connect.commit()
    connect.close()
    print("data fetch successful")


def input_data():
    connect = psycopg2.connect(dbname="postgres", user="postgres", password="postgres", host="localhost", port="5432")
    print("connected")
    nm = input("Enter your name: ")
    id = input("Enter your ID: ")
    age = input("Enter your age: ")
    cursor = connect.cursor()
    cursor.execute(f'''insert into employees(name, id, age) values(%s,%s,%s)''',(nm,id,age))

    connect.commit()
    connect.close()
    print("data adding successful")
    view_data()

input_data()