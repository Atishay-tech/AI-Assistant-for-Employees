import json

INFO_PATH = 'config.json'


def input_details():
    details = dict()

    print('Please enter login details:')
    details['id'] = input('ID: ')
    details['name'] = input('Name: ')
    details['category'] = \
        'admin' if int(input('Type (1 for admin, 2 for employee): ')) == 1\
        else 'employee'
    details['password'] = input('Password: ')

    return details


def exec(query: str = 'Update Info'):
    details = input_details()
    with open(INFO_PATH, 'w') as file:
        json.dump(details, file)


if __name__ == '__main__':
    exec()