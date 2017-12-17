from flask import Flask, render_template
from mongoengine import connect
import os, configparser

config = configparser.ConfigParser()
config.read('.env')

connect(db=config.get('mongo', 'db'), host=config.get('mongo', 'host'), username=config.get('mongo', 'username'), password=config.get('mongo', 'password'), port=config.getint('mongo', 'port'))

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	port = int(os.getenv('PORT',8080))
	host = os.getenv('IP', '0.0.0.0')
	app.run(port=port, host=host)