#========TASK_MODEL=========


from dataclasses import dataclass
from datetime import datetime, date, timedelta

from models.other_models import Category, Priority
from utils import format_deadline, parse_deadline


@dataclass
class Task:

    title : str

    description : str

    category : Category

    _deadline : datetime

    priority : Priority

    _complete : bool = False


    @property
    def complete(self):

        return "Done" if self._complete else "Not Done..."
    
    @complete.setter
    def complete(self, status : bool) -> None:

        if not isinstance(status, bool):

            raise TypeError("status must be bool")
        
        self._complete = status

    @property
    def reaming_time(self):

        now = datetime.now()

        reaming_time = self.deadline - now

        if reaming_time.total_seconds() <= 0:

            return f"deadline passed : {-reaming_time}"
        
        return reaming_time

    @property
    def deadline(self):

        return self._deadline

    @deadline.setter
    def deadline(self, due_time : datetime):

        if not isinstance(due_time, datetime):

            raise TypeError("Time must be a datetime object.")
        
        self._deadline = due_time


    def __post_init__(self):

        if not self.title.strip():

            raise TypeError("title cant be empty.")
        
    
    def __str__(self):
        
        if not self._complete:

            new_deadline = format_deadline(self.deadline)


            return f"{self.title} has to complete until {new_deadline} and its importancity is {self.priority.name} : {self.description}, category : {self.category}"
        
        if self._complete:

            return f"{self.title} has completed"