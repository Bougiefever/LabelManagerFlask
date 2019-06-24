from flask import Blueprint
# from .views.jobs import bp as job_bp, JobAPI
from .views import bp
from .views.jobs import JobAPI
from .views.images import ImageAPI


def register_api(blueprint, view, endpoint, url, pk='id', pk_type='int'):
    view_func = view.as_view(endpoint)
    blueprint.add_url_rule(
        url,
        defaults={pk: None},
        view_func=view_func,
        methods=['GET'])
    blueprint.add_url_rule(
        url,
        view_func=view_func,
        methods=['POST', 'PUT'])
    blueprint.add_url_rule(
        '%s<%s:%s>' % (url, pk_type, pk),
        view_func=view_func,
        methods=['GET', 'DELETE'])

register_api(bp, JobAPI, 'job_api', '/jobs/')
register_api(bp, ImageAPI, 'image_api', '/images/')
