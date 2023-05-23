import os
from flask import Flask, render_template, redirect, abort, request, session, flash
from flask_wtf import FlaskForm, csrf
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
# APP CONTEXT
app= Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)
app.config['CSRF_ENABLED'] = True

# TU SA NAM UKLADAJU DATA
info_list = ['test1', 'test2', 'test3']

#FORMULAR
class MojFormular(FlaskForm):
    info = StringField('Info', validators=[DataRequired(message='REQUIRED')])
    submit = SubmitField('Submit')


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
    form = MojFormular()  # ti generujeme nas formular
    app.logger.debug('FORMULAR BOL VYTVORENY')  # piseme loggeru
    if request.method == 'POST':  # iba ked je request POST
        csrf.generate_csrf()
        app.logger.debug('SPRAVA PRISLA')   # sprava z formularu prisla
        #if request.form.get('info') != '':
        if form.validate():
            print(request.form.get('info'))
            session['info'] = request.form.get('info')
            app.logger.info('INFO ULOZENA DO SESSION')
            return redirect(f'/submit')  # podakovanie
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