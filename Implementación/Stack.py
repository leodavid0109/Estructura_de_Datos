from Implementación.List import List


class Stack:
    def __init__(self):
        self._data = List()

    def size(self):
        return self._data.size()

    def isEmpty(self):
        return self.size() == 0

    def push(self, e):
        self._data.addFirst(e)

    def pop(self):
        return self._data.removeFirst()

    def top(self):
        if not self.isEmpty():
            return self._data.First().getData()
        else:
            return None
