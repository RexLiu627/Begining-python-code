import time
import warnings
from time import sleep

warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas
from yahoo_fin.stock_info import *
import requests_html#
from email.message import EmailMessage
import smtplib
import ssl
NP = get_live_price("NVDA")
email_sender = 'xenivixtyx@gmail.com'
email_password = 'wjgq hfpc ozcu hxdu'
email_receiver = 'rexliu627@gmail.com'

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
start3 = True
Roblox = get_live_price("RBLX")

while start == True:
    print(get_live_price("NVDA"))
    if get_live_price("NVDA") > 120:
        start = False
    else:
        if get_live_price("NVDA") < 110:
         start = False
        else:
            if get_live_price("NVDA") < 110 == False:
                if get_live_price("NVDA") > 120 == False:
                    start = True


while start2 == True:
    if get_live_price("NVDA") > 120:
        if get_live_price("NVDA") < 110 == False:

            start2 = True
            subject = 'ALERT NVDA PRICE RAISE CHANCE TO SELL'
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
             smtp.login(email_sender, email_password)
             smtp.sendmail(email_sender, email_receiver, em.as_string())
             print("SENT",get_live_price("NVDA"))
             sleep(5)
    else:
        start2 = False

while start3 == True:
    if get_live_price("NVDA") < 110:
        subject = 'ALERT NVDA PRICE DROP CHANCE TO BUY'
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
             smtp.login(email_sender, email_password)
             smtp.sendmail(email_sender, email_receiver, em.as_string())
             print("SENT LOWER",get_live_price("NVDA"))
             sleep(5)

