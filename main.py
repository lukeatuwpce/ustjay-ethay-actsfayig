#!/usr/bin/env python3

from bs4 import BeautifulSoup
from flask import Flask
import requests
import os

app = Flask(__name__)

@app.route('/')
def get_pig_latin_quote():
    response = requests.get("http://unkno.com/")

    soup = BeautifulSoup(response.content, "html.parser")
    quotes = soup.find_all("div", id="content")

    quote = quotes[0].getText().strip()

    post_args = { "input_text" : quote }
    esponsray = requests.post("https://hidden-journey-62459.herokuapp.com/piglatinize/", data=post_args)
    oupsay = BeautifulSoup(esponsray.content, "html.parser")
    oatquay = oupsay.find("h2").next_sibling.strip()

    return oatquay

if __name__ == "__main__":
    port = int(os.environ.get(('PORT'), 6738))
    app.run(host='0.0.0.0', port=port)

