class Other(object):
  def log(self):
    print 'log'

class Child(object):
  def __init__(self):
    self.other = Other()
  
  def logger(self):
    self.other.log()

son = Child()

son.logger()