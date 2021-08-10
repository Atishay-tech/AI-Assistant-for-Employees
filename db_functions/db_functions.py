from db_functions.DBcm import UseDatabase

dbconfig = {
    'host': '127.0.0.1',
    'user': 'company_admin',
    'password': 'company_password',
    'database': 'company_database',
}


def get_data(id: str, category: str) -> ('id', 'name'):
    
    _SQL = '''Select id, name from {} where id='{}';'''.format(category, id)

    with UseDatabase(dbconfig) as cursor:
        cursor.execute(_SQL)
        data = cursor.fetchone()

    return data


def get_meetings(emp_id: str, category: str, attended: int = 0):

    if category == 'admin':
        _SQL = '''Select * from meetings where attended = {}'''.format(attended)
    elif category == 'employee':
        _SQL = '''Select * from meetings
                    where (meetings.attended = {}) and meetings.id in
                    (select meet_id from meet_emp 
                    where emp_id = '{}' and meet_emp.attended = {});'''.format(attended, emp_id, attended)
    
    with UseDatabase(dbconfig) as cursor:
        cursor.execute(_SQL)
        meetings = cursor.fetchall()
    
    return meetings


def get_projects(emp_id: str, category: str, completed: int = 0):

    if category == 'admin':
        _SQL = '''Select * from projects where completed = {}'''.format(completed)
    elif category == 'employee':
        _SQL = '''Select * from projects
                    where (projects.completed = {}) and projects.id in
                    (select project_id from project_emp where emp_id = '{}');'''.format(completed, emp_id)
    
    with UseDatabase(dbconfig) as cursor:
        cursor.execute(_SQL)
        meetings = cursor.fetchall()
    
    return meetings


def user_in_database(id: str, password: str, category: str) -> bool:

    _SQL = '''Select * from {} where id='{}' and pass='{}';'''.format(category, id, password)

    with UseDatabase(dbconfig) as cursor:
        cursor.execute(_SQL)
        output = cursor.fetchall()

    if output:
        return True
    else:
        return False


def meeting_done(meet_id: str, emp_id: str, session_type: str) -> None:
    if session_type == 'admin':
        _SQL = '''Update meetings set attended = 1 where id = '{}';'''.format(meet_id)
    elif session_type == 'employee':
        _SQL = '''Update meet_emp set attended = 1
                    where meet_id = '{}' and emp_id = '{}';'''.format(meet_id, emp_id)

    with UseDatabase(dbconfig) as cursor:
        cursor.execute(_SQL)


def project_completed(project_id: str) -> None:
    _SQL = '''Update projects set completed = 1 where id = '{}';'''.format(project_id)

    with UseDatabase(dbconfig) as cursor:
        cursor.execute(_SQL)


def add_employee(id:str, name:str, password:str, address:str, num:int) -> None:

    _SQL = '''insert into employee (id, name, pass, address, num)
                values ('{}', '{}', '{}', '{}', {});'''.format(id, name, password, address, num)

    with UseDatabase(dbconfig) as cursor:
        cursor.execute(_SQL)


def add_project(project_id: str, name: str, date, info: str, employees: list) -> None:

    with UseDatabase(dbconfig) as cursor:
        _SQL = '''insert into projects (id, name, deadline, info)
                    values ('{}', '{}', '{}', '{}');'''.format(project_id, name, date, info)
        cursor.execute(_SQL)

        for emp_id in employees:
            _SQL = '''insert into project_emp (project_id, emp_id)
                        values ('{}', '{}');'''.format(project_id, emp_id)
            cursor.execute(_SQL)


def add_meeting(date, time, info: str, employees: list, allow_all: bool) -> None:

    datetime = date + ' ' + time
    
    with UseDatabase(dbconfig) as cursor:
        _SQL = '''insert into meetings (time, info)
                    values ('{}', '{}');'''.format(datetime, info)
        cursor.execute(_SQL)

        cursor.execute('''select id from meetings order by id desc limit 1;''')
        meet_id = cursor.fetchone()[0]

        if allow_all:
            cursor.execute('''Select id from employee''')
            employees = [row[0] for row in cursor.fetchall()]
    
        for emp_id in employees:
            _SQL = '''insert into meet_emp (meet_id, emp_id)
                        values ('{}', '{}');'''.format(meet_id, emp_id)
            cursor.execute(_SQL)


if __name__ == '__main__':
    print(get_data('1'))