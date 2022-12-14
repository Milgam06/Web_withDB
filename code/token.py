import jwt


userID = str(input("Username: ")) 
token = jwt.encode({"user_id": userID},)
