# python 3.9+ 
def process_item(items: list[float]) -> dict[str, int]:
    return {item: len(item) for item in items}

# before python 3.9+ 
from typing import List, Dict
def process_item(items: List[float])-> dict[str, int]: 
    return {item: len(item) for item in items}
