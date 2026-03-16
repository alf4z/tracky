import requests
from bs4 import BeautifulSoup
import schedule
import time
import telegram

TOKEN = "8632230189:AAE8ViNDOosEhHSfWC1582q868vJYNEQcJQ"
CHAT_ID = "468978056"

bot = telegram.Bot(token=TOKEN)

url = "https://www.amazon.in/Ant-Esports-MK1300-Mini-Mechanical/dp/B09GG2YVWH"

def send_price():

    print("Checking price...")

    headers = {"User-Agent": "Mozilla/5.0"}

    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    price_tag = soup.find("span", {"class": "a-price-whole"})

    if price_tag:
        price = price_tag.text.strip()
    else:
        price = "Price not found"

    message = f"""
🍥 Hey Alfaz,

📦 Product Price Update

Current Price: ₹{price}

Checked Automatically Today
"""

    bot.send_message(chat_id=CHAT_ID, text=message)

    print("Message sent!")

# run once immediately for testing
send_price()

print("Bot started...")

schedule.every(1).minutes.do(send_price)

while True:
    print("Checking schedule...")
    schedule.run_pending()
    time.sleep(10)
