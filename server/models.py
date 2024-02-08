from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()


class Bird(db.Model, SerializerMixin):
    __table_name__ = "birds"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)

    def __repr__(self):
        return f"<Bird {self.name} | Species : {self.species}>"
