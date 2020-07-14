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
- docker build -t scraping .
- docker run --name test --env-file ../line_api_key scraping
- heroku run python main.py -a scraping-st
- heroku config -a scraping-st

