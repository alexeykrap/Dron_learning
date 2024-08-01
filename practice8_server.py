import jwt
import datetime

SECRET_KEY = 'mySUPERsecretKEY-123'


def generate_token(object_id):
    payload = {
        'object_id': object_id,
        'exp': datetime.datetime.now(tz=datetime.UTC) + datetime.timedelta(seconds=5)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token


def get_token(object_id):
    if object_id:
        token = generate_token(object_id)
        print(token)
        return token
    return None
