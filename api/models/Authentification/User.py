from werkzeug.security import generate_password_hash, check_password_hash
from backend.database import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(254), nullable=False, unique=True)
    # pseudo = db.Column(db.String(50), nullable=False, unique=True)
    prenom = db.Column(db.String(50))
    nom = db.Column(db.String(50))
    likes = db.Column(db.Integer, default=0)
    password_hash = db.Column(db.String(350))
    
    DONOTSEND = ['password_hash']

    ### relationships
    albums = db.relationship('Album', backref='auteur')
    images = db.relationship('Image', backref='photographe')

    def __init__(self, **kwargs):
        try:
            kwargs['password_hash'] = self._set_password(kwargs.pop('password'))
        except KeyError:
            # maybe not needed, what about Oauth2 ?
            raise KeyError('password needed to create an User')

        super(User, self).__init__(**kwargs)

    def change_password(self, password, new_password, new_password_duplicate):
        if self.check_password(password):
            if new_password == new_password_duplicate:
                self.password_hash = generate_password_hash(new_password)

    # do *NOT* use it outside of the class, use change_password instead
    def _set_password(self, password):
        return generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {} {}>'.format(self.prenom, self.nom)
