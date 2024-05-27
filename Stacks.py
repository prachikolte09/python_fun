import collections


class Stack:
    ElementWithCachedMax = collections.namedtuple('ElementWithCachedMax', ('element', 'max'))

    def __init__(self):
        self._element_with_cached_max = []

    def empty(self) -> bool:
        return len(self._element_with_cached_max) == 0

    def max(self) -> int:
        if self.empty():
            raise IndexError('Stack is empty')
        return self._element_with_cached_max[-1].max

    def pop(self) -> int:
        if self.empty():
            raise IndexError('Stack is empty')
        return self._element_with_cached_max.pop().element

    def push(self, element):
        self._element_with_cached_max.append(self.ElementWithCachedMax(element, element if self.empty() else max(element, self.max())))



if __name__ == '__main__':
    stack = Stack()
    stack.push(7)
    stack.push(9)
    stack.push(5)
    stack.push(8)
    print(stack._element_with_cached_max)
    stack.push(4)
    print(stack.__dict__)