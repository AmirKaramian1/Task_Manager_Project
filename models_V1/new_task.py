#=========== TASK_MODEL ==========


from datetime import datetime, timedelta
from pydantic import BaseModel, Field, field_validator
from typing import Optional
from utils import format_deadline, parse_deadline


from .new_models import Category, Priority, SortField



class Task(BaseModel):

    # Model_Settings

    model_config = {'validate_assignment': True, 'extra' : 'forbid'}


    title : str = Field(..., min_length=3, max_length=100, description="Title of the task")

    description : Optional[str] = None

    complete : bool = False

    deadline : datetime

    category : Category

    priority : Priority


    def complete_it(self):

        self.complete = True


    @property
    def reaming_time(self):

        now = datetime.now()

        reaming_time = self.deadline - now

        if reaming_time.total_seconds() <= 0:

            return f"deadline passed : {-reaming_time}"
        
        return reaming_time

    
    #====== Field_Validator ======


    @field_validator("deadline")
    @classmethod
    
    def check_due_time(cls, value : datetime):

        now = datetime.now()

        if value < now :

            raise ValueError("deadline cant be in the past.")
        
        return value
    

    def __str__(self):
        
        if not self.complete:

            new_deadline = format_deadline(self.deadline)


            return f"{self.title} has to complete until {new_deadline} and its importancity is {self.priority.name} : {self.description}, category : {self.category.name}"
        
        if self.complete:

            return f"{self.title} has completed"