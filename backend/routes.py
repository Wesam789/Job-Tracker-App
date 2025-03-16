# routes.py
from flask import Blueprint, request, jsonify
from models import db, Job

job_routes = Blueprint('job_routes', __name__)

@job_routes.route('/jobs', methods=['GET'])
def get_jobs():
    jobs = Job.query.all()
    return jsonify([
        {'id': job.id, 'company': job.company, 'position': job.position, 'date_created': job.date_created, 'status': job.status}
        for job in jobs
    ])

@job_routes.route('/jobs', methods=['POST'])
def add_job():
    data = request.get_json()
    new_job = Job(
        company=data['company'],
        position=data['position'],
        date_created=data.get('date_created', ''),  
        status=data['status']
    )
    db.session.add(new_job)
    db.session.commit()
    return jsonify({
        'id': new_job.id,
        'company': new_job.company,
        'position': new_job.position,
        'date_created': new_job.date_created,
        'status': new_job.status
    }), 201 

@job_routes.route('/jobs/<int:job_id>', methods=['PUT'])
def update_job(job_id):
    job = Job.query.get(job_id)
    if not job:
        return jsonify({'message': 'Job not found'}), 404
    
    data = request.get_json()
    job.company = data.get('company', job.company)
    job.position = data.get('position', job.position)
    job.date_created = data.get('date_created', job.date_created)
    job.status = data.get('status', job.status)
    
    db.session.commit()
    return jsonify({'message': 'Job updated successfully'})

@job_routes.route('/jobs/<int:job_id>', methods=['DELETE'])
def delete_job(job_id):
    job = Job.query.get(job_id)
    if not job:
        return jsonify({'message': 'Job not found'}), 404
    
    db.session.delete(job)
    db.session.commit()
    return jsonify({'message': 'Job deleted successfully'})