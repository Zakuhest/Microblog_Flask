from flask import Blueprint, redirect, render_template, url_for
from app.models.post import Post
from app.models.user import Permission
from app.forms.forms import PostForm
from flask_login import current_user, login_required
from app.db import db

index_router = Blueprint('index', __name__)

@index_router.route('/', methods = ['GET', 'POST'])
@login_required #tiene que tener la sesion iniciada
def index():
    # Añadimos los post
    form = PostForm()
    if current_user.can(Permission.WRITE) and form.validate_on_submit():
        post = Post(body=form.body.data, author=current_user._get_current_object())
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('index.index'))
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template("indexCss.html", form = form, posts = posts, WRITE = Permission.WRITE)