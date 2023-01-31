from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return f'The current date and time is: {now}'

if __name__ == '__main__':
    app.run()
