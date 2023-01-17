from typing import Any, Callable
from game.character import Character

creations_funcs : dict[str, Callable[..., Character]] = {}


def register(character_type : str, creation_func : Callable[..., Character]):
    creations_funcs[character_type] = creation_func
    
def unregister(character_type : str):
    creations_funcs.pop(character_type, None)

def create(arguments : dict[str, Any]) -> Character:
    args_copy = arguments.copy()
    character_type = args_copy.pop("type")
    try:
        creation_func = creations_funcs[character_type]
    except KeyError:
        raise ValueError(f"Invalid character type: {character_type}")
    
    return creation_func(**args_copy)
    