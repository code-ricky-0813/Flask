from flask import Flask, render_template, request, redirect, jsonify, Response, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from forms import MessageForm
from datetime import datetime
import json
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'
db = SQLAlchemy(app)
Bootstrap(app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    content = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow) 

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MessageForm()
    if form.validate_on_submit():
        msg = Message(name=form.name.data, content=form.content.data)
        db.session.add(msg)
        db.session.commit()
        flash('留言成功！') 
        return redirect('/')
    messages = Message.query.order_by(Message.id.desc()).all()
    return render_template('index.html', form=form, messages=messages)

@app.route('/api/messages', methods=['GET'])
def get_messages():
    messages = Message.query.order_by(Message.id.desc()).all()
    message_list = [
        {
            "id": m.id,
            "name": m.name,
            "message": m.content,
            "timestamp": (m.timestamp + timedelta(hours=8)).strftime('%Y-%m-%d %H:%M:%S')
        }
        for m in messages
    ]
    return Response(
        json.dumps(message_list, ensure_ascii=False),
        content_type='application/json; charset=utf-8'
    )

@app.template_filter('tw_time')
def tw_time_filter(value):
    if value is None:
        return ""
    return (value + timedelta(hours=8)).strftime('%Y-%m-%d %H:%M:%S')

if __name__ == '__main__':
    app.run(debug=True)
