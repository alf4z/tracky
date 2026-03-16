import requests
from bs4 import BeautifulSoup
import schedule
import time
from telegram import Bot

TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

bot = Bot(token=TOKEN)

url = "PRODUCT_LINK"

target_price = 20000

def check_price():

    headers = {"User-Agent": "Mozilla/5.0"}

    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    price = soup.find("span", {"class": "a-price-whole"}).text
    price = int(price.replace(",", ""))

    if price < target_price:
        bot.send_message(chat_id=CHAT_ID,
                         text=f"🔥 Price dropped! Current price ₹{price}")

schedule.every(6).hours.do(check_price)

while True:
    schedule.run_pending()
    time.sleep(60)