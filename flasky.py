import os
from app import create_app, db
from app.models import User, Role
from flask_migrate import Migrate

# The code uses a class factory to create an instance of app
# based on the corresponding configuration, default=dev
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
# @TODO: Investigate why migrations are here
migrate = Migrate(app, db)

# This is to avoid importing User and Role everytime we need
# to work with the db from the shell. Quite useful
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)

# This is a custom command to execute tests.
# unittest will look for a 'tests' package in the whole directory
@app.cli.command()
def test():
    """ Run the unit tests"""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)