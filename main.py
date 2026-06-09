from models_V1 import Category, Priority, SortField, Task
from utils import format_deadline, parse_deadline
from services import TaskManager


def main():

    #======JUST_FOR_TEST========     
        

    gym_cat = Category(name="exercise")

    school_cat = Category(name="schooL and study")

    school_deadline = parse_deadline("2030/11/15 23:55")

    gym_deadline = parse_deadline("2026/05/20 16:00")

    task1 = Task(title="Gym", description="its good", deadline=school_deadline, priority=Priority.MEDIUM, category=gym_cat)

    task2 = Task(title="School", description="its terrible", deadline=school_deadline, priority=Priority.LOW, category=school_cat)

    task3= Task(title="School", description="its terrible", deadline=school_deadline, priority=Priority.LOW, category=gym_cat)



    my_manager = TaskManager()


    my_manager.add_task(task=task1)
    my_manager.add_task(task=task2)
    my_manager.add_task(task=task3)

    my_manager.done_task(task=task3)

    my_manager.find_task("School")

    my_manager.sort_task(SortField.DEADLINE)


    re_time = task3.reaming_time

    print(re_time)



if __name__ == "__main__":

    main()