from flaskblog import create_app, db
#hello world it is develop

app = create_app()

if __name__ == "__main__":
    #db.init_app(app)
    app.run(debug=True)