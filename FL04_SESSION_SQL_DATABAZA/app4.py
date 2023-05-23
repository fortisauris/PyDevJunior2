import os
import json
from flask import Flask, render_template, redirect, abort, request, session, flash
from flask_wtf import FlaskForm, csrf
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_session import Session
import sqlite3  # importujeme priopojenie do databazy sqlite3
# APP CONTEXT
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)
app.config['CSRF_ENABLED'] = True

app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = False
Session(app)   # tu vznika velka session

# TU SA NAM UKLADAJU DATA
info_list = ['test1', 'test2', 'test3']  # spomienka na app1

#FORMULAR
class MojFormular(FlaskForm):
    info = StringField('Info', validators=[DataRequired(message='REQUIRED')])
    submit = SubmitField('Submit')

DATABASE = 'appdb.db'

def add_record(info):  #
    with sqlite3.connect(DATABASE) as db:  # pripojime sa
        cur = db.cursor()  #

        sql_cmd = ' INSERT INTO info VALUES(?,?) '  # prikaz SQL
        data = (1, info)  # tu si pripravime data
        cur.execute(sql_cmd, data)   # vykoname prikaz
        db.commit()  # ulozime
        return True




# ROUTES
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/setsession')
def setsession():
    session['USERNAME'] = 'Anonymous'
    flash('USERNAME JE NASTAVENE')
    app.logger.debug('USERNAME JE NASTAVENE')
    return redirect('/index')

@app.route('/getsession')
def getsession():
    if 'USERNAME' in session:
        username = session['USERNAME']
        msg = f'SESSION FOR USER : {username} WAS ACCESED'
        flash(msg)
        app.logger.info(msg)
        return redirect('/index')
    else:
        return 'WELCOME GUEST'

@app.route('/delsession')
def delsession():
    session.pop('USERNAME', None)
    flash('SESSION BOLA VYMAZANA')
    app.logger.debug('SESSION BOLA VYMAZANA')
    return redirect('/index')


@app.route('/info', methods=['GET', 'POST'])
def info():
    form = MojFormular()
    app.logger.debug('FORMULAR BOL VYTVORENY')
    if request.method == 'POST':
        csrf.generate_csrf()
        app.logger.debug('SPRAVA PRISLA')
        #if request.form.get('info') != '':
        if form.validate():
            print(request.form.get('info'))
            session['info'] = request.form.get('info')
            # FIRST
            #with open(file='session_info.json', mode='a', encoding='utf8') as f:  # <- Tu to ukladamae do jsonu
            #    json.dump(fp=f, obj=session, indent=4)
            add_record(session['info'])
            app.logger.info('INFO ULOZENA DO SESSION')
            return redirect(f'/submit')
        else:
            app.logger.info('INFORMACIA NEBOLA ULOZENA')

    return render_template('info.html', form=form)

@app.route('/submit', methods=['GET'])
def submit():
    return render_template('submit.html')

@app.route('/view', methods=['GET'])
def infolist():
    try:
        entry = str(session['info'])
        app.logger('SPRAVA')
        flash('Info je v poriadku')
    except KeyError:
        entry=None
        flash('Nemam info')
    finally:
        return render_template('view.html', entry=entry)

if __name__ == '__main__':
    app.run(debug=True)