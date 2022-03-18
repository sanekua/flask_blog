from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm, RequestResetForm, ResetPasswordForm
from flaskblog import app, db, bcrypt, mail
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message
import secrets
import os

#
# @app.before_first_request
# def create_tables():
#     print("workoin")
#     db.create_all()
#
#
# @app.route('/')
# @app.route('/home')
# def home():
#     page = request.args.get('page', 1, type=int)
#     print('page',page)
#     posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=2)
#     return render_template('home.html', posts=posts)
#
#
# @app.route('/about')
# def about():
#     # db.session.add(User(username='Alex', email='ooo@mail.ua', password='1111'))
#     # db.session.commit()
#     # db.session.close()
#     return render_template('about.html')





# def save_picture(form_picture):
#     random_hex = secrets.token_hex(8)
#     _, f_ext = os.path.splitext(form_picture.filename)
#     picture_fn = random_hex + f_ext
#     picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
#
#     output_size = (125, 125)
#     i = Image.open(form_picture)
#     i.thumbnail(output_size)
#     i.save(picture_path)
#     print(picture_fn)
#     return picture_fn
#
#
#
# @app.route('/post/new', methods=['GET', 'POST'])
# @login_required
# def new_post():
#     form = PostForm()
#     if form.validate_on_submit():
#         post = Post(title=form.title.data, content=form.content.data, author=current_user)
#         db.session.add(post)
#         db.session.commit()
#         flash(f'Your post has been updated', 'success')
#         return redirect(url_for('home'))
#     return render_template('create_post.html', title='New Post',
#                            form=form, legend='New Post')
#
#
# @app.route('/post/<int:post_id>')
# def post(post_id):
#     post = Post.query.get_or_404(post_id)
#     print('post', post.__dict__)
#     return render_template('post.html', title=post.title, post=post)
#
#
# @app.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
# @login_required
# def update_post(post_id):
#     post = Post.query.get_or_404(post_id)
#     if post.author != current_user:
#         abort(403)
#     form = PostForm()
#     # print('post dicr', post.__dict__)
#     # print('from dict', form.title.data)
#     # print('from dict', form.content.data)
#     if form.validate_on_submit():
#         post.title = form.title.data
#         post.content = form.content.data
#         db.session.commit()
#         flash('Your post has been updated!', 'success')
#         return redirect(url_for('post', post_id=post.id))
#     elif request.method == 'GET':
#         form.title.data = post.title
#         form.content.data = post.content
#     print('post', current_user.__dict__)
#     return render_template('create_post.html', title='Updated Post',
#                            form=form, legend='Update Post')
#
#
# @app.route('/post/<int:post_id>/delete_post', methods=['POST'])
# def delete_post(post_id):
#     post = Post.query.get_or_404(post_id)
#     if post.author != current_user:
#         abort(403)
#     db.session.delete(post)
#     db.session.commit()
#     flash('Your post has been deleted', 'success')
#     return redirect(url_for('home'))
#
#
# @app.route('/user/<string:username>')
# def user_posts(username):
#     page = request.args.get('page', 1, type=int)
#     print('page',page)
#     user = User.query.filter_by(username=username).first_or_404()
#     posts = Post.query.filter_by(author=user)\
#         .order_by(Post.date_posted.desc())\
#         .paginate(page=page, per_page=2)
#     return render_template('user_posts.html', posts=posts, user=user)
#
#
# def send_reset_email(user):
#     token = user.get_reset_token()
#     print('token',token)
#     msg = Message('Password Reset Request', sender='noreply@demo.com',
#                   recipients=[user.email])
#     msg.body = f''' To reset your passwords , visit the following link:
# {url_for('reset_token', token=token, _external=True)}
#
# If you did not make this request just ignore this message !
#     '''
#     print(msg)
#     mail.send(msg)
#
#
# @app.route('/reset_password', methods=['GET', 'POST'])
# def reset_request():
#     if current_user.is_authenticated:
#         return redirect(url_for('home'))
#     form = RequestResetForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(email=form.email.data).first()
#         print('user reset password',)
#         send_reset_email(user)
#         # current_user.email = form.email.data
#         # db.session.commit()
#         print(999)
#         flash('An email has been sent with instructions to reset your password!', 'info')
#         return redirect(url_for('login'))
#     return render_template('reset_request.html',title='Reset Password', form=form)
#
#
# @app.route('/reset_password/<token>', methods=['GET', 'POST'])
# def reset_token(token):
#     if current_user.is_authenticated:
#         return redirect(url_for('home'))
#     user = User.verify_reset_token(token)
#     print('reset pasword user id', user)
#     if not user:
#         flash('That is invalid/expired token', 'warning')
#         return redirect(url_for('reset_request'))
#     form = ResetPasswordForm()
#     if form.validate_on_submit():
#         hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
#         print('user register', user)
#         user.password = hashed_password
#         db.session.commit()
#         flash(f' Your password has been updated !', 'success')
#         return redirect(url_for('login'))
#     return render_template('reset_token.html',title='Reset Password Token', form=form)
