from typing import TypeVar

TypeNum = TypeVar('TypeNum', int, float)

def add_number(a: TypeNum, b: TypeNum) -> TypeNum: 
    return a + b 


a: int = 0
b: float = 1. 

add_number(a, b)