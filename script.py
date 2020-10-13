def response(room, msg, sender, isGroupChat, replier, packageName, Kakao):
  if msg == "안녕!":
    replier.reply("안녕하세요.")
  
  return replier.data
