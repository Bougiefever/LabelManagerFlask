import pytest
from src import db
from src.models.job import Job, JobSchema


def test_schema_validation_successful():
    job = Job()
    job.name = "test name"
    job_schema = JobSchema()


def test_create_job_from_dict():
    job_dict = {"id": 1,  "name": "a job"}
    job = Job(job_dict)
    assert job is not None


def test_schema_validation_schema_validation():
    schema = JobSchema()
    jobdict = {'id': 1, 'name': 'create job object'}
    assert type(jobdict) is dict

    new_job = Job(jobdict)
    assert type(new_job) is Job

    json_job = schema.dump(new_job).data
    assert type(json_job) is dict