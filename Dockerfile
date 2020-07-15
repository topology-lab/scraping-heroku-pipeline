# image from https://github.com/joyzoursky/docker-python-chromedriver/blob/master/py3/py3.7-selenium/Dockerfile

FROM python:3.8

MAINTAINER Heima K.

#WORKDIR /app

RUN export APT_KEY_DONT_WARN_ON_DANGEROUS_USAGE=1

# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y --no-install-recommends google-chrome-stable

# install chromedriver
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# User settings
ARG UID=1000
ARG USER=apluser
RUN useradd -m -u ${UID} ${USER}
# Change user
USER ${UID}

# upgrade pip
RUN pip install --upgrade pip

# install modules
RUN pip install selenium
RUN pip install beautifulsoup4
RUN pip install requests

# copy scripts
#COPY main.py /home/apluser
ADD ./script/main.py main.py
#ADD . /app

# DEBUG
RUN pwd
RUN ls -la ./
#RUN ls -la ~/  # /user/apluser
#RUN ls -la /app


# execute script
CMD ["python", "main.py"]

