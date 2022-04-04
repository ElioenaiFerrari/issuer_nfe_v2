
from email import encoders
from email.mime.base import MIMEBase
import os
from dotenv import load_dotenv
import json
from flask import Flask, request, Response
from src.crawler import Crawler
import smtplib
from email.mime.multipart import MIMEMultipart
from flask_cors import CORS


load_dotenv()

app = Flask(__name__)
CORS(app, origins="*")


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/api/v2/issue', methods=['POST'])
def issue():
    user = request.json['user']
    company = request.json['company']
    note = request.json['note']
    on_done = request.json['on_done']

    crawler = Crawler(user, company, note)
    note = crawler.scrap()

    pdfname = "file.pdf"

    with open(pdfname, 'rb') as file:
        pdf = MIMEBase('application', 'pdf')
        pdf.set_payload(file.read())
        encoders.encode_base64(pdf)
        pdf.add_header('Content-Decomposition', 'attachment', filename=pdfname)

        msg = MIMEMultipart()

        msg["From"] = on_done["from"]
        msg["To"] = on_done["to"]
        msg["Subject"] = f'{on_done["collaborator"]} - {on_done["subject"]}'

        msg.attach(pdf)

        s = smtplib.SMTP(os.environ.get('MAILER_HOST'),
                         os.environ.get('MAILER_PORT'))

        s.login(os.environ.get('MAILER_USER'), os.environ.get('MAILER_PASS'))

        s.sendmail(msg['From'], msg['To'], msg.as_string())

    response = Response(
        mimetype="application/json",
        response=json.dumps(note),
        status=201
    )
    return response
