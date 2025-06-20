from flask import Flask, render_template

app = Flask(__name__)


posts = [
    {
        "author": "Arun",
        "title": "First Post",
        "content": "First post content.",
        "created_at": "June 19, 2025",
    },
    {
        "author": "Anonymous",
        "title": "Second Post",
        "content": "Second post content.",
        "created_at": "June 20, 2025",
    },
]


@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about_page():
    return render_template("about.html", title="About")


if __name__ == "__main__":
    app.run(debug=True)
