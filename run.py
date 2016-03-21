from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['debug'] = True

db = SQLAlchemy(app)
manager = Manager(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(128))
    register_time = db.Column(db.DateTime)
    topics = db.relationship("Topic", backref='user')

    def __repr__(self):
        return '<User %r>' % self.username
        
        
class Topic(db.Model):
    __tablename__ = 'topics'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    create_time = db.Column(db.DateTime)
    owner = db.Column(db.Integer, db.ForeignKey("users.id"))
    
    def __repr__(self):
        return "<Topic %r>" % self.title
        

class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(64))
    user_id = db.Column(db.Integer)
    topic_id = db.Column(db.Integer)
    create_time = db.Column(db.DateTime)
    
    def __repr__(self):
        return "<Message %r>" % self.content
        

@app.route("/user", methods=["POST", "GET"])
def user_register():
    pass        
        
if __name__ == '__main__':
    manager.run()
