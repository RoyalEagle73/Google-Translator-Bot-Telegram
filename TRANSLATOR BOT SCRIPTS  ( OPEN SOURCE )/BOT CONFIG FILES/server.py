from bot import telegram_chatbot
import translator_script

bot = telegram_chatbot("config.cfg")


def make_reply(msg):
    reply = None
    msg = msg.lower()
    if msg is not None:
        try:
            if '/' in msg :
                data = msg.split('/')
            elif '\\' in msg :
                data = msg.split('\\')
            

            if '\\' in msg or '/' in msg:
                if len(data)==4 :
                    del(data[0])
                    print(data)
                lang1 = data[0]
                lang2 = data[1]
                msg = data[2]
                reply = translator_script.text(data[0], data[1], data[2])
            return reply    
        except Exception as e:
            reply = None
            return reply


update_id = None
while True:
    # with open("last_update_id.txt", 'r+') as last_seen:
    #     update_id = last_seen.read()
    updates = bot.get_updates(offset=update_id)
    updates = updates['result']
    if updates:
        for item in updates[len(updates)-1:]:
            update_id = item["update_id"]
            try:
                message = str(item["message"]["text"])
            except:
                message = None
            print()
            print(item)
            print()
            try:
                from_ = item["message"]["from"]["id"]
            except Exception as e:
                from_ = item["edited_message"]["from"]["id"]
            
            reply = make_reply(message)
            bot.send_message(reply, from_)
