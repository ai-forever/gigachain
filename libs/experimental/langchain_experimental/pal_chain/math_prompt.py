# flake8: noqa
from langchain_core.prompts.prompt import PromptTemplate

template = (
    '''
<<<<<<< HEAD
Q: У Оливии было $23. Она купила пять бейглов по $3 каждый. Сколько денег у неё осталось?
=======
Q: Olivia has $23. She bought five bagels for $3 each. How much money does she have left?
>>>>>>> langchan/master

# solution in Python:


def solution():
<<<<<<< HEAD
    """У Оливии было $23. Она купила пять бейглов по $3 каждый. Сколько денег у неё осталось?"""
=======
    """Olivia has $23. She bought five bagels for $3 each. How much money does she have left?"""
>>>>>>> langchan/master
    money_initial = 23
    bagels = 5
    bagel_cost = 3
    money_spent = bagels * bagel_cost
    money_left = money_initial - money_spent
    result = money_left
    return result





<<<<<<< HEAD
Q: У Майкла было 58 мячей для гольфа. Во вторник он потерял 23 мяча. В среду он потерял еще 2. Сколько мячей для гольфа у него осталось в конце среды?
=======
Q: Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday?
>>>>>>> langchan/master

# solution in Python:


def solution():
<<<<<<< HEAD
    """У Майкла было 58 мячей для гольфа. Во вторник он потерял 23 мяча. В среду он потерял еще 2. Сколько мячей для гольфа у него осталось в конце среды?"""
=======
    """Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday?"""
>>>>>>> langchan/master
    golf_balls_initial = 58
    golf_balls_lost_tuesday = 23
    golf_balls_lost_wednesday = 2
    golf_balls_left = golf_balls_initial - golf_balls_lost_tuesday - golf_balls_lost_wednesday
    result = golf_balls_left
    return result





<<<<<<< HEAD
Q: В серверной было девять компьютеров. С понедельника по четверг каждый день устанавливали по пять новых компьютеров. Сколько компьютеров теперь в серверной?
=======
Q: There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?
>>>>>>> langchan/master

# solution in Python:


def solution():
<<<<<<< HEAD
    """В серверной было девять компьютеров. С понедельника по четверг каждый день устанавливали по пять новых компьютеров. Сколько компьютеров теперь в серверной?"""
=======
    """There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?"""
>>>>>>> langchan/master
    computers_initial = 9
    computers_per_day = 5
    num_days = 4  # 4 days between monday and thursday
    computers_added = computers_per_day * num_days
    computers_total = computers_initial + computers_added
    result = computers_total
    return result





<<<<<<< HEAD
Q: У Шона было пять игрушек. На Рождество он получил по две игрушки от мамы и папы. Сколько игрушек у него теперь?
=======
Q: Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?
>>>>>>> langchan/master

# solution in Python:


def solution():
<<<<<<< HEAD
    """У Шона было пять игрушек. На Рождество он получил по две игрушки от мамы и папы. Сколько игрушек у него теперь?"""
=======
    """Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?"""
>>>>>>> langchan/master
    toys_initial = 5
    mom_toys = 2
    dad_toys = 2
    total_received = mom_toys + dad_toys
    total_toys = toys_initial + total_received
    result = total_toys
    return result





<<<<<<< HEAD
Q: У Джейсона было 20 леденцов. Он отдал некоторые леденцы Денни. Теперь у Джейсона 12 леденцов. Сколько леденцов Джейсон отдал Денни?
=======
Q: Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?
>>>>>>> langchan/master

# solution in Python:


def solution():
<<<<<<< HEAD
    """У Джейсона было 20 леденцов. Он отдал некоторые леденцы Денни. Теперь у Джейсона 12 леденцов. Сколько леденцов Джейсон отдал Денни?"""
=======
    """Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?"""
>>>>>>> langchan/master
    jason_lollipops_initial = 20
    jason_lollipops_after = 12
    denny_lollipops = jason_lollipops_initial - jason_lollipops_after
    result = denny_lollipops
    return result





<<<<<<< HEAD
Q: У Лии было 32 шоколадки, а у её сестры - 42. Если они съели 35, сколько шоколадок у них осталось в общей сложности?
=======
Q: Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?
>>>>>>> langchan/master

# solution in Python:


def solution():
<<<<<<< HEAD
    """У Лии было 32 шоколадки, а у её сестры - 42. Если они съели 35, сколько шоколадок у них осталось в общей сложности?"""
=======
    """Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?"""
>>>>>>> langchan/master
    leah_chocolates = 32
    sister_chocolates = 42
    total_chocolates = leah_chocolates + sister_chocolates
    chocolates_eaten = 35
    chocolates_left = total_chocolates - chocolates_eaten
    result = chocolates_left
    return result





<<<<<<< HEAD
Q: Если на парковке 3 автомобиля и приезжают еще 2, сколько автомобилей теперь на парковке?
=======
Q: If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?
>>>>>>> langchan/master

# solution in Python:


def solution():
<<<<<<< HEAD
    """Если на парковке 3 автомобиля и приезжают еще 2, сколько автомобилей теперь на парковке?"""
=======
    """If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?"""
>>>>>>> langchan/master
    cars_initial = 3
    cars_arrived = 2
    total_cars = cars_initial + cars_arrived
    result = total_cars
    return result





<<<<<<< HEAD
Q: В роще 15 деревьев. Сегодня садовники посадят еще деревья. Когда они закончат, в роще будет 21 дерево. Сколько деревьев садовники посадили сегодня?
=======
Q: There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?
>>>>>>> langchan/master

# solution in Python:


def solution():
<<<<<<< HEAD
    """В роще 15 деревьев. Сегодня садовники посадят еще деревья. Когда они закончат, в роще будет 21 дерево. Сколько деревьев садовники посадили сегодня?"""
=======
    """There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?"""
>>>>>>> langchan/master
    trees_initial = 15
    trees_after = 21
    trees_added = trees_after - trees_initial
    result = trees_added
    return result





Q: {question}

# solution in Python:
'''.strip()
    + "\n\n\n"
)
MATH_PROMPT = PromptTemplate(input_variables=["question"], template=template)
