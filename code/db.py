import pymysql
import pandas
import jwt
from time import sleep

connecting = ""
cursor = ""
result = ""


name = ""
email = ""
num = ""
id = 1

# input information
def information():
    global name, email, num
    print("If you finish to put your information, You can no longer change it.")
    name = str(input("Name: "))
    email = str(input("Email: "))
    num = str(input("Number (No hyphen): "))
    return name, email, num
    

# connect with database
def connectDB(users: str, passwords: str, hosts: str, dbName: str, charsets: str = "utf8mb4"):
    global connecting
    try:
        connecting = pymysql.connect(
            user = users,
            password = passwords,
            host = hosts,
            db = dbName,
            charset = charsets
        )
    except:
        if not isinstance(users, str) or not isinstance(passwords, str) or not isinstance(hosts, str) or not isinstance(dbName, str) or not isinstance(charsets, str):
            raise TypeError("Argument's type is wrong")


# make cursor what selecting SQL objects
def cursoring():    
    global cursor
    cursor = connecting.cursor()



# data lookup & start running SQL
def startSQL(tables: str):
    global result
    try:
        sql = f"SELECT * FROM {tables};"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except:
        raise TypeError


# INSERT the information into the database
def plusData():
    global id
    try:
        id = result[-1][0]
    except IndexError:
        id = 0
    for _ in range(4):
        sleep(0.25)
        print(".", end="")
    sql = f'''INSERT INTO mandarinDB (id, name, email, num, token)
        Value ('{id+1}', '{name}', '{email}', '{num}', 'token');'''
    cursor.execute(sql)
    milgamDB.commit()
    return print(" success😎")

    
    
