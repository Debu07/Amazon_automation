import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL= 'https://www.amazon.in/Sony-Alpha-Mirrorless-Digital-Camera/dp/B0158SRJVQ/ref=sr_1_11?keywords=sony+dslr&qid=1568131114&s=gateway&sr=8-11'

headers={"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
def check_price():
    page=requests.get(URL,headers=headers)

    soup=BeautifulSoup(page.content,'html.parser')

    title=soup.find(id="productTitle").get_text()

    price=soup.find(id='priceblock_ourprice').get_text()
    err=price.replace("₹","")
    err_a=err.replace(",","")
    converted_price=float(err_a)

    if converted_price>150000:
        send_mail()
    print(title.strip())
    print("price:",converted_price)


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('senders_email_id@gmail.com','password@password')

    subject='Teri Kehh K Lungaaaaa !! '
    body='CHeck the amazon link:  https://www.amazon.in/Sony-Alpha-Mirrorless-Digital-Camera/dp/B0158SRJVQ/ref=sr_1_11?keywords=sony+dslr&qid=1568131114&s=gateway&sr=8-11'
    msg=f"Subject:{subject}\n\n{body}"
    server.sendmail(
        'senders_email_id@gmail.com',
        'receivers_email_id@gmail.com',
        msg
    )
    print("email sent")
    server.quit()
check_price()
