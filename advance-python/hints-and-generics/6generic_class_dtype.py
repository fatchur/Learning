from typing import TypeVar, Generic 


T = TypeVar('T')


class Stack(Generic[T]): 
    def __init__(self): 
        self._items: list[T] = []

    def push(self, item: T) -> None: 
        self._items.append(item)

    def pop(self) -> T | None: 
        return self._items.pop() if self._items else None 

    def peek(self) -> T | None: 
        return self._items[-1] if self._items else None 

    def is_empty(self) -> bool: 
        return len(self._items) == 0 


stackNum: Stack = Stack[int]()
stackNum.push(1)
stackNum.push(2)
stackNum.pop()
stackNum.peek() # Type checker knows this is Optional[int]


stackStr: Stack = Stack[str]()
stackStr.push('a')
stackStr.peek() # Type checker knows this is Optional[int]

