from . import db

# To define a new model just inherint from db.Model
# Flask will assign a default table name in case __tablename__ is not defined
# Dont' want that.
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # Relationships can be confusing. @TODO: Read more about Models
    # backref gives a handy name for the relationship so we can use User.role
    # instead of User.role_id.
    # lazy=dynamic helps to avoid queries get executed automatically
    # i.e. user_role = Users.query.filter_by(name='User').
    # user_role.users would return the list of users with the role=User
    # Sometimes we want to sort the resultset for example, in that case lazy helps
    users = db.relationship('User', backref='role', lazy='dynamic')
    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    full_name = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    def __repr__(self):
        return '<User %r>' % self.username
