from bs4 import BeautifulSoup
import requests

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

#####         Option 1
def stock_prices():
    url = 'https://www.moneycontrol.com/stocksmarketsindia/'
    source = requests.get(url, headers).text

    soup = BeautifulSoup(source, 'html.parser')
    sect = soup.find_all('div',class_='sectoral_indices')
    # print(sect)
    sect1 = soup.find('div',class_='sectoral_tablebx')
    table = sect1.find('table',class_='mctable1')
    # print(table)
    stock_price_msg = "%-17s%-17s%-17s%-17s"%('INDEX','VALUE','CHNG','%CHNG')
    stock_price_msg += '\n'+len(stock_price_msg)*'-'
    
    for row in table.find_all('tr'):
        for cell in row.find_all('td'):
            stock_price_msg += '%-17s' % (cell.text)
        stock_price_msg+='\n'
        
    stock_price_msg = stock_price_msg.replace('&','n')
    return stock_price_msg

##############      option 2

def facts():
    facts_ = '1. Bombay Stock Exchange (BSE) is the biggest stock exchange in the world in terms of the number of listed companies on an exchange. BSE has over 5,500 listed companies.\n\n\
2. BSE is also the oldest stock exchange in Asia. It was established in 1875.\n\n\
3. The participation of the common people in Indian share market is below a satisfactory level. Less than 2.5% population of India invest in the market.\n\n\
4. When master blaster used to play international cricket, his dismissal adversely affected the Indian stock market.\n\n\
5. The costliest share in the Indian share market is MRF. It costs Rs 69,290 to buy 1 share of MRF.\n\n\
6. There is total of 23 stock exchanges in India.\n\n\
7. Nifty has given a return of 11.32 percent p.a. since its inception [till Nov’2017]: The base value of nifty was 1,000 in 1995. Recently nifty crosses 10k mark and it is currently at 10,360 points.'
    return facts_

##############      option 3
def gold_price():
    gold_url = 'https://www.goodreturns.in/gold-rates/'
    source_of_gold = requests.get(gold_url, headers).text
    reply_gold = ""
    try:
        gold_soup = BeautifulSoup(source_of_gold,'lxml')
        gold_table = gold_soup.find_all('div',class_='gold_silver_table')
        gold_table_22cr = gold_table[0]
        reply_gold = '\tPrice of 22 Carat Gold\n\n'
        reply_gold1= '%-15s%-15s%-15s%-15s'%('GRAM','22Cr Today','22Cr Yesterday','PriceChng')
        reply_gold += reply_gold1+'\n'+len(reply_gold1)*'-'+'\n'
        i =0
        for row in gold_table_22cr.find_all('tr'):
            if i== 0:
                i+=1
                continue
            for cell in row.find_all('td'):
                reply_gold += '%-15s' % (cell.text).replace('\n','')
            reply_gold += '\n'
        gold_table_24cr = gold_table[1]
        reply_gold += '\n\n\tPrice of 24 Carat Gold \n\n'
        reply_gold2 = '%-15s%-15s%-15s%-15s'%('GRAM','24Cr Today','24Cr Yesterday','PriceChng')
        reply_gold += reply_gold2+'\n'+len(reply_gold2)*'-'+'\n'
        i = 0
        for row in gold_table_24cr.find_all('tr'):
            if i== 0:
                i+=1
                continue
            for cell in row.find_all('td'):
                reply_gold += '%-15s' % (cell.text).replace('\n','')
            reply_gold +='\n'

    except Exception as e:
        print(e)
    return reply_gold

########   option 3
def silver_price():
    #for silver
    silver_url = 'https://www.goodreturns.in/silver-rates/'
    try:
        source_of_silver = requests.get(silver_url, headers).text
        reply_silver = ""
        silver_soup = BeautifulSoup(source_of_silver,'lxml')
        silver_table = silver_soup.find_all('div',class_= 'gold_silver_table')[0]
        reply_silver = '\tPrice of Silver\n\n'
        reply_silver1 = '%-15s%-15s%-15s%-15s'%('GRAM','Rate Today','Rate Yesterday','PriceChng')
        reply_silver += reply_silver1+'\n'+len(reply_silver1)*'-'+'\n'
        i = 0
        for row in silver_table.find_all('tr'):
            if i== 0:
                i+=1
                continue
            for cell in row.find_all('td'):
                reply_silver += '%-15s' % (cell.text).replace('\n','')
            reply_silver += '\n'

    except Exception as e:
        print(e)

    return reply_silver

