import api

api.connectDB("root", "12345678", "127.0.0.1", "milgam_db")
api.cursoring()
api.startSQL("mandarinDB")
# api.insertData("milgam", "milgamfruit@naver.com", "1234567890")
api.selectData("mandarinDB","name", "milgam")