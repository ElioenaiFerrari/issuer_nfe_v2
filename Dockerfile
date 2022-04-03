FROM python:3.9

WORKDIR /app

RUN apt-get install -yqq unzip curl
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/100.0.4896.60/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . . 

ENV FLASK_APP=main.py
ENV FLASK_ENV=production

CMD ["flask", "run", "--port=3000", "--host=0.0.0.0"]