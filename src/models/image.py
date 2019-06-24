from flask import jsonify
from .. import db
from .. import ma
import sqlalchemy
from datetime import datetime
import enum


class ImageStatus(enum.Enum):
        ToBeLabeled = "To Be Labeld",
        Labeled = "Labeld",
        ToBeTested = "To Be Tested",
        Approved = "Approved",
        Rejected = "Rejected"


class Image(db.Model):
    __tablename__ = "images"
    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer(), db.ForeignKey('jobs.id'))
    filename = db.Column(db.String())
    imageStatus = db.Column(db.Enum(ImageStatus))
    created_on = db.Column(db.DateTime())
    last_updated_on = db.Column(db.DateTime())

    def __repr__(self):
        return '<Image %s>' % self.filename


class ImageSchema(ma.ModelSchema):
    class Meta:
        model = Image