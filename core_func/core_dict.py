from core_func import meetings
from core_func import projects
from core_func import open_site
from core_func import update_info
from core_func import add_meeting
from core_func import add_project
from core_func import add_employee

core_dict = {
    'meetings' : meetings.exec,
    'projects' : projects.exec,
    'open_site': open_site.exec,
    'change_details': update_info.exec,
    'add_meeting': add_meeting.exec,
    'add_project': add_project.exec,
    'add_employee': add_employee.exec,
}

if __name__ == '__main__':
    print('\nAvailable core functions are:')
    print(*core_dict.keys())