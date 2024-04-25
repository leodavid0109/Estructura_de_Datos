class ArrayStack:
    def __init__(self, capacity):
        self._data = [None] * capacity
        self._top = -1

    def size(self):
        return self._top+1

    def isEmpty(self):
        return self._size()==0

    def push(self, e):
        if self._top < len(self._data) - 1:
            self._top += 1
            self._data[self._top] = e
        else:
            print("Stack overflow")

    def pop(self):
        if not self.isEmpty():
            temp = self._data[self._top]
            self._data[self._top] = None
            self._top -= 1
            return temp
        else:
            return None

    def top(self):
        if not self.isEmpty():
            return self._data[self._top]
        else:
            return None
