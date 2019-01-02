from flask import Flask, render_template, url_for, flash, redirect
from forms import RegForm, LoginForm
from flask_msqldb import MySQL

app = Flask(__name__)

app.config["SECRET_KEY"] = "b91c18302ccdec516275c6ac1ad85b90"
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.comfig["MYSQL_DB"] = "flask2blog"

mysql = MySQL(app)
cur = mysql.connection.cursor()
# cur.execute("SQL")



posts = [

    {
        "id" : 1,
        "author" : "Vadon",
        "title" : "Blog 1",
        "content" : "content content content content",
        "date_posted" : "02-01-2019"
    },
    {
        "id" : 2,
        "author" : "Vadon",
        "title" : "Blog 2",
        "content" : "content content content content",
        "date_posted" : "02-01-2019"
    },
    {
        "id" : 3,
        "author" : "Vadon",
        "title" : "Blog 3",
        "content" : "content content content content",
        "date_posted" : "02-01-2019"
    }
]


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegForm()

    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!","success")
        return redirect(url_for("index"))

    return render_template("register.html", form=form, title="Registre")

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        if form.email.data == "vaismanvadik@gmail.com" and form.password.data == "pass":
            flash("You have been Logged in!", "success")
            return redirect(url_for("index"))
        else:
            flash("Login Falied", "danger")
    return render_template("login.html", form=form, title="Login")

if __name__ == "__main__":
    app.run(debug=True)