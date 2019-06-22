from flask import render_template, redirect, url_for, abort, flash, request,\
    current_app, make_response

from . import bp

from .. import db
from ..models.image import Image
from ..models.job import Job


@bp.route('/', methods=['GET'])
def index():
    return "Hello there"