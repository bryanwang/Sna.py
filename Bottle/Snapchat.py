from SnapSec import *
from bottle import static_file
import requests
import json

import random
import string
import time

class Snapchat:
    sec = SnapSec()

    def __init__(self):
        pass

    def login(self, username, password):
        data = {'username': username,
                'password': password,
                'timestamp': self.sec.timestamp(),
                'req_token': self.sec.req_token(self.sec.STATIC_TOKEN)}
        req = requests.post('https://feelinsonice-hrd.appspot.com/bq/login', data)
        return req

    def logout(self, username, auth_token):
        data = {'username': username,
                'timestamp': self.sec.timestamp(),
                'req_token': self.sec.req_token(auth_token),
                'json': {},
                'events': []}
        req = requests.post('https://feelinsonice-hrd.appspot.com/bq/logout', data)
        return req

    def signup(self, username, password, email, birthday):
        data = {'email': email,
                'password': password,
                'birthday': birthday,
                'timestamp': self.sec.timestamp(),
                'req_token': self.sec.req_token(self.sec.STATIC_TOKEN),
                'time_zone': 'America/Chicago'}
        req = requests.post('https://feelinsonice-hrd.appspot.com/bq/register', data)
        data2 = {'username': username,
                'email': email,
                'timestamp': self.sec.timestamp(),
                'req_token': self.sec.req_token(self.sec.STATIC_TOKEN)}
        req2 = requests.post('https://feelinsonice-hrd.appspot.com/bq/registeru', data2)
        return req2

    '''
    def get_image(self, username, auth_token, image_id):
        blob_url = "https://feelinsonice.appspot.com/ph/blob?id={}".format(image_id)
        blob_url += "&username=" + username + "&timestamp=" + str(self.sec.timestamp()) + "&req_token=" + self.sec.req_token(auth_token)
        enc_blob = requests.get(blob_url).content  
        img = open('images/' + image_id + '.jpg', 'wb')
        img.write(self.sec.decrypt(enc_blob))
        img.close()
        return static_file(image_id + '.jpg', root='images/')

    def get_video(self, username, auth_token, video_id):
        blob_url = "https://feelinsonice.appspot.com/ph/blob?id={}".format(video_id)
        blob_url += "&username=" + username + "&timestamp=" + str(self.sec.timestamp()) + "&req_token=" + self.sec.req_token(auth_token)
        enc_blob = requests.get(blob_url).content  
        img = open('videos/' + video_id + '.mp4', 'wb')
        img.write(self.sec.decrypt(enc_blob))
        img.close()
        return static_file(video_id + '.mp4', root='videos/')
    '''

    def get_media(self, username, auth_token, media_id):
        data = {'username': username,
                'timestamp': self.sec.timestamp(),
                'req_token': self.sec.req_token(auth_token),
                'id': media_id}
        req = requests.post('https://feelinsonice-hrd.appspot.com/bq/blob', data)
        raw = self.sec.decrypt(req.content)
        if b"\xFF\xD8\xFF\xE0" in raw:
            with open('images/' + media_id + '.jpg', 'wb') as f:
                f.write(raw)
            return static_file(media_id + '.jpg', root='images/')
        with open('videos/' + media_id + '.mp4', 'wb') as f:
            f.write(raw)
        return static_file(media_id + '.mp4', root='videos/')

    def stories(self, username, auth_token):
        data = {'username': username,
                'timestamp': self.sec.timestamp(),
                'req_token': self.sec.req_token(auth_token)}
        req = requests.post('https://feelinsonice-hrd.appspot.com/bq/stories', data)
        return req

    def upload(self, username, auth_token, content, media_id, data_type):
        data = {'username': username,
                'timestamp': self.sec.timestamp(),
                'req_token': self.sec.req_token(auth_token),
                'media_id': media_id,
                'type': data_type}
        files = {'data': self.sec.encrypt(content)}
        req = requests.post('https://feelinsonice-hrd.appspot.com/bq/upload', data=data, files=files)
        return req

    def send(self, username, auth_token, recipient, media_id, media_type, time):
        data = {'username': username,
                'timestamp': self.sec.timestamp(),
                'req_token': self.sec.req_token(auth_token),
                'recipient': recipient,
                'media_id': media_id,
                'type': media_type,
                'time': time}
        req = requests.post('https://feelinsonice-hrd.appspot.com/bq/send', data=data)
        return req

    def snap(self, username, auth_token, recipient, content, media_type, time):
        media_id = self.sec.media_id(username)
        self.upload(username, auth_token, content, media_id, media_type)
        return self.send(username, auth_token, recipient, media_id, media_type, time)

    def add_to_story(self, username, auth_token, media_id, media_type, time):
        data = {'username': username,
                'timestamp': self.sec.timestamp(),
                'req_token': self.sec.req_token(auth_token),
                'media_id': media_id,
                'client_id': media_id,
                'type': media_type,
                'time': time}
        req = requests.post('https://feelinsonice-hrd.appspot.com/bq/post_story' data)
        return req

    '''
    # Needs updating. 
    # Can't test because account was rate limited.
    # More info about this to come on my blog http://neuebits.com
    def find_friend(self, username, auth_token, number, name):
        data = {'username': username,
                'timestamp': self.sec.timestamp(),
                'req_token': self.sec.req_token(auth_token),
                'countryCode': 'US'}
        number = json.dumps({number: name})
        data = dict(data, numbers=n)
        req = requests.post('https://feelinsonice-hrd.appspot.com/bq/find_friends', data=data, headers={"User-agent": None})
        return req
    '''
    