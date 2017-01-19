from abc import ABCMeta, abstractmethod

class Shape(metaclass=ABCMeta):
	@abstractmethod
	def area(self):
		pass

class Circle(Shape):
	def __init__(self, r):
		self.r = r

	def area(self):
		return self.r* self.r*3.14

class Rectalg(Shape):
	def __init__(self, x, y):
		self.x=x
		self.y=y

	def area(self):
		return self.x * self.y

class Factory(object):
	def area(self, obj):
		return eval('obj').area()

c=Circle(2)
print(c.area())
r=Rectalg(2,3)
print(r.area())

f=Factory()
print(f.area(c))
print(f.area(r))
