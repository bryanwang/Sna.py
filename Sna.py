from Crypto.Cipher import AES
from Crypto.Hash import HMAC
from base64 import b64encode
from hashlib import sha256
import codecs
from time import time

import requests
import json

URL = "https://feelinsonice-hrd.appspot.com/bq"
SECRET = b'iEk21fuwZApXlz93750dmW22pw389dPwOk'
STATIC_TOKEN = 'm198sOkJEn37DjqZ32lpRu76xmw288xSQ9'
HASH_PATTERN = '0001110111101110001111010101111011010001001110011000110001000110'
BLOB_KEY = 'M02cnQ51Ji97vwT4'

'''
ID: id
Snap ID: c_id
Media Type: m = 0 (pic), 1 (video)
Sent Snaps: sts
Opened: ts
Sender: sn
Recipient: rp
Send Type: st = 1 (sent to you), 2 (sent by you)
Time: t
Screenshot Count: c
'''

def login(usr, pwd):
    data = {'timestamp':timestamp(), 'req_token': req_token(STATIC_TOKEN), 'username':usr, 'password':pwd }
    req = requests.post("https://feelinsonice.appspot.com/ph/login", data)
    auth_token = json.loads(req.text)['auth_token']
    return req

# Returns data identical to the login request
def sync(usr, token):
    data = {'timestamp': timestamp(), 'req_token': req_token(token), 'json': '{}', 'username': usr}
    req = requests.post("https://feelinsonice.appspot.com/ph/sync", data)
    return req

def get_blob(usr, token, img_id):
    # Form URL and download encrypted "blob"
    blob_url = "https://feelinsonice.appspot.com/ph/blob?id={}".format(img_id)
    blob_url += "&username=" + usr + "&timestamp=" + str(timestamp()) + "&req_token=" + req_token(token)
    enc_blob = requests.get(blob_url).content
    # Save decrypted image
    img = open(img_id + '.jpg', 'wb')
    img.write(decrypt(enc_blob))
    img.close()
    print(decrypt(enc_blob))
    return decrypt(enc_blob)
    
def unread(usr, pwd):
    auth_token = json.loads(login(usr, pwd).text)['auth_token']
    feed = json.loads(sync(usr, auth_token).text)
    for snap in feed['snaps']:
        if 'rp' not in snap or 'm' in snap:
            if snap['m'] == 0 and snap['st'] == 1:
                get_blob(usr, auth_token, snap['id'])
            
def timestamp():
    return int(round(time() * 1000))

def req_token(token):
    return hash256(token, str(timestamp()))

def hash256(var1, var2):
    h1 = sha256(SECRET + var1.encode('utf-8')).hexdigest()
    h2 = sha256(var2.encode('utf-8') + SECRET).hexdigest()
    result = ''
    for i in range(0, len(h1)):
        result += h2[i] if HASH_PATTERN[i] is "1" else h1[i]
    return result

def pad(data, bs=16):
    pc = bs - len(data) % bs
    return data + (chr(pc) * pc).encode('utf-8')

def decrypt(data):
    cipher = AES.new(BLOB_KEY, AES.MODE_ECB)
    return cipher.decrypt(pad(data))

def encrypt(data):
    cipher = AES.new(BLOB_KEY, AES.MODE_ECB)
    return cipher.encrypt(data)

feed = json.loads(login('itsdagraham', 'ShiGeLian16').text)
print(req_token(feed['auth_token']))
print(timestamp())
