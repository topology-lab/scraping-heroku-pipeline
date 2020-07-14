# scraping-heroku-pipeline
working for Python3 on Heroku


## 目的
Docker学習ついでにPythonも触ってみる。
機能はスクレイピング。

## 動作環境
開発時はローカルで動かせるようにDockerコンテナで。
リリース時はHerokuで。

### Heroku
Schedulerのみ。無料で動かす。

## Heroku用の環境構築
LINEへの通知トークンを、以下の環境変数に設定する。
LINE_NOTIFY_TOKEN=****

## メモ
docker build -t scraping .
docker run --name test --env-file ../line_api_key scraping


