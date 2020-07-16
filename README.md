# scraping-heroku-pipeline
working for Python3 on Heroku


## 目的
Docker学習ついでにPythonも触ってみる。
機能はスクレイピング。

## 動作環境
開発時はローカルで動かせるようにDockerコンテナで。
ステージング、プロダクト環境はHerokuで。

## Heroku
試しにpipelineを使ってみる。
python main.pyでしか動かすつもりもないので、URLからアクセスしてみ意味ない。
addonはSchedulerのみ。

## 環境構築
- Heroku
LINEへの通知トークンを環境変数に設定する。
```
heroku config:set LINE_NOTIFY_TOKEN=**** -a app-name
```

- ローカル
ファイルに「LINE_NOTIFY_TOKEN=****」書いて、docker実行時にオプションで指定する。

## メモ
- Heroku用dockerコマンドから実行
  - docker build -t scraping .
  - docker run --name test --env-file ../line_api_key scraping
- Herokuステージング環境での動作確認
  - heroku run python main.py -a scraping-st
  - heroku config -a scraping-st
- docker-composeで実行環境引数指定しつつ
  - docker-compose --env-file ../line_api_key up -d
- image掃除
  - docker rmi `docker images -aq`

## Update
- 2020/07/15
  - docker-compose使ってpython、selenium、chromeを別に構築するサンプルがあったので、そっちに変更
    - https://github.com/sikkimtemi/selenium
  - なんでseleniumとHEADLESSブラウザが使われるのかわかっていなかったが理解できた。
    - よくあるのだとログイン処理とかを実装できるからselenium使ってるっぽい。
      - 試しているColumbiaのECだと、色とかサイズとかによって在庫状況が変わるので、狙ったアイテムを選択する処理をseleniumで実装すればよりやりたいことが実現できると思われる。
    - pythonでrequest.getってやってもJavascriptが動かないので表示されないリソースが多い。それをHEADLESSブラウザが解決してくれるっぽい。
      - 試しているサイトだと、商品情報はまるっと初期表示後に取得してるっぽくて、header/footer以外の商品情報は取れていなかった。
  - 環境変数に「DEBUG=1」が設定されているかどうかで実行環境（docker-compose or Heroku）を判断するようなロジックを追加したけど、やっつけな気がしてならない。インフラの制約がアプリに実装されるのが良くない印象。
- 2020/07/16
  - docker、docker-composeで作られるコンテナの棲み分けが自分の中で整理できていなかったと考え直した。次の目的として作り直す予定。
    - docker：pythonイメージに諸々pip installされた環境。ほぼHeroku環境（/app配下に全ファイルがデプロイされている）っぽい構成。
    - docker-compose：必要な環境（Python/Chrome HEADLESS/selenium）が別コンテナとして作成される、Dockerで有るべき姿っぽい構成。
  - とりあえずスクレイピング機能の部分は今の実装で良しとする。これ以上作り込んでもライブラリ（BeautifulSoup）の機能確認にしかならなそう。
