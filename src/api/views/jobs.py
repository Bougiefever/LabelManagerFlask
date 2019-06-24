from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView
from http import HTTPStatus
from ...models.image import Image
from ...models.job import Job, JobSchema
import json
from . import bp

headers = {'Content-Type': 'application/json'}
jobs = Job()
job_schema = JobSchema()
jobs_schema = JobSchema(many=True)


class JobAPI(MethodView):
    """ handle jobs methods """

    def get(self, id):
        """ get a list of all jobs or one job if and id is passed in """

        if id is None:
            # return a list of jobs
            jobs_list = jobs.query.all()
            jobs_data = jobs_schema.dump(jobs_list).data
            body = jsonify({
                        "ok": True,
                        "message": "job list",
                        "data": jobs_data
            })
            return make_response(body, HTTPStatus.OK, headers)
        else:
            # return the job, or 404 if it doesn't exist
            job = jobs.query.get(id)
            if job is not None:
                body = jsonify({
                            "ok": True,
                            "message": "job was successfully retrieved",
                            "data": job_schema.dump(job).data
                })
                return make_response(body, HTTPStatus.OK, headers)
            else:
                body = jsonify({
                            "ok": False,
                            "message": "job does not exist",
                            "data": None
                })
                return make_response(body, HTTPStatus.NOT_FOUND, headers)

    def post(self):
        """ create a new job """
        json_data = request.get_json()
        job = Job(json_data)

        job = job.create(job)
        job_data = job_schema.dump(job).data
        body = jsonify({
                        "ok": True,
                        "message": "job was created successfully",
                        "data": job_data
                    })
        return make_response(body, HTTPStatus.CREATED, headers)

    def delete(self, id):
        """ delete a single job """

        try:
            jobs.delete(id)
            body = jsonify({
                                "ok": True,
                                "message": "job was successfully deleted",
                                "data": None
                    })
            return make_response(body, HTTPStatus.ACCEPTED, headers)
        except Exception as e:
            body = jsonify({
                                "ok": False,
                                "message": "job does not exist or could not be deleted",
                                "data": None
                    })
            return make_response(body, HTTPStatus.BAD_REQUEST, headers)

    def put(self):
        """ update a single job """
        json_data = request.get_json()

        job = jobs.update(json_data)
        job_data = job_schema.dump(job).data
        body = jsonify({
                                "ok": True,
                                "message": "job was successfully updated",
                                "data": job_data
                    })
        return make_response(body, HTTPStatus.OK, headers)