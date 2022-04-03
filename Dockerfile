FROM python:3.9


WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . . 

EXPOSE 80

CMD ["flask", "run", "--port=80"]