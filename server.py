from bot import telegram_chatbot
from emoji import emojize,demojize
import telegram

bot = telegram_chatbot("config.cfg")
import stocks_price
# print(bot.token)
update_id = None

def make_reply(msg):
    if msg is not None:
        msg = msg.decode('utf-8')[2:-1]
        reply = "Hey there! \nIshan's bot here.\nThis is how can I help! Reply num of choice\n :one: Stock Indexes\n :two: Stock Mkt Facts \n :three: Gold and Silver Price \n :four: Dollar Price\n :five: Petrol Prices\n :six: Diesel Prices\n :seven: Corona Cases"
        print(msg)
        try:
            if msg.isnumeric() and int(msg) < 8:
                if int(msg) == 1:
                    reply = stocks_price.stock_prices()
                elif int(msg) == 2:
                    reply = stocks_price.facts()
                elif int(msg) == 3:
                    reply = stocks_price.gold_price() + '\n' + stocks_price.silver_price()
                elif int(msg) == 4:
                    reply = stocks_price.dollar_price()
                elif int(msg) == 5:
                    reply = stocks_price.petrol_price()
                elif int(msg) == 6:
                    reply = stocks_price.diesel_price()
                elif int(msg) == 7:
                    reply,reply_ind = stocks_price.corona_tracker()
                    reply = emojize(reply,use_aliases=True)
                    reply_ind = emojize(reply_ind,use_aliases=True)
                    return [reply,reply_ind]
                else:
                    reply = "You might have not read menu properly"'\n'+reply
            else:
                reply = reply
        except Exception as e:
            print(e)
            reply = 'FATAL issues occured will be back soon. This has been reported to admin. Till then try other option'
    return emojize(reply,use_aliases=True)


while True:
    print("...")
    updates = bot.get_updates(offset=update_id)
    # print(updates)
    updates = updates["result"]

    if updates :
        for item in updates:
            update_id = item["update_id"]
            sender = ('Unknown' if not item['message']['from']['first_name'] else item['message']['from']['first_name'])
            print(sender)
            try:
                if 'edited_message' in item:
                    message = str(item["edited_message"]["text"]).encode('utf-8')
                else : message = str(item["message"]["text"]).encode('utf-8')
                # print(message)
            except Exception as e:
                # print(e)
                message = None
            if 'edited_message' in item: from_ = item["edited_message"]["from"]["id"]
            else : from_ = item["message"]["from"]["id"]
            reply = make_reply((demojize(str(message))).encode('utf-8'))
            if type(reply) is list:
                for i in reply:
                    bot.send_message(i, from_)
            else:
                bot.send_message(reply, from_)

