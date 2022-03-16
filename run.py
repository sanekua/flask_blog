from flaskblog import app, db


if __name__ == "__main__":
    db.init_app(app)
    app.run(debug=True)