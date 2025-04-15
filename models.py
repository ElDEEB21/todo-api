from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(250))
    due_date = db.Column(db.String(10))  # YYYY-MM-DD
    completed = db.Column(db.Boolean, default=False)
    priority = db.Column(db.String(10), default='medium')
