from typing import List, TypeVar, Callable, Optional

T = TypeVar('T')
U = TypeVar('U')


def get_first_item(items: List[T]) -> Optional(T): 
    return items[0] if items else None

number: List[int] = [1, 2, 3]
first_num = get_first_item(number) #type checker know this is int | None

letter: List[str] = ['1', '2', '3']
first_num = get_first_item(letter) #type checker know this is str | None


def map_list(items: list[T], func: Callable[[T], U]) -> list[U]: 
    return [func(item) for item in items]


map_list(number, str) # return ['1', '2', '3']
map_list(letter, len) # retunr [1, 1, 1]