from flask import Blueprint, render_template


# definujeme blueprint

admin_bp = Blueprint(
    'admin_bp',
    __name__,
    template_folder='templates',
    static_folder='static'
)

@admin_bp.route('/admin')
def admin_home():
    return render_template('admin.html')