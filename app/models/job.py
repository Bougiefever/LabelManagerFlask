from flask import jsonify
from .. import db
from .. import ma
import sqlalchemy
from datetime import datetime


class Job(db.Model):
    __tablename__ = "jobs"

    def __init__(self, job_dict=None):
        if job_dict is not None:
            if "id" in job_dict:
                self.id = job_dict["id"]
            self.name = job_dict["name"]

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=100), nullable=False, unique=True)
    created_on = db.Column(db.DateTime())
    last_updated_on = db.Column(db.DateTime())
    # image_count = db.Column(db.Integer())
    images = db.relationship('Image', backref='job', lazy='select')

    def create(self, job):
        job.created_on = datetime.utcnow()
        job.last_updated_on = datetime.utcnow()
        db.session.add(job)
        db.session.commit()
        return job

    def update(self, job_dict):
        id = job_dict["id"]
        del job_dict["id"]
        if "created_on" in job_dict:
            del job_dict["created_on"]
        self.query.filter_by(id=id).update(job_dict)
        job = self.query.get(id)
        job.last_updated_on = datetime.utcnow()
        print(job.id, job.name, job.last_updated_on)

        db.session.commit()
        job = self.query.get(id)
        return job

    def delete(self, job_id):
        job = self.query.filter_by(id=job_id).one()
        db.session.delete(job)
        db.session.commit()

    def __repr__(self):
        return '<Job %s>' % self.name
    # __table_args__ = (
    #     db.CheckConstraint('image_count > 0', name='positive_count'),
    # )


class JobSchema(ma.ModelSchema):
    class Meta:
        model = Job
