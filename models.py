from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Dlh(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dlznik = db.Column(db.String(100), nullable=False)
    prijemca = db.Column(db.String(100), nullable=False)
    suma = db.Column(db.String(100), nullable=False)
    poznamka = db.Column(db.Text, default="")
    datum_pridania = db.Column(db.DateTime, default=datetime.utcnow)