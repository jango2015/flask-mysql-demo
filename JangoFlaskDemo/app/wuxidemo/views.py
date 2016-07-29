from app.services.pythonmongotestservice import get_accounts,get_account_by_appid
from flask import render_template
from app.services.redistestservice import get_by_key,set_by_key
# import json
from . import users
@users.route('/users')
def index():
    users = get_accounts()
    # users = json.loads(users)
    return  render_template('users.html',users=users)

appid = 'wx410bd3fe3afd168c'
@users.route('/users/id')
def user():
    cache = get_by_key(appid)
    if cache is None:
        item = get_account_by_appid(appid)
        cache = item
        set_by_key(appid,item)
    # item = json.loads(item)
    return render_template('users.html',users=cache)