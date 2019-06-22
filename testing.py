from app.models import Job, Image, JobSchema
import flask_marshmallow

job = Job()
job.name = "test name"
job.image_count = -10
#job.nofield = "nofield"
job_schema = JobSchema()
job_json = job_schema.dump(job)
print(job_json)


flask_marshmallow.pprint(job_json)
