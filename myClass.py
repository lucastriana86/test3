


class myClass(object):

    def __init__(self, value):
        self._value = value

    def changeValue(self,newValue):
        self._value = newValue

    def returnValue(self):
        return self._value