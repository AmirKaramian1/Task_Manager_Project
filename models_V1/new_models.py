#=======OTHER_MODELS_THAT_HELP_TASK_CLASS=========



from pydantic import BaseModel, Field
from enum import Enum


#=======CATEGORY_MODEL========


class Category(BaseModel):

    name : str = Field(..., min_length=2, max_length=30)


#========PRIORITY_MODEL=========


class Priority(str, Enum):

    LOW = "low"

    MEDIUM = "medium"

    HIGH = "high"


#========SORT_FIELD_CLASS=========


class SortField(str, Enum):

    PRIORITY = "priority"
    DEADLINE = "deadline"
    CATEGORY = "category"
    DONE = "complete"