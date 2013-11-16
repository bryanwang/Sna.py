from Crypto.Cipher import AES
from hashlib import sha256
import time
import codecs
import requests
import json
from urllib import parse as urllib

import bottle
from bottle import route, run, request, post, static_file, template
import os

URL = "https://feelinsonice-hrd.appspot.com/bq"
SECRET = b'iEk21fuwZApXlz93750dmW22pw389dPwOk'
STATIC_TOKEN = 'm198sOkJEn37DjqZ32lpRu76xmw288xSQ9'
HASH_PATTERN = '0001110111101110001111010101111011010001001110011000110001000110'
BLOB_KEY = 'M02cnQ51Ji97vwT4'

def login(usr, pwd):
    data = {'timestamp':timestamp(),
            'req_token': req_token(STATIC_TOKEN),
            'username':usr,
            'password':pwd}
    req = requests.post("https://feelinsonice.appspot.com/ph/login", data)
    #auth_token = json.loads(req.text)['auth_token']
    return req

def signup(usr, pwd, email, birthday):
    # Register account
    token = req_token(STATIC_TOKEN)
    data = {'birthday': birthday,
            'email': email,
            'password': pwd,
            'req_token': token,
            'time_zone': 'America/Chicago',
            'timestamp': str(timestamp())}
    req = requests.post('https://feelinsonice-hrd.appspot.com/bq/register', data)
    # Complete registration and claim username if not taken
    data2 = {'email': email,
             'req_token': req_token(STATIC_TOKEN),
             'timestamp': timestamp(),
             'username': usr}
    req2 = requests.post('https://feelinsonice-hrd.appspot.com/bq/registeru', data2)
    return req2

# Returns data identical to the login request
def sync(usr, token):
    data = {'timestamp': timestamp(), 'req_token': req_token(token), 'json': '{}', 'username': usr}
    req = requests.post("https://feelinsonice.appspot.com/ph/sync", data)
    return req


def get_image(usr, token, img_id):
    # Form URL and download encrypted "blob"
    blob_url = "https://feelinsonice.appspot.com/ph/blob?id={}".format(img_id)
    blob_url += "&username=" + usr + "&timestamp=" + str(timestamp()) + "&req_token=" + req_token(token)
    enc_blob = requests.get(blob_url).content  
    # Save decrypted image
    img = open('images/' + img_id + '.jpg', 'wb')
    img.write(decrypt(enc_blob))
    img.close()
    return static_file(img_id + '.jpg', root='images/')

def get_video(usr, token, img_id):
    # Form URL and download encrypted "blob"
    blob_url = "https://feelinsonice.appspot.com/ph/blob?id={}".format(img_id)
    blob_url += "&username=" + usr + "&timestamp=" + str(timestamp()) + "&req_token=" + req_token(token)
    enc_blob = requests.get(blob_url).content  
    # Save decrypted image
    img = open('videos/' + img_id + '.mp4', 'wb')
    img.write(decrypt(enc_blob))
    img.close()
    return static_file(img_id + '.mp4', root='images/')

'''    
def unread(usr, pwd):
    auth_token = json.loads(login(usr, pwd).text)['auth_token']
    feed = json.loads(sync(usr, auth_token).text)
    for snap in feed['snaps']:
        if 'rp' not in snap or 'm' in snap:
            if snap['m'] == 0 and snap['st'] == 1:
                get_blob(usr, auth_token, snap['id'])
'''       
            
def timestamp():
    return int(round(time.time() * 1000))

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

@route('/login', method='POST')
def log():
    username = request.POST.get('username', '').split()
    password = request.POST.get('password', '').split()
    print(username, password)
    return login(username, password).text

@route('/signup', method='POST')
def signup():
    usr = request.POST.get('username', '').split()
    pwd = request.POST.get('password', '').split()
    email = request.POST.get('email', '').split()
    birthday = request.POST.get('birthday', '').split()
    res = signup(usr, pwd, email, birthday)
    return res.text

@route('/token', method='POST')
def token():
    auth_token = request.POST.get('auth_token', '').split()
    return req_token(auth_token)
    
@route('/image', method='GET')
def image():
    username = request.query.username
    token = request.query.auth_token
    img_id = request.query.id
    return get_image(username, token, img_id)

@route('/video', method='GET')
def video():
    username = request.query.username
    token = request.query.auth_token
    img_id = request.query.id
    return get_video(username, token, img_id)

'''
@route('/unread')
def get_unread():

    username = request.query.username
    password = request.query.password
    return unread(username, password)
'''

# WebPortal Commands
@route('/style')
def get_style():
    return static_file('static/bootstrap.css', root='')

@route('/theme')
def get_theme():
    return static_file('static/boostrap-theme.css', root='')

@route('/')
def home():
    return template('login.tpl')

@route('/web_signup')
def create_account():
    return template('register.tpl')

@route('/web_log', method='POST')
def web_log():
    usr = request.POST.get('username', '').split()
    pwd = request.POST.get('password', '').split()
    feed = json.loads(login(usr, pwd).text)
    snaps = feed['snaps']
    return template('snap_list.tpl', snaps = snaps, snap = snaps[0])

@route('/register', method='POST')
def web_reg():
    usr = request.POST.get('username', '').split()
    pwd = request.POST.get('password', '').split()
    email = request.POST.get('email', '').split()
    birthday = request.POST.get('birthday', '').split()
    res = signup(usr, pwd, email, birthday)
    print(res)
    return template('<p>{{data}}</p>', res.text)

run(host="localhost", port=int(os.environ.get("PORT", 17241)))

