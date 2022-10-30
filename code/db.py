import pymysql
import pandas
import json
import jwt

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



sql = '''INSERT INTO mandarinDB (id, name, email)
    Value ('3', ');'''