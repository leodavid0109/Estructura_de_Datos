class DoubleNode:
    def __init__(self, data = None):
        self._data = data
        self._prev = None
        self._next = None

    def setData(self, d):
        self._data = d

    def setNext(self, n):
        self._next = n

    def setPrev(self, p):
        self._prev = p

    def getData(self):
        return self._data

    def getNext(self):
        return self._next

    def getPrev(self):
        return self._prev