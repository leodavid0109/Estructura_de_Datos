class ArrayQueue:
    def __init__(self, capacity):
        self._data = [None] * capacity
        self._first = -1
        self._rear = -1

    def size(self):
        temp = len(self._data) - self._first + self._rear
        temp = temp % len(self._data) + 1
        return temp

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, e):
        if self.size() < len(self._data):
            self._rear = (self._rear + 1) % len(self._data)
            self._data[self._rear] = e

    def dequeue(self):
        if self.isEmpty():
            return None
        else:
            temp = self._data[self._first]
            self._data[self._first] = None
            self._first = (self._first + 1) % len(self._data)
            return temp

    def _first(self):
        if self.isEmpty():
            return None
        return self._data[self._first]
