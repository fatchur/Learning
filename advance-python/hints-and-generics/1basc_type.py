

# basic function annotations
from ast import Dict


def greet(name: str) -> str: 
    return f"Hello, {name}"


# basic variable annotations
age: int = 25 
scores: list[float]= [0.1, 0.2]
my_dict: dict[str, int] = {"a": 1, "b":2}
