data = []

class replier:
  global data
  def __init__(self, packName, room, isDebugChat):
    self.isDebugChat = isDebugChat
    self.packName = packName
    self.room = room
    self.data = data
  
  def clear(self):
    del data[:]

  def reply(self, msg):
    data.append(msg)
    print(data)

class KakaoLink:
  global data
  def send(self, room, args, type):
    data.append({
      'room' : room,
      'args' : args,
      'type' : type
    })
