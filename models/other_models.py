#========CATEGORY_MODEL========


from dataclasses import dataclass
from enum import Enum


@dataclass
class Category:

    name : str

    def __post_init__ (self):

        if not self.name.strip():

            raise ValueError("category name cant be empty.")
        
    def __str__ (self):

        return self.name
    


class Priority(Enum):

    LOW = 1

    MEDIUM = 2

    HIGH = 3


class SortField(Enum):

    PRIORITY = "priority"
    DEADLINE = "deadline"
    CATEGORY = "category"
    DONE = "complete"
