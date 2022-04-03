
from dotenv import load_dotenv
import json
from flask import Flask, request, Response
from src.crawler import Crawler

load_dotenv()

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/api/v2/issue', methods=['POST'])
def issue():
    user = request.json['user']
    company = request.json['company']
    note = request.json['note']

    crawler = Crawler(user, company, note)
    note = crawler.scrap()

    response = Response(
        mimetype="application/json",
        response=json.dumps(note),
        status=201
    )
    return response
