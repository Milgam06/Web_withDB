from tkinter.font import names
import pymysql
import pandas
import json
import jwt


name = ""
email = ""
num = ""

def information():
    global name, email, num
    print("If you finish to put your information, You can no longer change it.")
    name = str("Name: ")
    email = str("Email: ")
    num = str("Number (No hyphen): ")
    

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


# # transform to dataframe
result = pandas.DataFrame(result)
print(result)


def plusData():
    sql = f'''INSERT INTO mandarinDB (id, name, email, num, token)
        Value ('0001', '{name}', '{email}', '{num}', 'afdafafsfdfasafefasewq23');'''
    cursor.execute(sql)
    milgamDB.commit()
    
    
    

