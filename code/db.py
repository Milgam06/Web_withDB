import pymysql
import pandas
import json
import jwt
from time import sleep


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
    

# milgamDB connect
milgamDB = pymysql.connect(
    user = "root",
    password = "12345678",
    host = "127.0.0.1",
    db = "milgam_db",
    charset = "utf8mb4"
)


# make cursor what selecting SQL objects
cursor = milgamDB.cursor()



# data lookup & start running SQL
sql = "SELECT * FROM mandarinDB;"
cursor.execute(sql)
result = cursor.fetchall()


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

    
    
