import pytest

import json
from labelmanager import db
from app.models.job import Job
from app.models.image import Image
from http import HTTPStatus


@pytest.fixture
def http_headers():
    return {'Content-Type': 'application/json'}


@pytest.mark.smoke
def test_jobs_endpoint(db_client):
    response = db_client.get('/api/jobs/1')
    assert response is not None


def test_get_one_returns_404_when_job_not_exists(db_client):
    url = '/api/jobs/100'
    response = db_client.get(url)
    assert response.status_code == 404


def test_get_one_returns_job_when_job_exists(db_client, database):
    jobname = "job job"

    # save job in db
    job_dict = {'name': jobname}
    job = Job(job_dict)
    database.session.add(job)
    database.session.commit()
    job = Job.query.filter_by(name=jobname).first()
    assert job is not None

    # get job
    id = job.id
    url = '/api/jobs/{}'.format(str(id))
    response = db_client.get(url)
    assert response.status_code == 200
    json_data = response.json
    assert json_data["ok"] == True
    job = json_data["data"]

    # make sure job exists and we get back the correct job
    assert job is not None
    assert job["name"] == jobname


def test_get_many_returns_empty_list_when_no_jobs_exist(db_client):
    url = '/api/jobs/'
    response = db_client.get(url)
    assert response.status_code == 200
    json_data = response.json
    assert json_data["ok"] == True
    assert json_data["data"] == []


def test_post_creates_new_job(db_client, database, http_headers):
    jobname = "messenger"
    body = json.dumps({'name': jobname})
    response = db_client.post('/api/jobs/', data=body, headers=http_headers)
    assert response.status_code == HTTPStatus.CREATED
    json_data = response.json
    assert json_data["ok"] == True
    saved_job = json_data['data']
    assert saved_job["id"] is not None
    assert saved_job["name"] == jobname
    assert saved_job["created_on"] is not None
    newjob = Job.query.filter_by(name=jobname).first()
    assert newjob is not None


def test_delete_when_job_exists(db_client, database):
    jobname = "delete me"

    # save job in db
    job_dict = {'name': jobname}
    job = Job(job_dict)
    database.session.add(job)
    database.session.commit()
    job = Job.query.filter_by(name=jobname).first()
    assert job is not None

    # delete job
    id = job.id
    url = '/api/jobs/{}'.format(str(id))
    response = db_client.delete(url)
    assert response.status_code == 202
    json_data = response.json
    assert json_data["ok"] == True
    json_data["data"] == None

    # make sure job was deleted from the database
    job = Job.query.get(id)
    assert job is None


def test_delete_when_job_does_not_exist(db_client, database):
    id = 100
    url = '/api/jobs/{}'.format(str(id))
    response = db_client.delete(url)
    assert response.status_code == HTTPStatus.BAD_REQUEST
    json_data = response.json
    assert json_data["ok"] == False
    json_data["data"] == None


def test_update(db_client, database, http_headers):
    jobname = "update me"

    # save job in db
    job_dict = {'name': jobname}
    job = Job(job_dict)
    database.session.add(job)
    database.session.commit()
    job = Job.query.filter_by(name=jobname).first()
    id = job.id
    assert job is not None

    newname = "job has a new name"
    body = json.dumps({'id': job.id, 'name': newname})
    response = db_client.put('/api/jobs/', data=body, headers=http_headers)
    assert response.status_code == HTTPStatus.OK
    json_data = response.json
    assert json_data["ok"] == True
    updated_job = json_data['data']
    assert updated_job["id"] == id
    assert updated_job["name"] == newname

    saved_job = Job.query.get(id)
    assert saved_job.name == newname