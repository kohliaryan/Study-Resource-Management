from extenstions import db
from flask_security import UserMixin, RoleMixin
from flask_security.models import fsqla_v3 as fsq

fsq.FsModels.set_df_info(db)

class User(db.model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    active = db.Column(db.Boolean)
    fs_uniquifier = db.Column(db.String, nullable=False)
    roles = db.relationship('Role', secoundary = 'user_roles')

class Roles(db.model, RoleMixin):
    id = db.Column(db.Integer, primary_key=True),
    name = db.Column(db.String(80), unique=False, ullable=False)
    description = db.Column(db.String)

class UserRoles(db.model):
    id = db.Column(db.Integer, primary_key=True),
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))


