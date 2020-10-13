const kalingModule = require('kaling').Kakao();
const Kakao = new kalingModule;
Kakao.init('Your JS Key')
Kakao.login('Your ID', 'Your Password')

function response(room, msg, sender, isGroupChat, replier, imageDB, packageName) {
  const info = {
    room : room,
    msg : msg,
    sender : sender,
    isGroupChat : isGroupChat,
    packageName : packageName,
    isDebugChat : replier.isDebugChat
  };
  
  const url = "https:// - Your Flask Server URL - /";
  const connect = org.jsoup.Jsoup.connect(url + JSON.stringify(info).replace(/\//g, "=pl_Steve28_lq=")).execute();
  const data = JSON.parse(connect.body().replace(/\'/g, '\"'));
  for (let i of data) {
    if (typeof i == 'string') replier.reply(i);
    else Kakao.send(i.room, i.args, i.type);
  }
}
