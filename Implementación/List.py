from Implementación.Node import Node


class List:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def size(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def setSize(self, s):
        self._size = s

    def First(self):
        return self._head

    def Last(self):
        return self._tail

    def addFirst(self, e):
        n = Node(e)
        if self.isEmpty():
            self._head = n
            self._tail = n
        else:
            n.setNext(self._head)
            self._head = n
        self._size += 1

    def addLast(self, e):
        n = Node(e)
        if self.isEmpty():
            self._head = n
            self._tail = n
        else:
            self._tail.setNext(n)
            self._tail = n
        self._size += 1

    def removeFirst(self):
        if not self.isEmpty():
            temp = self._head
            self._head = temp.getNext()
            temp.setNext(None)
            self._size -= 1
            return temp.getData()
        else:
            return None

    def removeLast(self):
        if self._size == 1:
            return self.removeFirst()
        else:
            temp = self._tail
            anterior = self._head
            while anterior.getNext() != self._tail:
                anterior = anterior.getNext()
            anterior.setNext(None)
            self._tail = anterior
            self._size -= 1
            return temp.getData()

    def __str__(self):
        temp = self._head
        impresion = ""
        while temp != self._tail:
            impresion = impresion + str(temp) + " --> "
            temp = temp.getNext()
        return impresion + str(temp)
