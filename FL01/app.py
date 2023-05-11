
from flask import Flask, render_template, abort, redirect, request
import datetime


app = Flask(__name__)

# ERROR HANDLERS
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500

# R O U T E S

@app.route('/')
@app.route('/index')
def main():
	return "<h1>AHOJ JA SOM DZIN Z FLASKU</h1>"

@app.route('/mojastranka')
def moja():
    return '<h2>Test mojej stranky</h2><br><p>Toto je moja skusobna stranka WEB</p>'

@app.route('/vitajte')
def welcome():
    return render_template('vitajte.html')  # po slovensky

@app.route('/welcome')
def vitajte():
    return redirect('/vitajte')

@app.route('/cas')
def cas():
    return render_template('main.html', cas=datetime.datetime.now())

@app.route('/spravy/<int:index>', methods=['GET'])
def spravy(index):
    spravy = ['sprava1 - zlacnelo mydlo', 'sprava2- zajtra bude pekne', 'sprava3 - Hotovo']
    try:
        return render_template('spravy.html', msg=spravy[index])
    except IndexError:
        abort(404)

@app.route('/kurzkk', methods=['GET'])
def kurz():
    kurz = [12, 34,23,78,45, -5,-76,15,34, 89]
    return render_template('kurzkk.html', kurzy=kurz)


if __name__ == '__main__':
    app.run(debug=True)

# DEVELOPMENT -> DEVOPS -> PRODUKCNY SERVER  <- USER
# --> v3        --> v2.5   --> v1.8

'''
2 - BUgy -
1 - issues
'''

# Agilny vyvoj

