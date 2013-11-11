import pyttsx

engine = pyttsx.init()

for v in engine.getProperty('voices'):
	if v.name == 'spanish-latin-am':
		engine.setProperty('rate', 170)
		engine.setProperty('voice', v.id)
		engine.say("Hola")
		engine.say("Estan redis para que les coma el culo?")
		engine.say("Cinco cuadras...")
		engine.say("Fokin Puta")

engine.runAndWait()



