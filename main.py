
import hmac
import base64
from hashlib import sha1
from hmac import new
import os
import secmail
import aminofix as amino
import json
import threading
import wget
import time
import requests
import heroku3
from bs4 import BeautifulSoup
from new import emaill, passwordd, custompwd, chatlink, private, key, app_name, deviceid, nickname, replit


PREFIX = bytes.fromhex("42")
SIG_KEY = bytes.fromhex("F8E7A61AC3F725941E3AC7CAE2D688BE97F30B93")
DEVICE_KEY = bytes.fromhex("02B258C63559D8804321C5D5065AF320358D366F")

def generate_device_Id() -> str:
    identifier = PREFIX + (os.urandom(20))
    mac = new(DEVICE_KEY, identifier, sha1)
    return f"{identifier.hex()}{mac.hexdigest()}".upper()


def gen_email():
    mail = secmail.SecMail()
    email = mail.generate_email()
    return email

def get_message(email):
    url="0"
    try:
        time.sleep(3)
        f=email
        mail = secmail.SecMail()
        inbox = mail.get_messages(f)
        print('done')
        for Id in inbox.id:
          msg = mail.read_message(email=f, id=Id).htmlBody
          bs = BeautifulSoup(msg, 'html.parser')
          images = bs.find_all('a')[0]
          url = (images['href']+'\n')
          if url is not None:
            print('Vrification Url\n')
            print(url)
    except:
        pass
    return url

def captcha_solver(captcha: str):
    return requests.post(
            "https://captchasolver.neodouglas.repl.co/predict",
            data={"image": captcha}
        ).json()['captcha'][0]


client = amino.Client(deviceid)
client.login(emaill, passwordd)
bb = client.get_from_code(chatlink)
chatId = bb.objectId
cid = bb.path[1:bb.path.index("/")]
client.join_community(cid)
sub = amino.SubClient(comId=cid, profile=client.profile)
sub.join_chat(chatId)

password = custompwd
# client.devicee()

device = generate_device_Id()
client = amino.Client(device)
for _ in range(3):
    try:
        os.remove("code.png")
    except:
        pass
    devicee = client.device_id
    email = gen_email()
    print(email)
    client.request_verify_code(email=email)
    url = get_message(email)
    try:
        code = captcha_solver(url)
        print(code)
    except:
        print("cant get code")
    sub.send_message(chatId=chatId, message=("THE CODE is : "+str(code)), messageType=0)

    try:
        client.register(email=email, password=password, nickname=nickname, verificationCode=str(code), deviceId=devicee)
        d = {}
        d["email"] = str(email)
        d["password"] = str(password)
        d["device"] = str(devicee)
        # t=json.dumps(d)
        print(d)
        requests.get(url=f"{replit}/api/save?email={str(email)}&password={str(password)}&device={str(devicee)}")
    except Exception as l:
        print(l)
        pass

    # de=client.devicee()
device = generate_device_Id()
client = amino.Client(device)
for _ in range(2):
    try:
        os.remove("code.png")
    except:
        pass
    devicee = client.device_id
    email = gen_email()
    print(email)
    client.request_verify_code(email=email)
    url = get_message(email)
    try:
        code = captcha_solver(url)
        print(code)
    except:
        print("cant get code")
    sub.send_message(chatId=chatId, message=("THE CODE is : " + str(code)), messageType=0)

    try:
        client.register(email=email, password=password, nickname=nickname, verificationCode=str(code), deviceId=devicee)
        d = {}
        d["email"] = str(email)
        d["password"] = str(password)
        d["device"] = str(devicee)
        # t=json.dumps(d)
        print(d)
        requests.get(url=f"{replit}/api/save?email={str(email)}&password={str(password)}&device={str(devicee)}")
    except Exception as k:
        print(k)
        pass




