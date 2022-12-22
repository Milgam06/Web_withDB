import jwt

secretKey = "fpdlsqhdntlrtm"

userID = str(input("Username: ")) 
token = jwt.encode({"user_id": userID},secretKey, "HS256")
