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
