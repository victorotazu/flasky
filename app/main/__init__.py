from flask import Blueprint
# This is how flask/python knows that this is a blueprint.
# Blueprints allow devs to organize their code in modules
# main is created here to avoid circular references with views and errors
main = Blueprint('main', __name__)
from . import views, errors