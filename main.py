import hmac
import base64
from hashlib import sha1
import os


def generate_device_Id():
    identifier = os.urandom(20)
    return ("32" + identifier.hex() + hmac.new(bytes.fromhex("76b4a156aaccade137b8b1e77b435a81971fbd3e"),
                                               b"\x32" + identifier, sha1).hexdigest()).upper()


import amino
import json
import threading
import wget
import requests
import heroku3
from new import emaill, passwordd, custompwd, chatlink, private, key, app_name, deviceid, nickname, replit


def restart():
    heroku_conn = heroku3.from_key(key)
    botapp = heroku_conn.apps()[app_name]
    botapp.restart()


client = amino.Client(deviceid)
client.login(emaill, passwordd)
bb = client.get_from_code(chatlink)
chatId = bb.objectId
cid = bb.path[1:bb.path.index("/")]
client.join_community(cid)
sub = amino.SubClient(comId=cid, profile=client.profile)
sub.join_chat(chatId)

def code(url):
    return requests.post('https://60da331a-4c43-4af6-931a-f738c5a1d607.id.repl.co/submundo', data={'image': url}).json()['captcha'][0]

password = custompwd
# client.devicee()
de = generate_device_Id()
client = amino.Client(de)
for _ in range(3):
    try:
        os.remove("code.png")
    except:
        pass
    dev = client.device_id
    email = client.gen_email()
    print(email)
    client.request_verify_code(email=email, dev=dev)
    url = client.get_message(email)
    wget.download(url=url, out="code.png")
    with open("code.png", "rb") as file:
        sub.send_message(chatId=chatId, fileType="image", file=file)
        sub.send_message(chatId=chatId, message="start convert code.", messageType=0)
    code = requests.post('https://60da331a-4c43-4af6-931a-f738c5a1d607.id.repl.co/submundo', data={'image': url}).json()['captcha'][0]
    sub.send_message(chatId=chatId, message=("THE CODE is : "+str(code)), messageType=0)

    try:
        client.register(email=email, password=password, nickname=nickname, verificationCode=code, deviceId=dev)
        d = {}
        d["email"] = str(email)
        d["password"] = str(password)
        d["device"] = str(dev)
        # t=json.dumps(d)
        print(d)
        requests.get(url=f"{replit}/api/save?email={str(email)}&password={str(password)}&device={str(dev)}")
    except Exception as l:
        print(l)
        pass

    # de=client.devicee()
de = generate_device_Id()
client = amino.Client(de)
for _ in range(2):
    try:
        os.remove("code.png")
    except:
        pass
    dev = client.device_id
    email = client.gen_email()
    print(email)
    client.request_verify_code(email=email, dev=dev)
    url = client.get_message(email)
    wget.download(url=url, out="code.png")
    with open("code.png", "rb") as file:
        sub.send_message(chatId=chatId, fileType="image", file=file)
        sub.send_message(chatId=chatId, message="start convert code.", messageType=0)
    code = requests.post('https://60da331a-4c43-4af6-931a-f738c5a1d607.id.repl.co/submundo', data={'image': url}).json()['captcha'][0]
    sub.send_message(chatId=chatId, message=("THE CODE is : " + str(code)), messageType=0)

    try:
        client.register(email=email, password=password, nickname=nickname, verificationCode=code, deviceId=dev)
        d = {}
        d["email"] = str(email)
        d["password"] = str(password)
        d["device"] = str(dev)
        # t=json.dumps(d)
        print(d)
        requests.get(url=f"{replit}/api/save?email={str(email)}&password={str(password)}&device={str(dev)}")
    except Exception as k:
        print(k)
        pass

restart()
