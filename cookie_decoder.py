from flask import Flask, jsonify, session, request
from flask_cookie_decode import CookieDecode
import hashlib
from itsdangerous import URLSafeTimedSerializer
from flask.sessions import TaggedJSONSerializer

app = Flask(__name__)
app.config.update({'SECRET_KEY': 'thisisasuperrandomsecretkeyforsessionmate'})
# cookie = CookieDecode()
# cookie.init_app(app)
SECRET_KEY = 'thisisasuperrandomsecretkeyforsessionmate'


@app.route('/')
def index():
    a = request.args.get('a')
    b = decode_flask_cookie(SECRET_KEY, a)
    print(b)
    return '1'


def decode_flask_cookie(secret_key, cookie_str):
    salt = 'cookie-session'
    serializer = TaggedJSONSerializer()
    signer_kwargs = {
        'key_derivation': 'hmac',
        'digest_method': hashlib.sha1
    }
    s = URLSafeTimedSerializer(secret_key, salt=salt, serializer=serializer, signer_kwargs=signer_kwargs)
    return s.loads(cookie_str)


if __name__ == "__main__":
    app.run()
