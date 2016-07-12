#!/usr/bin/env python
# -*- coding:utf-8 -*-

from bottle import Bottle

from common import Hubot, User, apikey, param, success, failed, root

app = application = Bottle()
get = app.get
post = app.post
put = app.put
delete = app.delete


@post('/user')
@root()
@param(require=['username'])
def api_create_user(params):
    u = User.create(params['username'])
    if u:
        return success(apikey=u.apikey)
    else:
        return failed()


@post('/hubot')
@apikey
@param(require=['slack_token'])
def api_create_hubot(params, user):
    h = Hubot.create(params['slack_token'])
    if h.last_response.status_code in [200, 201]:
        return success(name=h.name)
    else:
        return failed(error=h.last_response.text)


@post('/hubot/start')
@apikey
@param(require=['name'])
def api_start_hubot(params, user):
    h = Hubot(params['name'])
    h.start()
    if h.last_response.status_code == 204:
        return success(name=h.name)
    else:
        return failed(error=h.last_response.text)


@post('/hubot/stop')
@apikey
@param(require=['name'])
def api_stop_hubot(params, user):
    h = Hubot(params['name'])
    h.stop()
    if h.last_response.status_code == 204:
        return success(name=h.name)
    else:
        return failed(error=h.last_response.text)


@post('/hubot/restart')
@apikey
@param(require=['name'])
def api_restart_hubot(params, user):
    h = Hubot(params['name'])
    h.restart()
    if h.last_response.status_code == 204:
        return success(name=h.name)
    else:
        return failed(error=h.last_response.text)


@delete('/hubot')
@apikey
@param(require=['name'])
def api_remove_hubot(params, user):
    h = Hubot(params['name'])
    h.remove()
    if h.last_response.status_code == 204:
        return success()
    else:
        return failed(error=h.last_response.text)


@put('/hubot')
@apikey
@param(require=['name'], option=['slack_token'])
def api_update_hubot(params, user):
    h = Hubot(params['name'])
    h.stop()
    h.update(
        slack_token=params['slack_token']
    )
    if h.last_response.status_code in [200, 201]:
        h.start()
        if h.last_response.status_code == 204:
            return success(h.name)
    return failed(error=h.last_response.text)


@get('/hubot/<name>/env')
def api_get_hubot_env(name):
    h = Hubot(name)
    if h.enable:
        return success(h.get_env())
    return failed(error='No Such Container: {}'.format(name))


@get('/hubot/<name>/db')
def api_get_hubot_db(name):
    h = Hubot(name)
    if h.enable:
        return success(h.db)
    return failed(error='No Such Container: {}'.format(name))

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
