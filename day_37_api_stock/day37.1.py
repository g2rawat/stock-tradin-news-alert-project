import requests as rq
import smtplib as smt
import datetime as dt
import pandas as pd
today_date=str(dt.datetime.today()).split()[0]
yes_date=str(dt.datetime.today()-dt.timedelta(days=1)).split()[0]

market_api="https://www.alphavantage.co/query?"
news_api="https://newsapi.org/v2/everything"

market_key="501WBMHPJW9ZZNM6"
news_key="f509b6f54c10482a924f0b92969baea8"

req_news={
    "q":"zomato",
    "language":"en",
    "from":today_date,
    "sortBy":"popularity",
    "apiKey":news_key
}

name_stk="ZOMATO.BSE"

# req_crypto_market={
#     "function":"DIGITAL_CURRENCY_DAILY",
#     "symbol":name_stk,
#     "market":"INR",
#     "apikey":"key"
# }

req_stock_market={
    "function":"TIME_SERIES_DAILY",
    "symbol":name_stk,
    "apikey":market_key
}




# ____________________________________for crypto_________________________________________________________

# sim=rq.get(market_api,params=req_crypto_market)
# kim=sim.json()

# name=kim["Meta Data"]["3. Digital Currency Name"]
# date=kim["Meta Data"]["6. Last Refreshed"]
# dt_obj = dt.datetime.strptime(date, '%Y-%m-%d %H:%M:%S').strftime("%d/%b/%Y(%a)")
# # new_date=dt.datetime.strptime(date, "%Y-%m-%d").date()
# # new_date1=f"{new_date.month}/{new_date.day}/{new_date.year}"
# today_open=float(kim["Time Series (Digital Currency Daily)"][today_date]["1a. open (INR)"])
# today_close=float(kim["Time Series (Digital Currency Daily)"][today_date]["4a. close (INR)"])
# # yesturday_close=float(kim["Time Series (Digital Currency Daily)"]["2022-09-14"]["4.a close (INR)"])
# cal=round((abs(today_close-today_open)/today_open)*100,2)
# if today_open>today_close:
#     state="🔻"
# elif today_open==today_close:
#     state="💚"
# else:
#     state="🔺"
# print(
#     f"Date:{dt_obj}\nCompany: {name}\
#         \nOpen: {today_open}\nClose:{today_close}\
#         \nStatus:{cal}%{state}"
#     )

# for n in range(5):
#     news=rq.get(news_api,req_news)
#     news_p=news.json()["articles"][n]["title"]
#     print(news_p)


# _______________________________________us & indian market______________________________________________________

sim=rq.get(market_api,params=req_stock_market)
kim=sim.json()

name=kim["Meta Data"]["2. Symbol"]
# print(kim["Meta Data"])
print(name)
date=kim["Meta Data"]["3. Last Refreshed"]
dt_obj = dt.datetime.strptime(date, '%Y-%m-%d').strftime("%d/%b/%Y(%a)")

today_open=float(kim["Time Series (Daily)"][yes_date]["1. open"])
today_close=float(kim["Time Series (Daily)"][yes_date]["4. close"])
# yesturday_close=float(kim["Time Series (Daily)"]["2022-09-14"]["4. close"])
cal=round(((today_close-today_open)/today_open)*100,2)
if cal<0:
    state="🔻"
    cal=cal*(-1)
else:
    state="🔺"
print(
    f"Date:{dt_obj}\nCompany: {name}\
        \nOpen: {today_open}\nClose:{today_close}\
        \nStatus:{cal}%{state}"
    )


news=rq.get(news_api,req_news)
news_p=news.json()["articles"][:5]
# for m in news_p:
    # print(m["title"])
    # print(m["description"])
# print(news_p)
if cal>2:
    format_article=[f"\nHeadline:{m['title']}.\n Brief: {m['description']} " for m in news_p]
    # for z in format_article:
    #     print(z)


# print(format_article)
mail="g2jeetusuck@gmail.com"
password="ykotdrxhzdckschc"
with smt.SMTP("smpt.gmail.com") as send:
    send.starttls()
    send.login(mail)
    send.sendmail(
        from_addr=mail,
        to_addrs="rawabhi07@gmail.com",
        msg=f"subject:ZOMATO stock price\n\n{format_article}\n\nYou get Stock related NEWS only when volatility is more than 2%"
        )

#run this code on python anywhere from Tuesday to Saturday (Saturday and Sunday market closed)