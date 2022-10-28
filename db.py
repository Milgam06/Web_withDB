import pymysql


# milgamDB connect
milgam_db = pymysql.connect(
    user = "root",
    password = "12345678",
    host = "127.0.0.1",
    db = "milgamDB",
    charset = "utf8mb4"
)


# make cursor what selecting SQL objects
cursor = milgam_db.cursor()


# data lookup & start running SQL
sql = "SELECT * FROM mandarinDB;"
cursor.execute(sql)
result = cursor.fetchall()
print(*result)