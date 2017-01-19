class Singleton1(object):
	_ins = None

	def __new__(cls):
		if not cls._ins:
			cls._ins = super(Singleton1, cls).__new__(cls)
		return cls._ins

	def __init__(self, name=None, age=0):
		self.name = name
		self.age = age

	def __repr__(self):
		return("({}, {})".format(self.name, self.age))
	def __str__(self):
		return ("{}:{}".format(self.name, self.age))

class Singleton2(object):
	def __new__(cls, *args, **kwargs):
		if not hasattr(cls, '_instance'):
			cls._instance = super(Singleton2, cls).__new__(cls)
		return cls._instance

	def __init__(self, *args, **kwargs):
		self.name, self.age = args	


def singleton3(cls):
	instances = {}
	def getinstance(*args, **kwargs):
		if cls not in instances:
			instances[cls] = cls(*args, **kwargs)
		return instances[cls]
	return getinstance

@singleton3
class Myclass:
	def __init__(self, name, age):
		self.name=name
		self.age=age
	def __str__(self):
		return("({}, {})".format(self.name, self.age))

	
class call_init(object):
	def __init__(self):
		self._cache = {0:0, 1:1}

	def __call__(self, n):
		if n not in self._cache:
			self._cache[n] = self._cache[n-2] + self._cache[n-1]

		return self._cache[n]
				

class Outfunc:
	def __init__(self, m):
		self.p1 = m

	def __call__(self, f, *args, **kwargs):
		def wrapper(*args, **kwargs):
			print(self.p1)
			print(f.__name__)
			return f(*args, **kwargs)
			
		return wrapper
		

@Outfunc("hhhhh")
def add(x,y):
	return (x+y)
