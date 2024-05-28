# flake8: noqa
from langchain_core.prompts.prompt import PromptTemplate

EXAMPLES = [
<<<<<<< HEAD
    """Настройка: Ты сейчас играешь в быстрый раунд TextWorld! Вот твоя задача на
сегодня. Прежде всего, ты можешь, например, попробовать отправиться на восток. После этого, возьми
папку из шкафчика. С папкой, положи папку на каминную полку.
Хорошо, спасибо!

-= Хранилище =-
Ты только что вошел в хранилище. Ты начинаешь оценивать, что здесь есть.

Здесь есть открытый сейф. Какое разочарование! Сейф пуст! Ты разглядываешь полку.
Но на ней ничего нет. Что, ты думаешь, что в TextWorld
должны быть вещи?

Тебе не нравятся двери? Почему бы тебе не попробовать пойти на восток, этот вход не охраняется.

Thought: Мне нужно отправиться на восток
Action: Играть[идти на восток]
Observation: -= Офис =-
Ты прибываешь в офис. Обычный.

Ты можешь разглядеть шкафчик. В шкафчике есть папка. Ты видишь чемодан. Чемодан
пуст, какой ужасный день! Ты прислоняешься к стене, случайно нажимая на секретную кнопку. Стена открывается, открывая каминную полку. Ты задумчиво спрашиваешься, кто оставил это здесь. Каминная полка стандартная. Каминная полка, похоже, пуста. Если ты еще не заметил, кажется, что у стены есть что-то, это стол. К сожалению, на нем ничего нет. Хм. Ну да ладно
Есть выход на запад. Не волнуйся, он не охраняется.

Thought: Мне нужно взять папку из шкафчика
Action: Играть[взять папку]
Observation: Ты берешь папку из шкафчика.

Thought: Мне нужно положить папку на каминную полку
Action: Играть[положить папку на каминную полку]

Observation: Ты кладешь папку на каминную полку.
Твой счет только что увеличился на одно очко.
*** Конец ***
Thought: Произошел Конец
Action: Закончить[да]

"""
]
SUFFIX = """\n\nНастройка: {input}
=======
    """Setup: You are now playing a fast paced round of TextWorld! Here is your task for
today. First of all, you could, like, try to travel east. After that, take the
binder from the locker. With the binder, place the binder on the mantelpiece.
Alright, thanks!

-= Vault =-
You've just walked into a vault. You begin to take stock of what's here.

An open safe is here. What a letdown! The safe is empty! You make out a shelf.
But the thing hasn't got anything on it. What, you think everything in TextWorld
should have stuff on it?

You don't like doors? Why not try going east, that entranceway is unguarded.

Thought: I need to travel east
Action: Play[go east]
Observation: -= Office =-
You arrive in an office. An ordinary one.

You can make out a locker. The locker contains a binder. You see a case. The
case is empty, what a horrible day! You lean against the wall, inadvertently
pressing a secret button. The wall opens up to reveal a mantelpiece. You wonder
idly who left that here. The mantelpiece is standard. The mantelpiece appears to
be empty. If you haven't noticed it already, there seems to be something there
by the wall, it's a table. Unfortunately, there isn't a thing on it. Hm. Oh well
There is an exit to the west. Don't worry, it is unguarded.

Thought: I need to take the binder from the locker
Action: Play[take binder]
Observation: You take the binder from the locker.

Thought: I need to place the binder on the mantelpiece
Action: Play[put binder on mantelpiece]

Observation: You put the binder on the mantelpiece.
Your score has just gone up by one point.
*** The End ***
Thought: The End has occurred
Action: Finish[yes]

"""
]
SUFFIX = """\n\nSetup: {input}
>>>>>>> langchan/master
{agent_scratchpad}"""

TEXTWORLD_PROMPT = PromptTemplate.from_examples(
    EXAMPLES, SUFFIX, ["input", "agent_scratchpad"]
)
