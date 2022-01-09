from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://dataforms.db'
db = SQLAlchemy(app)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# sanity check route
@app.route('/', methods=['GET'])
def hello():
    return jsonify('respondiendo desde el servidor de flask')

# @app.route('/')
# def home():
#     return render_template('sutmit.html')

@app.route('/sutmit', methods=['GET', 'POST'])
def sutmit():
    _name ='francisco'
    _email = 'cisco@gmail.com'
    _sex = 'Male'
    _time_tiktok = 0
    _time_whatsapp = 2
    _time_twitter = 1
    _time_instagram = 4
    _time_facebook = 3

    sqlite = "INSERT OR REPLACE INTO users VALUES (?,?,?,?,?,?,?,?);"
    data = (_name, _email, _sex, _time_tiktok, _time_whatsapp,
            _time_twitter, _time_instagram, _time_facebook)
    conn =sqlite3.connect('dataforms.db')
    c = conn.cursor()
    c.execute(sqlite, data)
    conn.commit()

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug = True, host='localhost', port='5000')
