def response(room, msg, sender, isGroupChat, replier, packageName, Kakao):
  if msg == "안녕!":
    replier.reply("안녕하세요.")
    Kakao.send(room, 대충 템플릿 JSON 이라는 것, "custom")
  If sender == "Steve28":
    replier.reply("안녕하세요, " + sender + "님!")

  return replier.data
