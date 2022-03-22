from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import datetime
# We need to change the title of this file to more relevant file name

app = Flask(__name__)
# When you change the file name, the the sqlite db name also to match correspondingly
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///home.db'
db = SQLAlchemy(app)

question_data = [
    {
        'question': 'How\'s the day?',
        'options': ['good', 'avg', 'bad']
    },
    {
        'question': 'How\'s yesterday?',
        'options': ['good2', 'avg', 'bad']
    },
    {
        'question': 'How\'s tomorrow?',
        'options': ['good3', 'avg', 'bad']
    }
]

length = len(question_data)


class DairyNote(db.Model):
    id = db.Column('id', db.Integer(), primary_key=True)
    date = db.Column('date', db.Date(), nullable=False, unique=True)
    note = db.Column('note', db.String(), nullable=False)

    # We can remove this function if not needed
    def __repr__(self):
        return f'DairyNote on {self.date}'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/dairy')
def dairy():
    return render_template('dairy.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/quiz')
def quiz():
    # return render_template('quiz.html', question_data=question_data, length=length)
    return render_template('quiz.html', question_data=question_data, length=length)
