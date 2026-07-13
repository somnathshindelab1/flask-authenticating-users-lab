import os
import sys

sys.path.insert(0, os.getcwd())

from app import app
from models import db, User

with app.app_context():
    db.drop_all()
    db.create_all()
    user = User(username='demo')
    db.session.add(user)
    db.session.commit()
    print('db ready')

    with app.test_client() as client:
        client.get('/clear')
        resp = client.post('/login', json={'username': 'demo'})
        print('login', resp.status_code, resp.get_json())
        print('session', client.session_transaction().get('user_id'))
        resp2 = client.delete('/logout')
        print('logout', resp2.status_code, resp2.data)
        resp3 = client.get('/check_session')
        print('check', resp3.status_code, resp3.get_json())
