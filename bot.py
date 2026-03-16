import requests
from bs4 import BeautifulSoup
import schedule
import time

TOKEN = "8632230189:AAE8ViNDOosEhHSfWC1582q868vJYNEQcJQ"
CHAT_ID = "468978056"

url = "https://www.amazon.in/Ant-Esports-MK1300-Mini-Mechanical/dp/B09GG2YVWH"

def send_price():

    headers = {"User-Agent": "Mozilla/5.0"}

    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    price_tag = soup.select_one(".a-price-whole")

    if price_tag:
        price = price_tag.text.strip()
    else:
        price = "Price not found"

    message = f"""
📦 Product Price Update

Current Price: ₹{price}
"""

    telegram_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": message
    }

    requests.post(telegram_url, data=data)

    print("Message sent!")

# run once for testing
send_price()

schedule.every(1).minutes.do(send_price)

while True:
    schedule.run_pending()
    time.sleep(10)
