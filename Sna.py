from Crypto.Cipher import AES
import hashlib
import codecs
import time

import requests
import json

SECRET = 'iEk21fuwZApXlz93750dmW22pw389dPwOk'
STATIC_TOKEN = 'm198sOkJEn37DjqZ32lpRu76xmw288xSQ9'
HASH_PATTERN = '0001110111101110001111010101111011010001001110011000110001000110'
AUTH_TOKEN = ''

def login(usr, pwd):
    data = {'timestamp':timestamp(), 'req_token': req_token(STATIC_TOKEN, timestamp()), 'username':usr, 'password':pwd }
    req = requests.post("https://feelinsonice.appspot.com/ph/login", data)
    AUTH_TOKEN = json.loads(req.text)['auth_token']
    return req.text

def sync(usr):
    data = {'timestamp':timestamp(), 'req_token':req_token(AUTH_TOKEN, timestamp()), 'json': '{}', 'username':usr}
    req = requests.post("https://feelinsonice.appspot.com/ph/sync", data)
    return req.text

def timestamp():
    return int(round(time.time() * 1000))

def req_token(token, time):
    s1 = SECRET.encode('utf-8') + token.encode('utf-8')
    s2 = str(time).encode('utf-8') + SECRET.encode('utf-8')

    s3 = hashlib.sha256(s1).hexdigest()
    print('s3: ', s3)
    s4 = hashlib.sha256(s2).hexdigest()
    print('s4: ', s4)

    result = ''
    for i in range(0, len(s3)):
        result += s4[i] if HASH_PATTERN[i] is "1" else s3[i]
    return result

def auth_token(req):
    return json.loads(req)['auth_token']
