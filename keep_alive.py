# Code that keeps the bot alive by connecting it to the uptimerobot site (https://uptimerobot.com/)
# DO NOT mess with this file
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Hello. I am alive!" # If bot is online, lets us know 

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()