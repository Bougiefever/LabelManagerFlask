import pytest

import json

from src.models.job import Job, JobSchema
from src.models.image import Image
from http import HTTPStatus
import datetime
import time

@pytest.fixture
def http_headers():
    return {'Content-Type': 'application/json'}

@pytest.mark.smoke
def test_images_endpoint(db_client):
    response = db_client.get('/api/images/')
    assert response.status_code == HTTPStatus.OK