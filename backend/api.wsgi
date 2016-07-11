#!/usr/bin/env python
# -*- coding:utf-8 -*-

from bottle import Bottle, request, response

from common import Hubot, apikey, param, success, failed
import config

app = application = Bottle()
get = app.get
post = app.post
put = app.put
delete = app.delete


@post('/hubot')
@apikey
@param(require=['slack_token'])
def api_create_hubot(params):
    h = Hubot.create(params['slack_token'])
    if h.last_response.status_code in [200, 201]:
        return success(name=h.name)
    else:
        return failed(name=h.name)


@post('/hubot/start')
@apikey
@param(require=['name'])
def api_start_hubot(params):
    h = Hubot(params['name'])
    h.start()
    if h.last_response.status_code == 204:
        return success(name=h.name)
    else:
        return failed(name=h.name)


@post('/hubot/stop')
@apikey
@param(require=['name'])
def api_stop_hubot(params):
    h = Hubot(params['name'])
    h.stop()
    if h.last_response.status_code == 204:
        return success(name=h.name)
    else:
        return failed(name=h.name)


@delete('/hubot')
@apikey
@param(require=['name'])
def api_remove_hubot(params):
    h = Hubot(params['name'])
    h.remove()
    if h.last_response.status_code == 204:
        return success()
    else:
        return failed()


@put('/hubot')
@apikey
@param(require=['name'])
def api_update_hubot(params):
    h = Hubot(params['name'])
    h.stop()
    h.update()
    h.start()
    if h.last_response.status_code == 204:
        return success(h.name)
    else:
        return failed()


@get('/hubot/<name>/env')
def api_get_hubot_env(name):
    h = Hubot(name)
    return success(h.get_env())
