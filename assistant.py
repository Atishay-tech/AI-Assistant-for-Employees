from comcenter.com_class import Command
from speech import VoiceEngine
from core_func import core


engine = VoiceEngine()

def speak():
    while True:
        input_ = engine.listen_from_mic(adjust=True)
        if input_ in ['exit', 'quit', 'bye', 'goodbye']:
            engine.speak('Have a good day!')
            break
        print(input_)
        engine.speak('On It.')
        if not input_ or not core.exec_core(input_):
            command = Command(input_)
            command.execute()


if __name__ == '__main__':
    speak()