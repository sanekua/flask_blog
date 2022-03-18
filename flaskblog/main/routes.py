from flask import Blueprint
from flask import render_template, request
from flaskblog import db
from flaskblog.models import Post

main = Blueprint('main', __name__)


@main.before_first_request
def create_tables():
    print("workoin")
    db.create_all()


@main.route('/')
@main.route('/home')
def home():
    page = request.args.get('page', 1, type=int)
    print('page', page)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=2)
    return render_template('home.html', posts=posts)


@main.route('/about')
def about():
    # db.session.add(User(username='Alex', email='ooo@mail.ua', password='1111'))
    # db.session.commit()
    # db.session.close()
    return render_template('about.html')
