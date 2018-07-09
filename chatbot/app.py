from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os, json
from flask import Flask, render_template, request
from flask import jsonify

app = Flask(__name__,static_url_path="/static")
bot = ChatBot('Servify_bot')

bot.set_trainer(ListTrainer)

curr_dir=os.getcwd()

path=curr_dir+'/servify/'

for files in os.listdir(path):
    data = open(path + files ,'r',encoding='iso-8859-1').readlines()
    bot.train(data)
#############
# Routing
#
@app.route('/message', methods=['POST'])
def reply():
    message = request.form['msg']
    reply=str(bot.get_response(message))
    print(reply)
    
    return jsonify({'text':reply})
    #return jsonify( { 'text': execute.decode_line(sess, model, enc_vocab, rev_dec_vocab, request.form['msg'] ) } )

@app.route("/")
def index():
    return render_template("index.html")

# start app
if (__name__ == "__main__"):
    app.run(port = 8000)
