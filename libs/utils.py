class Singleton(type):
    """ A metaclass that creates a Singleton base class when called. """
    _instances = {}

    def __init__(self, name, bases, mmbs):
        super(Singleton, self).__init__(name, bases, mmbs)
        self._instance = super(Singleton, self).__call__()

    def __call__(self, *args, **kw):
        return self._instance
