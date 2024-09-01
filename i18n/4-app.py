#!/usr/bin/env python3
"""Task 4: Force locale with URL parameter
"""

from flask import Flask, request, render_template
from flask_babel import Babel


class Config:
    """Config class"""

    DEBUG = True
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    locale = request.args.get("locale")
    if locale in app.config["LANGUAGES"]:
        print(f"Locale set by URL parameter: {locale}")
        return locale
    best_match = request.accept_languages.best_match(app.config["LANGUAGES"])
    print(f"Best match locale: {best_match}")
    return best_match


@app.route("/")
def index() -> str:
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run()
