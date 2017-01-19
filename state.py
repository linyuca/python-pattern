from abc import abstractmethod, ABCMeta

class State(metaclass=ABCMeta):
	@abstractmethod
	def handle(self):
		pass

class Astate(State):
	def handle(self):
		print(" aaaaaaaaaaa handled ")
class Bstate(State):
	def handle(self):
		print(" bbbbbbbbbbb handled ")

class Context(State):
	def __init__(self):
		self._state=None

	@property
	def state(self):
		return self._state
		
	@state.setter
	def state(self, s):
		self._state=s

	def handle(self):
		self._state.handle()

c=Context()
a=Astate()
b=Bstate()
c.state=a
c.handle()
c.state=b
c.handle()