##########   option 4
def dollar_price():
    url = 'http://www.moneycontrol.com/currency/bse-usdinr-price.html'
    source = requests.get(url, headers).text
    reply = ""
    try:
        soup = BeautifulSoup(source, 'lxml')
        dollar = soup.find('span', class_ = 'gr_20').strong.text
        change = soup.find('span', class_ = 'gr_14').text
        reply = "The Price of one dollar is ₹{} \nChange is ₹{}".format(dollar,change)
    except Exception as e:
        print(e)
    return reply

########### option 5
def petrol_price():
    url = 'https://www.goodreturns.in/petrol-price.html'
    reply = ''
    try:
        source = requests.get(url, headers)
        soup = BeautifulSoup(source.content, 'lxml')
        table = soup.find_all('div', class_ = 'gold_silver_table')[0]
        reply = 'P E T R O L   P R I C E S\n\n'
        reply1 = "%-15s%-15s%-15s"%('City','TodayPrice',"YesterdayPrice")+"\n"
        reply = reply + reply1 + "-"*len(reply1) + '\n'
        i = 0
        for row in table.find_all('tr'):
            if i == 0:
                i+=1
                continue
            for cell in row.find_all('td'):
                reply += '%-15s' % (cell.text).replace('\n','')
            reply  += '\n'

    except Exception as e:
        print(e)

    return reply

#########    Option 6
def diesel_price():
    url = 'https://www.goodreturns.in/diesel-price.html'
    reply = ''
    try:
        source = requests.get(url, headers)
        soup = BeautifulSoup(source.content, 'lxml')
        table = soup.find_all('div', class_ = 'gold_silver_table')[0]
        reply = 'D I E S E L   P R I C E S\n\n'
        reply1 = "%-15s%-15s%-15s"%('City','TodayPrice',"YesterdayPrice")+"\n"
        reply = reply + reply1 + "-"*len(reply1) + '\n'
        i = 0
        for row in table.find_all('tr'):
            if i == 0:
                i+=1
                continue
            for cell in row.find_all('td'):
                reply += '%-15s' % (cell.text).replace('\n','')
            reply  += '\n'

    except Exception as e:
        print(e)

    return reply

########  Option 7
def corona_tracker():
    #for world
    url = 'https://www.worldometers.info/coronavirus/'
    source = requests.get(url, headers)
    soup = BeautifulSoup(source.content,'lxml')
    reply = 'Corona Virus Data\n'+'-'*30+'\n'+'World :earth_africa: \n'
    cases_tally = soup.find_all('div',id='maincounter-wrap')
    for i in range(3):
        reply += cases_tally[i].h1.text+' '+cases_tally[i].find('div',class_='maincounter-number').span.text+'\n'
    reply += '\nActive Cases\n'
    cases_tally = soup.find('div',class_='panel-body')
    for i in range(1):
        reply += cases_tally.div.text[:109]
    reply +='\n*Updates in every 20 minutes'
    #for India
    url_ind = 'https://www.worldometers.info/coronavirus/country/india/'
    source = requests.get(url_ind, headers)
    soup = BeautifulSoup(source.content,'lxml')
    reply_ind = 'Corona Virus Data\n'+'-'*30+'\n'+'India :india \n'
    cases_tally = soup.find_all('div',id='maincounter-wrap')

    for i in range(3):
        reply_ind += cases_tally[i].h1.text+' '+cases_tally[i].find('div',class_='maincounter-number').span.text+'\n'
    reply_ind += '\nActive Cases\n'
    cases_tally = soup.find('div',class_='panel-body')
    for i in range(1):
        reply_ind += cases_tally.div.text[:96]
    reply_ind +='\n*Updates in every 20 minutes'
    return reply,reply_ind























