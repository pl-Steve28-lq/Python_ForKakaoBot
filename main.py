from flask import Flask
import json
from script import response
from replierClass import replier, KakaoLink

app = Flask('app')

@app.route('/<info>')
def resp(info):
  data = json.loads(info.replace('\'', '\"').replace('=pl_Steve28_lq=', '/'))
  room = data['room']
  msg = data['msg']
  sender = data['sender']
  isGroupChat = data['isGroupChat']
  packageName = data['packageName']
  isDebugChat = data['isDebugChat']
  
  r = replier(packageName, room, isDebugChat)
  r.clear()
  k = KakaoLink()
  return str(response(room, msg, sender, isGroupChat, r, packageName, k))

app.run(host='0.0.0.0', port=8080)
