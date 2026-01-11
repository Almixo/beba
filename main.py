from flask import Flask, render_template, redirect, url_for, flash, request
from werkzeug.utils import secure_filename
from uuid import uuid4
import os

from datetime import datetime

from random import randint

from secret import ReturnDlhText

from forms import DlzbyForm
from models import db, Dlh

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sigma67420'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dlzby.db'

db.init_app(app)

#Vytvorenie DB pri prvom spustení
with app.app_context():
    db.create_all()

@app.route("/odstranit/<int:id>")
def odstranit(id):
    uloha = Dlh.query.get_or_404(id)
    db.session.delete(uloha)
    db.session.commit()
    return redirect(url_for("zobraz_dlhy"))

@app.route('/', methods=['GET','POST'])
def home_page():
    dlzby = Dlh.query.order_by(Dlh.datum_pridania.asc()).all()
    return render_template('index.html', dlzby=dlzby)

@app.route('/zobraz_dlhy', methods=['GET','POST'])
def zobraz_dlhy():
    dlzby = Dlh.query.order_by(Dlh.datum_pridania.asc()).all()
    return render_template('zobraz_dlhy.html', dlzby=dlzby, txt=ReturnDlhText())

@app.route('/pridaj_dlh', methods=["GET","POST"])
def pridaj_ulohu():
    form = DlzbyForm()
    if form.validate_on_submit():
        dlh = Dlh(
            dlznik = form.dlznik.data,
            prijemca = form.prijemca.data,
            suma = form.suma.data,
            poznamka = form.poznamka.data
        )
        
        db.session.add(dlh)
        db.session.commit()
        return redirect(url_for('zobraz_dlhy'))

    return render_template('pridaj_dlh.html', form=form, txt=ReturnDlhText())