import http.client
import json
import urllib.request
import hashlib
import os
from dotenv import load_dotenv
load_dotenv()

def get_external_ip():
    return urllib.request.urlopen('https://ident.me').read().decode('utf8')

connection = http.client.HTTPSConnection('api.twitch.tv')
clientid = os.getenv('CLIENT_ID')
auth = {'Client-ID': clientid, 'Authorization': os.getenv('TWITCH_TOKEN')}
secret = os.getenv('TWITCH_SECRET')
lease_seconds = 864000
callback = os.getenv('TWITCH_CALLBACK')

def get_twitch_user_by_name(usernames):

    if isinstance(usernames, list):
        usernames = ['login={0}'.format(i) for i in usernames]
        req = '/helix/users?'+'&'.join(usernames)
    else:
        req = '/helix/users?login='+usernames

    print(req)
    connection.request('GET', req ,None, headers=auth)
    response = connection.getresponse()
    print(response.status, response.reason)
    re = response.read().decode()
    print(re)
    j = json.loads(re)
    return j

def get_twitch_user_by_id(userids):

    if isinstance(userids, list):
        userids = ['id={0}'.format(i) for i in userids]
        req = '/helix/users?'+'&'.join(userids)
    else:
        req = '/helix/users?id='+userids

    print(req)
    connection.request('GET', req ,None, headers=auth)
    response = connection.getresponse()
    print(response.status, response.reason)
    re = response.read().decode()
    print(re)
    j = json.loads(re)
    return j

def get_twitch_userid(usernames):

    j = get_twitch_user_by_name(usernames)
    if isinstance(usernames, list):
        relist = []
        for a in j["data"]:
            relist.append(a["id"])
        userid = relist
    else:
        userid = (j["data"][0]["id"])
    return userid

def get_twitch_username(userid):

    j = get_twitch_user_by_id(userid)
    if isinstance(userid, list):
        relist = []
        for a in j["data"]:
            relist.append(a["login"])
        userid = relist
    else:
        userid = (j["data"][0]["login"])
    return userid
    
def suscribe_to_get_followers(id):

    mode = 'subscribe'    
    print("callback to: "+callback);
    headers = {'Client-ID': clientid, 'Content-type': 'application/json', 'Authorization': os.getenv('TWITCH_TOKEN')}

    topic = 'https://api.twitch.tv/helix/users/follows?first=1&to_id='+id

    foo = { 'hub.mode':mode,
            'hub.topic':topic,
            'hub.callback':callback,
            'hub.lease_seconds':lease_seconds,
            'hub.secret': secret
            }

    json_foo = json.dumps(foo)

    connection.request('POST', '/helix/webhooks/hub' ,body=json_foo, headers=headers)
    
    response = connection.getresponse()
    print(response.status, response.reason)
    print(response.read().decode())


def suscribe_to_get_followerlist(idlist):
    idlist = get_twitch_userid(idlist)
    for id in idlist:
        suscribe_to_get_followers(id)