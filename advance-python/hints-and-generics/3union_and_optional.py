from typing import Union, Optional 


def parse_id(id: Union[int, str]) -> int: 
    if isinstance(id, str): 
        return int(id)
    
    return id 


def find_id(id: Union[int, str]) -> Optional[int]: 
    if isinstance(id, str): 
        tmp: int = int(id)
        if tmp > 0: 
            return tmp
    
    if id > 0: 
        return id


        