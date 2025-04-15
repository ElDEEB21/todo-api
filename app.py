from flask import Flask, request, jsonify
from models import db, Task

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/tasks', methods=['GET'])
def get_tasks():
    query = Task.query

    if 'completed' in request.args:
        query = query.filter_by(completed=(request.args['completed'].lower() == 'true'))
    if 'due_date' in request.args:
        query = query.filter_by(due_date=request.args['due_date'])
    if 'priority' in request.args:
        query = query.filter_by(priority=request.args['priority'])

    tasks = query.all()
    response = jsonify([task_to_dict(t) for t in tasks])
    response.headers['Content-Type'] = 'application/json'
    return response

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    task = Task(
        title=data['title'],
        description=data.get('description'),
        due_date=data.get('due_date'),
        priority=data.get('priority', 'medium')
    )
    db.session.add(task)
    db.session.commit()
    return jsonify(task_to_dict(task)), 201

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    task = Task.query.get_or_404(id)
    response = jsonify(task_to_dict(task))
    response.headers['Content-Type'] = 'application/json'
    return response

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = Task.query.get_or_404(id)
    data = request.json
    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    task.due_date = data.get('due_date', task.due_date)
    task.completed = data.get('completed', task.completed)
    task.priority = data.get('priority', task.priority)
    db.session.commit()
    return jsonify(task_to_dict(task))

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return '', 204

@app.route('/tasks/<int:id>/complete', methods=['PUT'])
def mark_complete(id):
    task = Task.query.get_or_404(id)
    task.completed = True
    db.session.commit()
    return jsonify(task_to_dict(task))

@app.route('/tasks/<int:id>/incomplete', methods=['PUT'])
def mark_incomplete(id):
    task = Task.query.get_or_404(id)
    task.completed = False
    db.session.commit()
    return jsonify(task_to_dict(task))

@app.route('/tasks/<int:id>/priority', methods=['PUT'])
def update_priority(id):
    task = Task.query.get_or_404(id)
    task.priority = request.json.get('priority', task.priority)
    db.session.commit()
    return jsonify(task_to_dict(task))

def task_to_dict(task):
    return {
        'id': task.id,
        'title': task.title,
        'description': task.description,
        'due_date': task.due_date,
        'completed': task.completed,
        'priority': task.priority
    }

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
