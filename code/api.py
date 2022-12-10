import pymysql
import pandas
import jwt
from time import sleep

cursor = ""
result = ""
id = 1

# connect with database
def connectDB(users: str, passwords: str, hosts: str, dbName: str, charsets: str = "utf8mb4"):
    global connecting
    try:
        connecting = pymysql.connect(user = users, password = passwords, host = hosts, db = dbName, charset = charsets)
        return connecting
    except:
        if not isinstance(users, str) or not isinstance(passwords, str) or not isinstance(hosts, str) or not isinstance(dbName, str) or not isinstance(charsets, str):
            raise TypeError("Argument's type is wrong")


# make cursor what selecting SQL objects
def cursoring():    
    global cursor
    cursor = connecting.cursor()


# data lookup & start running SQL
def startSQL(tables: str):
    global table
    table = tables
    global result
    try:
        sql = f"SELECT * FROM {tables};"
        cursor.execute(sql)
        result = cursor.fetchall()
        print("Success connecting 😎")
    except:
        raise TypeError(f"Can't find the tables named {tables}")


# INSERT the information into the database
def insertData(name: str, email: str, num: str):
    global table
    global connecting
    global id
    try:
        id = result[-1][0]
    except IndexError:
        id = 0
    for _ in range(4):
        sleep(0.25)
        print(".", end="")
    sql = f'''INSERT INTO {table} (id, name, email, num, token)
        Value ('{id+1}', '{name}', '{email}', '{num}', 'token');'''
    cursor.execute(sql)
    connecting.commit()
    return print("Success to INSERT😎")

