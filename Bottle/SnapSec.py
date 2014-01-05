from Crypto.Cipher import AES
from hashlib import sha256
import time
import uuid

class SnapSec:
    SECRET = b'iEk21fuwZApXlz93750dmW22pw389dPwOk'
    STATIC_TOKEN = 'm198sOkJEn37DjqZ32lpRu76xmw288xSQ9'
    HASH_PATTERN = '0001110111101110001111010101111011010001001110011000110001000110'
    KEY = 'M02cnQ51Ji97vwT4'

    def __init__(self):
        pass

    def timestamp(self):
        return int(round(time.time() * 1000))

    def media_id(self, username):
        return '{0}~{1!s}'.format(username.upper(), uuid.uuid4())

    def req_token(self, auth_token):
        return self.hash256(auth_token, str(self.timestamp()))

    def hash256(self, var1, var2):
        h1 = sha256(self.SECRET + var1.encode('utf-8')).hexdigest()
        h2 = sha256(var2.encode('utf-8') + self.SECRET).hexdigest()
        result = ''
        for i in range(0, len(h1)):
            result += h2[i] if self.HASH_PATTERN[i] is "1" else h1[i]
        return result

    def pad(self, data, bs=16):
        pc = bs - len(data) % bs
        return data + (chr(pc) * pc).encode('utf-8')

    def decrypt(self, data):
        cipher = AES.new(self.KEY, AES.MODE_ECB)
        return cipher.decrypt(self.pad(data))

    def encrypt(self, data):
        cipher = AES.new(self.KEY, AES.MODE_ECB)
        return cipher.encrypt(self.pad(data))