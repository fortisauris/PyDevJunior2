from flask import Blueprint, render_template, request

auth = Blueprint(
    'auth',
    __name__,
    template_folder='templates',
    static_folder='static'
)

@auth.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        print(request.form)
    return render_template('login.html')
