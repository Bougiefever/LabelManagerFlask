from flask import jsonify
from .. import db
from .. import ma
import sqlalchemy
from datetime import datetime


class Image(db.Model):
    __tablename__ = "images"
    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer(), db.ForeignKey('jobs.id'))
    filename = db.Column(db.String())

    def __repr__(self):
        return '<Image %s>' % self.filename


class ImageSchema(ma.ModelSchema):
    class Meta:
        model = Image