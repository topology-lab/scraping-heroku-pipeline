import os
import requests
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

url = "https://www.columbiasports.co.jp/items/col/CU0134/"

# データ取得
#resp = requests.get(url)
#print(resp.text)
#
#soup = BeautifulSoup(resp.content, "html.parser")
#print(soup.title)
#buttons = soup.find_all("button") 
#for button in buttons:
#    print(button.get_text())
#
#print("========")


# LINEに通知させる関数
def line_notify(message):
    # LINE通知トークンの取得
    line_notify_token = os.environ['LINE_NOTIFY_TOKEN']
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {line_notify_token}'}
    data = {'message': f'{message}'}
    requests.post(line_notify_api, headers=headers, data=data)


# docker-composeによる環境か、Herokuかを環境変数で切り替える。
# やり方として良いとは考えていない。
def get_browser():

    if  "DEBUG" in os.environ:
        # docker-compose setting
        return webdriver.Remote(
            command_executor='http://selenium-hub:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)
    else:
        # Heroku settings
        # Heroku上のChrome Driverを指定(※デプロイするときはコメントを外す)
        driver_path = '/app/.chromedriver/bin/chromedriver'
        
        # Headless Chromeをあらゆる環境で起動させるオプション
        options = Options()
        #options.add_argument('--disable-gpu');
        #options.add_argument('--disable-extensions');
        #options.add_argument('--proxy-server="direct://"');
        #options.add_argument('--proxy-bypass-list=*');
        #options.add_argument('--start-maximized');
        options.add_argument('--headless');

        return webdriver.Chrome(
            executable_path=driver_path,
            options=options)


if __name__ == '__main__':
    try:
        #browser = webdriver.Firefox()  # 普通のFilefoxを制御する場合
        #browser = webdriver.Chrome()   # 普通のChromeを制御する場合

        # HEADLESSブラウザに接続
        browser = get_browser()

        # Googleで検索実行
        browser.get(url)

        # 検索結果取得
        html = browser.page_source

        # HTMLをパースする
        soup = BeautifulSoup(html, 'html.parser') # または、'lxml'

        # DEBUG
        buttons = soup.find_all('button')
        for b in buttons:
            print("Web在庫" in b.text)

        print(soup.select_one('button.active') is None)

        # スクレイピングした購入ボタンのテキストを取得
        message = soup.select_one('button.nostock').get_text()
        message = soup.select_one('button.active')

        if soup.select_one('button.active') is None:
            print(soup.select_one('button.nostock').get_text())
        else:
            # LINEに通知させる
#            line_notify(message)
            print(message)

    finally:
        # 終了
        browser.close()
        browser.quit()
