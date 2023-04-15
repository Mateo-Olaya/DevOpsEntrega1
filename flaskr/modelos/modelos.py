from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from sqlalchemy import DateTime
from sqlalchemy import Date
import datetime

db = SQLAlchemy()

class BlackList(db.Model):
    id = db.Column(db. Integer, primary_key=True)
    email = db.Column(db.String)
    motivo = db.Column(db.String(256))
    ip_address = db.Column(db.String(46))
    createdAt = db.Column(DateTime(),default=datetime.datetime.utcnow)

class BlackListSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = BlackList
        include_relationships = True
        load_instance = True