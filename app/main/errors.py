from flask import render_template
from . import main

# Notice the change: app --> main. This is because the error handlers are
# defined under the 'main' blueprint/package.
@main.app_errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500