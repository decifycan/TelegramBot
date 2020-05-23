from bot import telegram_chatbot
from emoji import emojize,demojize
##import telegram

bot = telegram_chatbot("config.cfg")
import stocks_price
# print(bot.token)
update_id = None

def make_reply(msg):
    if msg is not None:
        msg = msg.decode('utf-8')[2:-1]
        reply = "Hey there! \nManjaro here."
        menu = "\nThis is how can I help! Reply num of choice\n\n :one: Stock Indexes:chart:\n\n :two: Stock Mkt Facts:yum: \n\n :three: Gold and Silver Price \n\n :four: Dollar:heavy_dollar_sign: Price\n\n :five: Petrol Prices :fuel_pump: \n\n :six: Diesel Prices :fuel_pump:\n\n :seven: Corona Cases \n\n*__Hosted on Ishan's PC__ Apologies if you experience latency."
        print(msg)
        try:
            if msg.isnumeric() or msg =='/start':
                if msg == '/start':
                    return [reply, emojize(menu,use_aliases=True)]
                elif int(msg) == 1:
                    reply = stocks_price.stock_prices()
                elif int(msg) == 2:
                    reply = stocks_price.facts()
                elif int(msg) == 3:
                    return [stocks_price.gold_price(), stocks_price.silver_price()]
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
                    return [emojize("You have not read menu properly :bangbang:",use_aliases=True),emojize(menu,use_aliases=True)]
            else:
                return [emojize("You have not read menu properly :bangbang:",use_aliases=True),emojize(menu,use_aliases=True)]
        except Exception as e:
            print(e)
            return [emojize('FATAL issues occured will be back :soon:. This has been reported to admin. Till then try other option',use_aliases=True),emojize(menu,use_aliases=True)]
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

