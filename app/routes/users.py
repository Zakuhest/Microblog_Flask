from flask import Blueprint, render_template, flash, url_for, redirect
from flask_login import current_user, login_required
from app.models.user import User, Permission
from app.forms.forms import EditProfileForm
from app.db import db
from app.decorator import admin_required, permission_required
import hashlib

users_router = Blueprint("users", __name__)

@users_router.route("/insert")
def insert():
    u = User(username = "cris", email = "crisdic@mail.com")
    u.set_password("123")
    db.session.add(u)
    db.session.commit()
    return "Insertado"

@users_router.route('/admin')
@login_required
@admin_required
def for_admins_only():
    return "Para admins!"


@users_router.route('/moderate')
@login_required
@permission_required(Permission.MODERATE)
def for_moderators_only():
    return "Para comentarios de moderadores!"


def gravatar(email="", size=100, default="identicon", rating="g"):
    url = "https://secure.gravatar.com/avatar"
    hash = hashlib.md5(email.encode("utf-8")).hexdigest()
    return "{url}/{hash}?s={size}&d={default}&r={rating}".format(
        url=url, hash=hash, size=size, default=default, rating=rating
    )

@users_router.route('/avatar')
def avatar():
    img_avatar=gravatar(current_user.email,size=256)
    return render_template('avatar.html',variable=img_avatar)


@users_router.errorhandler(404)
def pagina_no_encontrada(e):
    return render_template('404.html')

@users_router.route('/noexiste')
def usuario_noencontrado():
    return render_template('noexiste.html')


@users_router.route('/usuario/<username>')
@login_required
def informacion_usuario(username):
    #WHERE
    obj_usuario=User.query.filter_by(username=username).first_or_404()
    return render_template('usuario/perfil.html',usuario =obj_usuario)


@users_router.route('/usuario/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()

    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.location = form.location.data
        current_user.about_me = form.about_me.data

        db.session.add(current_user._get_current_object())
        db.session.commit()

        flash('Tu perfil se actualizó correctamente.')
        return redirect(url_for('users.informacion_usuario', username=current_user.username))

    form.name.data = current_user.name
    form.location.data = current_user.location
    form.about_me.data = current_user.about_me

    return render_template('usuario/editar_perfil.html', form=form)