from Implementación.DoubleNode import DoubleNode

class DoubleList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def size(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def first(self):
        return self._head

    def last(self):
        return self._tail

    def addFirst(self, e):
        n = DoubleNode(e)
        if self.isEmpty():
            self._head = n
            self._tail = n
        else:
            n.setNext(self._head)
            self._head.setPrev(n)
            self._head = n
        self._size += 1

    def addLast(self, e):
        n = DoubleNode(e)
        if self.isEmpty():
            self._head = n
            self._tail = n
        else:
            self._tail.setNext(n)
            n.setPrev(self._tail)
            self._tail = n
        self._size += 1

    def removeFirst(self):
        if self.isEmpty():
            return None
        else:
            temp = self._head
            self._head = temp.getNext()
            temp.setNext(None)
            self._head.setPrev(None)
            self._size -= 1
            return temp.getData()

    def removeLast(self):
        if self.isEmpty():
            return None
        else:
            temp = self._tail
            self._tail = temp.getPrev()
            self._tail.setNext(None)
            temp.setPrev(None)
            self._size -= 1
            return temp.getData()

    def remove(self, n):
        if n == self._head:
            return self.removeFirst()
        elif n == self._tail:
            return self.removeLast()
        else:
            e = n.getData()
            temp_prev = n.getPrev()
            temp_next = n.getNext()
            temp_prev.setNext(temp_next)
            temp_next.setPrev(temp_prev)
            n.setNext(None)
            n.setPrev(None)
            self._size -= 1
            return e

    def addBefore(self, n, e):
        if n == self._head:
            self.addFirst(e)
        else:
            m = DoubleNode(e)
            temp_prev = n.getPrev()
            temp_prev.setNext(m)
            m.setPrev(temp_prev)
            m.setNext(n)
            n.setPrev(m)
            self._size += 1

    def addAfter(self, n, e):
        if n == self._tail:
            self.addLast(e)
        else:
            m = DoubleNode(e)
            temp_next = n.getNext()
            n.setNext(m)
            m.setPrev(n)
            m.setNext(temp_next)
            temp_next.setPrev(m)
            self._size += 1

    def __str__(self):
        s = "["
        temp = self._head
        while temp is not None:
            s += str(temp.getData())
            if temp.getNext() is not None:
                s += ", "
            temp = temp.getNext()
        s += "]"
        return s