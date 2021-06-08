"""Module for performing speech recognition and text to speech methods."""

import pyttsx3
import speech_recognition as sr


class VoiceEngine():
    """Main Speech Class
    
    Methods:
        listen_from_mic     : Receives audio input from microphone and returns it as string
        record_from_file    : Receives audio input from audio file and returns it as string
        speak               : Speaks the given text
        set_voice           : Sets the voice to male or female
    
    Attributes:
        recognizer      (sr.Recognizer)
        speech_engine   (pyttsx3.Engine)
    """

    def __init__(self) -> None:
        self.recognizer = sr.Recognizer()
        self.speech_engine = pyttsx3.init()
        self.set_voice(1)


    def set_voice(self, agent_no: int = 1) -> None:
        """Sets the voice to male or female
        
        agent_no: 0 for male, 1 for female
        """
        voices = self.speech_engine.getProperty('voices')
        self.speech_engine.setProperty('voice', voices[agent_no].id)


    def listen_from_mic(self, adjust: bool = False, show_all: bool= False) -> str:
        """Receives audio from microphone and returns it as a str
        
        adjust: set equal to True to adjust for ambient noise
        show_all: set equal to True to get extended recognition results
        """
        mic = sr.Microphone()
        audio_data = None
        
        try:
            with mic as source:
                if adjust:
                    self.recognizer.adjust_for_ambient_noise(source)
                print("Listening...")
                audio_data = self.recognizer.listen(source)
            return self._audio_to_str(audio_data, show_all)

        except:
            print("\nMic access error!")
            return None


    def record_from_file(self, file_path: str = None) -> str:
        """Receives audio input from audio file and returns it as a str
        
        file_path: the path to the audio containing file
        """
        audio_data = None

        if isinstance(file_path, str):
            try:
                with sr.AudioFile(file_path) as source:
                    audio_data = self.recognizer.record(source)
            except:
                print("\nPlease give a correct file path!")
          
            return self._audio_to_str(audio_data)

        else:
            print("\nFile path should be a 'str'!")
            return None


    def _audio_to_str(self, audio_data, show_all: bool= False) -> str:
        """Converts audio_data into string and returns the result
        
        Uses Google API for voice recognition.
        """
        try:
            return self.recognizer.recognize_google(audio_data, show_all=show_all)
        
        except sr.UnknownValueError:
            print("\nUnable to understand. Please try again.")
            return None
        
        except sr.RequestError as e:
            print(f"\nCould not request results from Google; {e}")
            return None


    def speak(self, text: str = None) -> 'Output from Speakers':
        """Speaks the given text
        
        text: string to be spoken by the speech_engine
        """
        if text is not None:
            self.speech_engine.say(text)
        else:
            self.speech_engine.say("No text given to speak.")
        
        self.speech_engine.runAndWait()



if __name__ == '__main__':
    engine = VoiceEngine()
    text = engine.listen_from_mic(adjust=True, show_all=False)
    print(text)
    engine.speak(text)