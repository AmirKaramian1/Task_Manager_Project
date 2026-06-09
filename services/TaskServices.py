#==========TASK_MANAGER==========


from datetime import datetime, date, time
from enum import Enum


from models_V1 import Category, Priority, SortField, Task




class TaskManager:

    def __init__(self):
        
        self._tasks = []

    @property
    def tasks (self) -> list:

        return self._tasks.copy()

    
    def done_task(self, task: Task) -> None:

        if task not in self._tasks:

            raise TypeError("task must be a task!")
        
        
        task.complete_it()

    
    def show_tasks(self) -> None:

        for i, task in enumerate(self._tasks, start=1):

            print(f"{i}. {task}")


    def add_task(self, task : Task) -> None:

        if not isinstance(task, Task):

            raise TypeError("task must be a task, creat task first!")
        
        self._tasks.append(task)
        print("task added.")

    def remove_task(self, task : Task) -> None:

        if not isinstance(task, Task):

            raise TypeError("task must be a task")
        
        self.task.remove(task)
        print("task removed.")

    
    def find_task(self, title : str) -> None:

        founded_tasks = [task for task in self._tasks if task.title == title]

        for i, task in enumerate(founded_tasks, start=1):

            print(f"{i}. {task}")

        if len(founded_tasks) < 1:

            raise NotImplementedError("Task not found.")
        
    SORT_KEYS = {"priority" : lambda t: t.priority.value,
                     "deadline" : lambda t: t.deadline,
                     "category" : lambda t: t.category.name,
                     "complete" : lambda t: t.complete}
        

    def sort_task(self, sort_by : SortField, reverse : bool = False):

        try:

            self._tasks.sort(key=self.SORT_KEYS[sort_by.value], reverse=reverse)

            for i, task in enumerate(self._tasks, start=1):

                print(f"{i}. {task}")

        except KeyError:

            raise ValueError(f"Unknown sort field : {sort_by}")
        