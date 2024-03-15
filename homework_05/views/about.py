from flask import Blueprint, render_template

about_app = Blueprint(
    "about_app",
    __name__,
    url_prefix="/about"
)


@about_app.get("/")
def about_view():
    return render_template("about.html")
