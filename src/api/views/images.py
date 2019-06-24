from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView
from http import HTTPStatus
from ...models.image import Image
from ...models.job import Job,
import json

headers = {'Content-Type': 'application/json'}
jobs = Job()
job_schema = JobSchema()
jobs_schema = JobSchema(many=True)


class ImageAPI(MethodView):
    """ handle image methods """

    def get(self, id):
        """ get a list of all jobs or one job if and id is passed in """
        if id is None:
            # return a list of images
            body = jsonify({
                        "ok": True,
                        "message": "image list",
                        "data": []
            })
            return make_response(body, HTTPStatus.OK, headers)
        else:
            # return one image
            body = jsonify({
                        "ok": True,
                        "message": "image",
                        "data": None
            })
            return make_response(body, HTTPStatus.OK, headers)

    def post(self):
        # create a new image
        body = jsonify({
                    "ok": True,
                    "message": "image",
                    "data": None
        })
        return make_response(body, HTTPStatus.OK, headers)

    def delete(self, id):
        # delete an image
        body = jsonify({
                    "ok": True,
                    "message": "image",
                    "data": None
        })
        return make_response(body, HTTPStatus.OK, headers)

    def put(self, id):
        # update a single image
        body = jsonify({
                    "ok": True,
                    "message": "image",
                    "data": None
        })
        return make_response(body, HTTPStatus.OK, headers)
