import pyttsx
import pygsr

def say(text):
	engine = pyttsx.init()

	for v in engine.getProperty('voices'):
		if v.name == 'spanish-latin-am':
			engine.setProperty('rate', 170)
			engine.setProperty('voice', v.id)
			engine.say(text)

	engine.runAndWait()



