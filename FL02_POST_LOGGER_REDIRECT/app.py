import os
from flask import Flask, render_template, redirect, abort, request
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
'''
@app.route('/info', methods=['GET', 'POST'])
def info():
    if request.method == 'POST':
        print(request.form.get('info'))
        info_list.append(request.form.get('info'))
        app.logger.info('INFO ULOZENA')
    form = MojFormular()
    app.logger.debug('FORMULAR BOL VYTVORENY')
    return render_template('info.html', form=form)

# Prestavka do 20:10

@app.route('/info', methods=['GET'])
def info_get():
    form = MojFormular()
    app.logger.debug('FORMULAR BOL VYTVORENY')
    return render_template('info.html', form=form)

@app.route('/info', methods=['POST'])
def info_post():
    if request.method == 'POST':
        print(request.form.get('info'))
        info_list.append(request.form.get('info'))
        app.logger.info('INFO ULOZENA')
        return redirect(f'/submit')
'''

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
            info_list.append(request.form.get('info'))
            app.logger.info('INFO ULOZENA')
            return redirect(f'/submit')
        else:
            app.logger.info('INFORMACIA NEBOLA ULOZENA')

    return render_template('info.html', form=form)

@app.route('/submit', methods=['GET'])
def submit():
    return render_template('submit.html')

@app.route('/list', methods=['GET'])
def infolist():
    return render_template('list.html', entries=info_list)

if __name__ == '__main__':
    app.run(debug=True)