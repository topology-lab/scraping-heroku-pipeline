FROM python:3.8

# vimとseleniumをインストール
RUN set -x && \
  apt-get update && \
  apt-get install -y vim && \
  pip install --upgrade pip && \
  pip install selenium && \
  pip install beautifulsoup4 && \
  pip install requests
