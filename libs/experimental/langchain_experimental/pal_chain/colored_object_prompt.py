# flake8: noqa
from langchain_core.prompts.prompt import PromptTemplate

template = (
    """
<<<<<<< HEAD
# Генерация кода Python3 для решения задач
# Q: На тумбочке находятся красный карандаш, фиолетовая кружка, бордовый брелок, розовый мишка, черная тарелка и синий мяч для снятия стресса. Какого цвета мяч для снятия стресса?
# Поместим объекты в словарь для быстрого поиска
=======
# Generate Python3 Code to solve problems
# Q: On the nightstand, there is a red pencil, a purple mug, a burgundy keychain, a fuchsia teddy bear, a black plate, and a blue stress ball. What color is the stress ball?
# Put objects into a dictionary for quick look up
>>>>>>> langchan/master
objects = dict()
objects['pencil'] = 'red'
objects['mug'] = 'purple'
objects['keychain'] = 'burgundy'
objects['teddy bear'] = 'fuchsia'
objects['plate'] = 'black'
objects['stress ball'] = 'blue'

<<<<<<< HEAD
# Найдем цвет мяча для снятия стресса
=======
# Look up the color of stress ball
>>>>>>> langchan/master
stress_ball_color = objects['stress ball']
answer = stress_ball_color


<<<<<<< HEAD
# Q: На столе вы видите ряд объектов: фиолетовую скрепку, розовый мяч для снятия стресса, коричневый брелок, зеленый зарядный кабель, малиновый спиннер и бордовую ручку. Какого цвета объект сразу справа от мяча для снятия стресса?
# Поместим объекты в список для сохранения порядка
=======
# Q: On the table, you see a bunch of objects arranged in a row: a purple paperclip, a pink stress ball, a brown keychain, a green scrunchiephone charger, a mauve fidget spinner, and a burgundy pen. What is the color of the object directly to the right of the stress ball?
# Put objects into a list to record ordering
>>>>>>> langchan/master
objects = []
objects += [('paperclip', 'purple')] * 1
objects += [('stress ball', 'pink')] * 1
objects += [('keychain', 'brown')] * 1
objects += [('scrunchiephone charger', 'green')] * 1
objects += [('fidget spinner', 'mauve')] * 1
objects += [('pen', 'burgundy')] * 1

<<<<<<< HEAD
# Найдем индекс мяча для снятия стресса
=======
# Find the index of the stress ball
>>>>>>> langchan/master
stress_ball_idx = None
for i, object in enumerate(objects):
    if object[0] == 'stress ball':
        stress_ball_idx = i
        break

<<<<<<< HEAD
# Найдем объект сразу справа
direct_right = objects[i+1]

# Проверим цвет объекта справа
=======
# Find the directly right object
direct_right = objects[i+1]

# Check the directly right object's color
>>>>>>> langchan/master
direct_right_color = direct_right[1]
answer = direct_right_color


<<<<<<< HEAD
# Q: На тумбочке вы видите следующие предметы, расположенные в ряд: бирюзовую тарелку, бордовый брелок, желтый зарядный кабель, оранжевую кружку, розовую тетрадь и серую чашку. Сколько неоранжевых предметов вы видите слева от бирюзового предмета?
# Поместим объекты в список для сохранения порядка
=======
# Q: On the nightstand, you see the following items arranged in a row: a teal plate, a burgundy keychain, a yellow scrunchiephone charger, an orange mug, a pink notebook, and a grey cup. How many non-orange items do you see to the left of the teal item?
# Put objects into a list to record ordering
>>>>>>> langchan/master
objects = []
objects += [('plate', 'teal')] * 1
objects += [('keychain', 'burgundy')] * 1
objects += [('scrunchiephone charger', 'yellow')] * 1
objects += [('mug', 'orange')] * 1
objects += [('notebook', 'pink')] * 1
objects += [('cup', 'grey')] * 1

<<<<<<< HEAD
# Найдем индекс бирюзового предмета
=======
# Find the index of the teal item
>>>>>>> langchan/master
teal_idx = None
for i, object in enumerate(objects):
    if object[1] == 'teal':
        teal_idx = i
        break

<<<<<<< HEAD
# Найдем неоранжевые предметы слева от бирюзового предмета
non_orange = [object for object in objects[:i] if object[1] != 'orange']

# Подсчитаем количество неоранжевых предметов
=======
# Find non-orange items to the left of the teal item
non_orange = [object for object in objects[:i] if object[1] != 'orange']

# Count number of non-orange objects
>>>>>>> langchan/master
num_non_orange = len(non_orange)
answer = num_non_orange


# Q: {question}
""".strip()
    + "\n"
)

COLORED_OBJECT_PROMPT = PromptTemplate(input_variables=["question"], template=template)
