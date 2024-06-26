from Implementación.List import List


class Queue:
    def __init__(self):
        self._data = List()

    def size(self):
        return self._data.size()

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, e):
        self._data.addLast(e)

    def dequeue(self):
        if self.isEmpty():
            return None
        return self._data.removeFirst()

    def first(self):
        if self.isEmpty():
            return None
        return self._data.First().getData()
