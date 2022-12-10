from flask import Blueprint, redirect, flash, url_for, request, render_template
from flask_login import current_user, login_user, logout_user
from app.forms.forms import LoginForm
from app.models.user import User
from app.login import Login
from werkzeug.urls import url_parse

auth_router = Blueprint("auth", __name__)

Login.login_view = 'auth.login'  # type: ignore

@auth_router.route('/login',methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated: #si no esta autenticado

        return redirect(url_for('index.index'))
    #Se arma el login
    form = LoginForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Usuario o contraseña no valida')
            return redirect(url_for('auth.login'))


        login_user(user, remember=True)
        next_=request.args.get("next")
        return redirect(url_for('index.index'))

    return render_template('login.html',form=form)

@auth_router.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index.index'))