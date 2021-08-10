import eel
from comcenter.com_class import Command
from core_func import core

eel.init('frontend')

@eel.expose
def get_result(input_):
    if input_ in ['exit', 'quit', 'bye', 'goodbye']:
        return 'Have a good day!'
    
    result = core.exec_core(input_)
    if result:
        return result

    else:
        command = Command(input_)
        command.execute()
        return 'Redirecting'

if __name__ == '__main__':
    eel.start('index.html')