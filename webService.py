from flask import Flask, render_template, request
import requests, urllib
app = Flask(__name__)

#Логика
@app.route("/")
def index():
    #user = { 'nickname': 'Max' } # выдуманный пользователь
    user = { 'nickname' : request.args.get('name'),
            'content' : request.args.get('message')}
    msg = "Давай дружить"
    encode_msg = urllib.parse.quote(msg.encode('utf-8'))
    return render_template("index.html",
        title = "Rekruto",
        encode_msg  = encode_msg,
        user = user)


#Запуск
if __name__ == "__main__":
    app.run(host = '127.0.0.1', port=1717)
