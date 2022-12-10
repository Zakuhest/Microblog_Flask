from flask import Blueprint, render_template, url_for, redirect, request
from flask_login import login_required, current_user
from app.db import db
from app.forms.forms import EditPostForm
from app.models.post import Post
from app.models.user import Permission

posts_router = Blueprint("posts", __name__)

@posts_router.route('/post/edit-post/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_post(id):
    form = EditPostForm()
    post = Post.query.get(id)
    if post == None:
        return redirect(url_for('index.index'))
    if current_user.can(Permission.WRITE) and form.validate_on_submit():
        post.body = form.body.data
        db.session.commit()
        return redirect(url_for('index.index'))
    
    form.body.data = post.body
    return render_template('posteo/editar_posts.html', form=form, post=post, WRITE = Permission.WRITE)

from flask import g, jsonify

""" @posts_router.route('/postJson/', methods=['POST'])
@permission_required_rest(Permission.WRITE)
def new_post():
    post = Post.from_json(request.json)
    post.author = g.current_user
    db.session.add(post)
    db.session.commit()
    return jsonify(post.to_json()), 201, {'Location': url_for('post_detail', id=post.id)} """