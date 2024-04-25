class Node:
    def __init__(self, data=None):
        self._data = data
        self._next = None

    def getData(self):
        return self._data

    def getNext(self):
        return self._next

    def setData(self, e):
        self._data = e

    def setNext(self, n):
        self._next = n

    def __str__(self):
        return str(self._data)