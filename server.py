from flask import Flask, render_template, request, redirect, session
import db_functions.db_functions as db
from typing import NewType

html_page = NewType('html_page', None)

app = Flask(__name__)
app.secret_key = 'secret key'


@app.route('/')
@app.route('/login/', methods=['GET'])
def login() -> html_page:
    return render_template('login.html')


@app.route('/login/<category>', methods=['POST'])
def validate_data(category) -> html_page:
    id = request.form.get('id')
    password = request.form.get('password')

    if db.user_in_database(id, password, category):
        session['id'] = id
        session['type'] = category
        print(session)
        return redirect('/{}page/{}'.format(category, id))
    
    else:
        return "Invalid id or password"


@app.route('/employeepage/<id>')
def get_employee_data(id) -> html_page:
    
    if 'id' in session and session['id'] == id and session['type'] == 'employee':
        id, name = db.get_data(id, 'employee')

        return render_template('employee_page.html',
                                id=id,
                                name=name)

    else:
        return redirect('/')


@app.route('/adminpage/<id>')
def get_admin_page(id) -> html_page:

    if 'id' in session and session['id'] == id and session['type'] == 'admin':
        id, name = db.get_data(id, 'admin')
        print(id, name)
        print(session)
        return render_template('admin_page.html',
                                id=id,
                                name=name)
    
    else:
        return redirect('/')


@app.route('/meetings/<id>')
def view_meetings(id) -> html_page:
    if 'id' in session and session['id'] == id:
        meetings = db.get_meetings(id, session['type'])
    else:
        return "Invalid id or password"
    
    return render_template('meetings.html',
                            id = id,
                            meetings = meetings)


@app.route('/projects/<id>')
def view_projects(id) -> html_page:
    if 'id' in session and session['id'] == id:
        projects = db.get_projects(id, session['type'])
    else:
        return "Invalid id or password"
    
    return render_template('projects.html',
                            id = id,
                            projects = projects)


@app.route('/meeting_done/<meeting_id>')
def meeting_done(meeting_id):
    db.meeting_done(meeting_id, session['id'], session['type'])

    return redirect('/meetings/{}'.format(session['id']))


@app.route('/project_completed/<project_id>')
def project_done(project_id):
    print(session)
    if 'id' in session and session['type'] == 'admin':
        db.project_completed(project_id)
    else:
        return 'Out of your reach..'

    return redirect('/projects/{}'.format(session['id']))


@app.route('/addemployee', methods=['POST'])
def add_employee():
    id = request.form.get('id')
    name = request.form.get('name')
    password = request.form.get('password')
    address = request.form.get('address')
    number = request.form.get('number')

    db.add_employee(id, name, password, address, number)

    return redirect('/adminpage/{}'.format(session['id']))


@app.route('/addmeeting', methods=['POST'])
def add_meeting():
    date = request.form.get('date')
    time = request.form.get('time')
    info = request.form.get('info')
    employees = [x.strip() for x in request.form.get('employees').split(',')]
    allow_all = request.form.get('allow_all') == 'True'

    db.add_meeting(date, time, info, employees, allow_all)

    return redirect('/adminpage/{}'.format(session['id']))


@app.route('/addproject', methods=['POST'])
def add_project():
    id = request.form.get('id')
    name = request.form.get('name')
    deadline = request.form.get('date')
    info = request.form.get('info')
    employees = [x.strip() for x in request.form.get('employees').split(',')]

    db.add_project(id, name, deadline, info, employees)

    return redirect('/adminpage/{}'.format(session['id']))


@app.route('/logout')
def logout() -> html_page:
    session.pop('id')
    session.pop('type')
    return redirect('/')


if __name__ == "__main__":
    app.run()