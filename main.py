from comcenter.com_class import Command
from speech import VoiceEngine

engine = VoiceEngine()
input = engine.listen_from_mic(adjust=True)
command = Command(input)
command.execute()
engine.speak('Here are your results.')