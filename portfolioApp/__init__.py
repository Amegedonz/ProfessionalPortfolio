import flask


app = flask.app()

app.route("/")
def home_page():
    ...