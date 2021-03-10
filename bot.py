from flask import Flask, request, jsonify
from webexteamssdk import WebexTeamsAPI
import os


WT_BOT_TOKEN =  os.environ['WT_BOT_TOKEN1']
#WT_BOT_TOKEN = 'put your bot token'

app = Flask(__name__)
api = WebexTeamsAPI(access_token=WT_BOT_TOKEN)
#api.messages.create(toPersonEmail="aalmodha@cisco.com", markdown='hello it\'s me \n from your bot')

@app.route('/', methods=['POST'])
def webhook():
    raw_json = request.get_json()
    #s = str(raw_json)

    if raw_json['resource'] == 'messages' : # depending in the type of webhook, create if statment
        message_id = raw_json['data']['id']
        message = api.messages.get(message_id)
        if message.personEmail != 'rep@webex.bot': # so the bot does not reply to itself
            api.messages.create(toPersonEmail=message.personEmail, markdown=message.text)
    else :
        pass
    
    #webex webhook expects ok response back. after a certen requiests without ok resposne it will disactivate the webhook
    return jsonify({'success': True})



if __name__=="__main__":
    app.run()



