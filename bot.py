import requests
from bs4 import BeautifulSoup
import schedule
import time
import telegram

TOKEN = 8632230189:AAFF2bXQxoGV3bnj9hr1fzFbpvOYisVEE5w
CHAT_ID = 7463999147

bot = telegram.Bot(token=TOKEN)

url = "https://www.amazon.in/Ant-Esports-MK1300-Mini-Mechanical/dp/B09GG2YVWH/ref=sr_1_7?crid=39A5VJGSRYE5E&dib=eyJ2IjoiMSJ9.DPDadPwftyQZoNEiixRRqKXx7ES8AVGqR-0QPLRk8ccIx-4bgkhaqWa6AlnIlOZ8TV6fHeo-HYEwYwyrFTGIBh8nq5tNUZt-BZpU6zYx5af2VGFUiGIFLuOWZCGBrzYcJ2PdmbPvedNZ8UVn8a5Z9TmfLGk5B92m7S6BsjBO-mcJ0PTPDwwuELdQbZOO8ff9b5jjOVN40Qv0EFkTyPXmC_MoYFDP826QrzhXKSyNcYI.Yb5Zk4LQv4WqcprqSkHJg5dhrKXVUpyKlSO1o0IUlDQ&dib_tag=se&keywords=ant+esports+mechanical+keyboard&nsdOptOutParam=true&qid=1773654958&sprefix=ant+%2Caps%2C465&sr=8-7"

def send_price():

    headers = {"User-Agent": "Mozilla/5.0"}

    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    price = soup.find("span", {"class": "a-price-whole"}).text

    message = f""""
    🍥Hey Alfaz,
    
📦 Product Price Update

Current Price: ₹{price}

Checked Automatically Today
""""

    bot.send_message(chat_id=CHAT_ID, text=message)


# run once per day
schedule.every(1).minutes.do(send_price)

while True:
    schedule.run_pending()
    time.sleep(60)
