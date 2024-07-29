import jwt
import datetime

SECRET_KEY = 'MYkey-111'

def generate_token(user_id):
    payload = {
        'user_id': user_id,
        'exp': datetime.datetime.now(tz=datetime.UTC) + datetime.timedelta(seconds=5)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

def get_token(user_id):
    if user_id:
        token = generate_token(user_id)
        print(token)
        return token
    return None