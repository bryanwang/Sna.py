import os
import bottle
from bottle import route, run, request, post, static_file, template

from SnapSec import *
from Snapchat import *

import json

sec = SnapSec()
snap = Snapchat()

class SnapBottle:

    def __init__(self):
        pass

    @staticmethod
    def run(host, port):
        run(host=host, port=int(os.environ.get("PORT", port)))

    @route('/login', method='POST')
    def log():
        username = request.POST.get('username', '').split()
        password = request.POST.get('password', '').split()
        return snap.login(username, password).text

    @route('/get_login', method='GET')
    def get_log():
        username = request.query.username
        password = request.query.password
        return snap.login(username, password).text

    @route('/logout', method='POST')
    def logout():
        username = request.POST.get('username', '').split()
        auth_token = request.POST.get('auth_token').split()
        return snap.logout(username, auth_token).text

    @route('/get_logout', method='GET')
    def get_logout():
        username = request.query.username
        auth_token = request.query.auth_token
        return snap.logout(username, auth_token).text

    @route('/signup', method='POST')
    def signup():
        username = request.POST.get('username', '').split()
        password = request.POST.get('password', '').split()
        email = request.POST.get('email', '').split()
        birthday = request.POST.get('birthday', '').split()
        return snap.signup(username, password, email, birthday).text

    @route('/get_signup', method='GET')
    def get_signup():
        username = request.query.username
        password = request.query.password
        email = request.query.email
        birthday = request.query.birthday
        return snap.signup(usr, pwd, email, birthday).text

    @route('/req_token', method='POST')
    def token():
        auth_token = request.POST.get('auth_token', '').split()
        return sec.req_token(auth_token)

    @route('/get_req_token', method='GET')
    def get_token():
        auth_token = request.query.auth_token
        return sec.req_token(auth_token)
        
    @route('/image', method='GET')
    def image():
        username = request.query.username
        auth_token = request.query.auth_token
        image_id = request.query.id
        return snap.get_image(username, auth_token, image_id)
        
    @route('/video', method='GET')
    def video():
        username = request.query.username
        auth_token = request.query.auth_token
        video_id = request.query.id
        return snap.get_video(username, auth_token, video_id)

    @route('/send', method='POST')
    def send():
        username = request.POST.get('username', '').split()
        auth_token = request.POST.get('auth_token', '').split()
        recipient = request.POST.get('recipient', '').split()
        content = request.files.data
        data_type = request.POST.get('data_type', '').split()
        time = request.POST.get('time', '').split()
        return snap.snap(username, auth_token, recipient, content.file.read(), data_type, time).text

    @route('/find_friend', method='POST')
    def find_friend():
        username = request.POST.get('username', '').split()
        auth_token = request.POST.get('auth_token', '').split()
        name = request.POST.get('name', '').split()
        number = request.POST.get('number', '').split()
        return find_friend(username, auth_token, name, number).text

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
    def web_signup():
        return template('register.tpl')

    @route('/web_login', method='POST')
    def web_log():
        # Load request variables and login data
        username = request.POST.get('username', '')
        #username = username[2:len(username)-2]
        password = request.POST.get('password', '')
        feed = json.loads(snap.login(username, password).text)
        # Define template variables
        auth_token = feed['auth_token']
        snap_id = list()
        snap_sn = list()
        snaps = list()
        snap_url = list()
        # Filter for unopened images
        for s in feed['snaps']:
            if 'rp' not in s or 'm' in s:
                # Images
                if s['m'] == 0 and s['st'] == 1 and 'sn' in s:
                    snaps.append(s)
                    snap_id.append(s['id'])
                    snap_sn.append(s['sn'])
                    snap_url.append('\'/snapy/image?username=' + str(username) + '&auth_token=' + str(auth_token) + '&id=' + str(s['id']) + '\'')
                # Videos
                if s['m'] == 1 and s['st'] == 1 and 'sn' in s:
                    snaps.append(snap)
                    snap_id.append(s['id'])
                    snap_sn.append(s['sn'])
                    snap_url.append('\'/snapy/video?username=' + str(username) + '&auth_token=' + str(auth_token) + '&id=' + str(s['id']) + '\'')
        return template('snap_list.tpl', loadImage = snap_url, ids = snap_id, senders = snap_sn)

    @route('/web_send', method='POST')
    def web_send():
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        feed = json.loads(snap.login(username, password).text)
        auth_token = feed['auth_token']
        recipient = request.POST.get('recipient', '')
        content = request.files.data
        data_type = 0
        time = 10
        snap.snap(username, auth_token, recipient, str(content), data_type, time)
        return 'Your image was successfully sent'


