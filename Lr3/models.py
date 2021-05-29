from app import database

class User(database.Model):
    __tablename__ = 'users'
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(120))

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Link(database.Model):
    __tablename__ = 'links'
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(200))
    user_id = database.Column(database.Integer(), database.ForeignKey('users.id'))

    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def __repr__(self):
        return '<Links {}>'.format(self.name)