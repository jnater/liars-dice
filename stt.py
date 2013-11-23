import os
import pyttsx
import pygsr
from pygsr import Pygsr
from contextlib import contextmanager

def say(text):
	engine = pyttsx.init()

	for v in engine.getProperty('voices'):
		if v.name == 'spanish-latin-am':
			engine.setProperty('rate', 200)
			engine.setProperty('voice', v.id)
			engine.say(text)

	engine.runAndWait()

def record():
	print "REC:"
	with suppress_stdout_stderr():
		speech = Pygsr()
		speech.record(3) # duration in seconds (3)
		try:
			phrase, complete_response = speech.speech_to_text('es_ES') # select the language
			return phrase
		except:
			return None


class suppress_stdout_stderr(object):
    '''
    A context manager for doing a "deep suppression" of stdout and stderr in 
    Python, i.e. will suppress all print, even if the print originates in a 
    compiled C/Fortran sub-function.
       This will not suppress raised exceptions, since exceptions are printed
    to stderr just before a script exits, and after the context manager has
    exited (at least, I think that is why it lets exceptions through).      

    '''
    def __init__(self):
        # Open a pair of null files
        self.null_fds =  [os.open(os.devnull,os.O_RDWR) for x in range(2)]
        # Save the actual stdout (1) and stderr (2) file descriptors.
        self.save_fds = (os.dup(1), os.dup(2))

    def __enter__(self):
        # Assign the null pointers to stdout and stderr.
        os.dup2(self.null_fds[0],1)
        os.dup2(self.null_fds[1],2)

    def __exit__(self, *_):
        # Re-assign the real stdout/stderr back to (1) and (2)
        os.dup2(self.save_fds[0],1)
        os.dup2(self.save_fds[1],2)
        # Close the null files
        os.close(self.null_fds[0])
        os.close(self.null_fds[1])

