import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


url = "https://www.columbiasports.co.jp/items/col/CU0134/"

# データ取得
resp = requests.get(url)
#print(resp.text)

soup = BeautifulSoup(resp.content, "html.parser")
#print(soup.title)
buttons = soup.find_all("button") 
#print(buttons)
for button in buttons:
    print(button.get_text())

message = soup.select_one("button.nostock")
print("button.nostock=")
print(message)

b = soup.find('div', class_="button")
print("div.button=")
print(b)
message = b


# ローカルに保存しているChrome Driverを指定(※デプロイするときはコメントアウトする)
#driver_path = '/usr/local/bin/chromedriver'

# Heroku上のChrome Driverを指定(※デプロイするときはコメントを外す)
# driver_path = '/app/.chromedriver/bin/chromedriver'

# Headless Chromeをあらゆる環境で起動させるオプション
#options = Options()
#options.add_argument('--disable-gpu');
#options.add_argument('--disable-extensions');
#options.add_argument('--proxy-server="direct://"');
#options.add_argument('--proxy-bypass-list=*');
#options.add_argument('--start-maximized');
#options.add_argument('--headless');

# クローラーの起動
#driver = webdriver.Chrome(executable_path=driver_path, chrome_options=options)

# Yahooの天気サイトにアクセス
#driver.get('https://weather.yahoo.co.jp/weather/')

# ソースコードを取得
#html = driver.page_source

# ブラウザを終了する
#driver.quit()

# HTMLをパースする
#soup = BeautifulSoup(html, 'lxml') # または、'html.parser'

# スクレイピングした《今日の日本の天気予報の要約》を変数に格納
#message = soup.select_one('#condition > p.text').get_text()

# LINEに通知させる関数
def line_notify(message):
    # LINE通知トークンの取得
    line_notify_token = os.environ['LINE_NOTIFY_TOKEN']
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {line_notify_token}'}
    data = {'message': f'message:{message}'}
    requests.post(line_notify_api, headers=headers, data=data)

# LINEに通知させる
line_notify(message)
