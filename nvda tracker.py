import time
import warnings

from time import sleep



warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas
from yahoo_fin.stock_info import *
from email.message import EmailMessage
import smtplib
import ssl
NP = get_live_price("NVDA")
email_sender = 'xenivixtyx@gmail.com'
email_password = 'wjgq hfpc ozcu hxdu'
print("Please type recipietent email")
email_receiver = input()

subject = 'ALERT NVDA PRICE CAHNGE'
body = (f"NVIDIA PRICE IS NOW {NP}")



em = EmailMessage()
em['From'] = email_sender
em['To'] = email_sender
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
start2 = True
start = True


print("select market ticker")
ticker = input()

print("type lower bound")
lowerBound1 = input()

print("type upper bound")
upperBound1 = input()

if not upperBound1.isnumeric():
    print("sorry your upper bound is not a valid number")
    exit()

if not lowerBound1.isnumeric():
    print("sorry your lower bound is not a valid number")
    exit()




lowerBound = int(lowerBound1)
upperBound = int(upperBound1)

while start == True:
    print(get_live_price(ticker))
    if get_live_price(ticker) > upperBound:
        start = False
    else:
        if get_live_price(ticker) < lowerBound:
         start = False
        else:
            if get_live_price(ticker) < lowerBound == False:
                if get_live_price(ticker) > upperBound == False:
                    start = True


while start2 == True:
    if get_live_price(ticker) > upperBound:
        start2 = True
        subject = (f'ALERT {ticker} PRICE RAISE CHANCE TO SELL')
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
            print("SENT", get_live_price(ticker))
            sleep(5)


    else:
        if get_live_price(ticker) < lowerBound:
            subject = (f'ALERT {ticker} PRICE DROP CHANCE TO BUY')
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_receiver, em.as_string())
                print("SENT LOWER", get_live_price(ticker))
                sleep(5)
        else:
            start2 = False

