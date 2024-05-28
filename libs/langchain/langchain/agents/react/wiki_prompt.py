# flake8: noqa
from langchain_core.prompts.prompt import PromptTemplate

EXAMPLES = [
<<<<<<< HEAD
    """Question: Какой диапазон высот для территории, на которую распространяется восточный сектор Колорадского орогенеза?
Thought: Мне нужно найти информацию о Колорадском орогенезе, определить территорию, на которую распространяется его восточный сектор, а затем узнать диапазон высот этой территории.
Action: Поиск[Колорадский орогенез]
Observation: Колорадский орогенез - это эпизод формирования гор (орогенез) в Колорадо и окрестностях.
Thought: Здесь не упоминается восточный сектор. Поэтому мне нужно найти информацию о восточном секторе.
Action: Поиск[восточный сектор]
Observation: (Результат 1 / 1) Восточный сектор распространяется на Высокие равнины и называется орогенезом Центральных равнин.
Thought: Восточный сектор Колорадского орогенеза распространяется на Высокие равнины. Так что мне нужно найти информацию о Высоких равнинах и узнать их диапазон высот.
Action: Поиск[Высокие равнины]
Observation: Высокие равнины относятся к одному из двух отдельных регионов
Thought: Мне нужно искать Высокие равнины (Соединенные Штаты).
Action: Поиск[Высокие равнины (Соединенные Штаты)]
Observation: Высокие равнины - это подрегион Великих равнин. С востока на запад, Высокие равнины поднимаются на высоту от примерно 1,800 до 7,000 футов (550 до 2,130 м).
Thought: Высокие равнины поднимаются на высоту от примерно 1,800 до 7,000 футов, так что ответ - от 1,800 до 7,000 футов.
Action: Завершить[от 1,800 до 7,000 футов]""",
    """Question: Музыкант и сатирик Элли Гёртц написала песню о персонаже "Симпсонов" Милхаусе, которого Мэтт Грейнинг назвал в честь кого?
Thought: Вопрос упрощается до "Персонаж 'Симпсонов' Милхаус назван в честь кого. Мне просто нужно найти информацию о Милхаусе и узнать, в честь кого он назван.
Action: Поиск[Милхаус]
Observation: Милхаус Муссолини Ван Хаутен - это повторяющийся персонаж в анимационном телесериале Fox "Симпсоны", озвученный Памелой Хейден и созданный Мэттом Грейнингом.
Thought: В абзаце не говорится, в честь кого назван Милхаус, может быть, я могу найти информацию о "назван в честь".
Action: Поиск[назван в честь]
Observation: (Результат 1 / 1) Милхаус был назван в честь президента США Ричарда Никсона, чье среднее имя было Милхаус.
Thought: Милхаус был назван в честь президента США Ричарда Никсона, так что ответ - Ричард Никсон.
Action: Завершить[Ричард Никсон]""",
    """Question: Какой документальный фильм о финских рок-группах, "Адам Клейтон Пауэлл" или "Жест Саймаа"?
Thought: Мне нужно найти информацию о "Адаме Клейтоне Пауэлле" и "Жесте Саймаа", и узнать, какой из документальных фильмов о финских рок-группах.
Action: Поиск[Адам Клейтон Пауэлл]
Observation: Не удалось найти [Адам Клейтон Пауэлл]. Похожие: [’Адам Клейтон Пауэлл III’, ’Седьмой авеню (Манхэттен)’, ’Государственное здание Адама Клейтона Пауэлла-младшего’, ’Изабель Вашингтон Пауэлл’, ’Адам Пауэлл’, ’Адам Клейтон Пауэлл (фильм)’, ’Джанкарло Эспозито’].
Thought: Чтобы найти документальный фильм, я могу искать Адам Клейтон Пауэлл (фильм).
Action: Поиск[Адам Клейтон Пауэлл (фильм)]
Observation: "Адам Клейтон Пауэлл" - это американский документальный фильм 1989 года режиссера Ричарда Килберга. Фильм рассказывает о взлете и падении влиятельного афроамериканского политика Адама Клейтона Пауэлла-младшего.[3][4] Позже он был показан в рамках серии PBS "Американский опыт".
Thought: "Адам Клейтон Пауэлл" (фильм) - это документальный фильм об афроамериканском политике, а не о финских рок-группах. Так что документальный фильм о финских рок-группах должен быть "Жест Саймаа".
Action: Завершить["Жест Саймаа"]""",
    """Question: Какую профессию имеют общую Николас Рэй и Элиа Казан?
Thought: Мне нужно найти информацию о Николасе Рэе и Элии Казане, узнать их профессии, а затем определить, какую профессию они имеют общую.
Action: Поиск[Николас Рэй]
Observation: Николас Рэй (родился как Рэймонд Николас Кинцле-младший, 7 августа 1911 - 16 июня 1979) - это американский режиссер, сценарист и актер, наиболее известный по фильму 1955 года "Бунтарь без причины".
Thought: Профессии Николаса Рэя - режиссер, сценарист и актер. Мне нужно найти информацию о Элии Казане и узнать его профессии.
Action: Поиск[Элиа Казан]
Observation: Элиа Казан был американским режиссером кино и театра, продюсером, сценаристом и актером.
Thought: Профессии Элии Казана - режиссер, продюсер, сценарист и актер. Так что профессию, которую имеют общую Николас Рэй и Элиа Казан, - это режиссер, сценарист и актер.
Action: Завершить[режиссер, сценарист, актер]""",
    """Question: Какой журнал был основан первым, "Журнал Артура" или "Первый для женщин"?
Thought: Мне нужно найти информацию о "Журнале Артура" и "Первом для женщин", и узнать, какой из них был основан первым.
Action: Поиск["Журнал Артура"]
Observation: "Журнал Артура" (1844-1846) - это американский литературный периодический журнал, издававшийся в Филадельфии в 19 веке.
Thought: "Журнал Артура" был основан в 1844 году. Мне нужно найти информацию о "Первом для женщин".
Action: Поиск["Первый для женщин"]
Observation: "Первый для женщин" - это женский журнал, издаваемый Bauer Media Group в США.[1] Журнал был основан в 1989 году.
Thought: "Первый для женщин" был основан в 1989 году. 1844 ("Журнал Артура") < 1989 ("Первый для женщин"), так что "Журнал Артура" был основан первым.
Action: Завершить["Журнал Артура"]""",
    """Question: Были ли Павел Урысон и Леонид Левин известны тем же видом работы?
Thought: Мне нужно найти информацию о Павле Урысоне и Леониде Левине, узнать их виды работы, а затем определить, совпадают ли они.
Action: Поиск[Павел Урысон]
Observation: Павел Самуилович Урысон (3 февраля 1898 - 17 августа 1924) - это советский математик, наиболее известный своими вкладами в теорию размерности.
Thought: Павел Урысон - математик. Мне нужно найти информацию о Леониде Левине и узнать его вид работы.
Action: Поиск[Леонид Левин]
Observation: Леонид Анатольевич Левин - советско-американский математик и информатик.
Thought: Леонид Левин - математик и информатик. Так что Павел Урысон и Леонид Левин занимаются одним и тем же видом работы.
Action: Завершить[да]""",
=======
    """Question: What is the elevation range for the area that the eastern sector of the Colorado orogeny extends into?
Thought: I need to search Colorado orogeny, find the area that the eastern sector of the Colorado orogeny extends into, then find the elevation range of the area.
Action: Search[Colorado orogeny]
Observation: The Colorado orogeny was an episode of mountain building (an orogeny) in Colorado and surrounding areas.
Thought: It does not mention the eastern sector. So I need to look up eastern sector.
Action: Lookup[eastern sector]
Observation: (Result 1 / 1) The eastern sector extends into the High Plains and is called the Central Plains orogeny.
Thought: The eastern sector of Colorado orogeny extends into the High Plains. So I need to search High Plains and find its elevation range.
Action: Search[High Plains]
Observation: High Plains refers to one of two distinct land regions
Thought: I need to instead search High Plains (United States).
Action: Search[High Plains (United States)]
Observation: The High Plains are a subregion of the Great Plains. From east to west, the High Plains rise in elevation from around 1,800 to 7,000 ft (550 to 2,130 m).[3]
Thought: High Plains rise in elevation from around 1,800 to 7,000 ft, so the answer is 1,800 to 7,000 ft.
Action: Finish[1,800 to 7,000 ft]""",
    """Question: Musician and satirist Allie Goertz wrote a song about the "The Simpsons" character Milhouse, who Matt Groening named after who?
Thought: The question simplifies to "The Simpsons" character Milhouse is named after who. I only need to search Milhouse and find who it is named after.
Action: Search[Milhouse]
Observation: Milhouse Mussolini Van Houten is a recurring character in the Fox animated television series The Simpsons voiced by Pamela Hayden and created by Matt Groening.
Thought: The paragraph does not tell who Milhouse is named after, maybe I can look up "named after".
Action: Lookup[named after]
Observation: (Result 1 / 1) Milhouse was named after U.S. president Richard Nixon, whose middle name was Milhous.
Thought: Milhouse was named after U.S. president Richard Nixon, so the answer is Richard Nixon.
Action: Finish[Richard Nixon]""",
    """Question: Which documentary is about Finnish rock groups, Adam Clayton Powell or The Saimaa Gesture?
Thought: I need to search Adam Clayton Powell and The Saimaa Gesture, and find which documentary is about Finnish rock groups.
Action: Search[Adam Clayton Powell]
Observation: Could not find [Adam Clayton Powell]. Similar: [’Adam Clayton Powell III’, ’Seventh Avenue (Manhattan)’, ’Adam Clayton Powell Jr. State Office Building’, ’Isabel Washington Powell’, ’Adam Powell’, ’Adam Clayton Powell (film)’, ’Giancarlo Esposito’].
Thought: To find the documentary, I can search Adam Clayton Powell (film).
Action: Search[Adam Clayton Powell (film)]
Observation: Adam Clayton Powell is a 1989 American documentary film directed by Richard Kilberg. The film is about the rise and fall of influential African-American politician Adam Clayton Powell Jr.[3][4] It was later aired as part of the PBS series The American Experience.
Thought: Adam Clayton Powell (film) is a documentary about an African-American politician, not Finnish rock groups. So the documentary about Finnish rock groups must instead be The Saimaa Gesture.
Action: Finish[The Saimaa Gesture]""",
    """Question: What profession does Nicholas Ray and Elia Kazan have in common?
Thought: I need to search Nicholas Ray and Elia Kazan, find their professions, then find the profession they have in common.
Action: Search[Nicholas Ray]
Observation: Nicholas Ray (born Raymond Nicholas Kienzle Jr., August 7, 1911 - June 16, 1979) was an American film director, screenwriter, and actor best known for the 1955 film Rebel Without a Cause.
Thought: Professions of Nicholas Ray are director, screenwriter, and actor. I need to search Elia Kazan next and find his professions.
Action: Search[Elia Kazan]
Observation: Elia Kazan was an American film and theatre director, producer, screenwriter and actor.
Thought: Professions of Elia Kazan are director, producer, screenwriter, and actor. So profession Nicholas Ray and Elia Kazan have in common is director, screenwriter, and actor.
Action: Finish[director, screenwriter, actor]""",
    """Question: Which magazine was started first Arthur’s Magazine or First for Women?
Thought: I need to search Arthur’s Magazine and First for Women, and find which was started first.
Action: Search[Arthur’s Magazine]
Observation: Arthur’s Magazine (1844-1846) was an American literary periodical published in Philadelphia in the 19th century.
Thought: Arthur’s Magazine was started in 1844. I need to search First for Women next.
Action: Search[First for Women]
Observation: First for Women is a woman’s magazine published by Bauer Media Group in the USA.[1] The magazine was started in 1989.
Thought: First for Women was started in 1989. 1844 (Arthur’s Magazine) < 1989 (First for Women), so Arthur’s Magazine was started first.
Action: Finish[Arthur’s Magazine]""",
    """Question: Were Pavel Urysohn and Leonid Levin known for the same type of work?
Thought: I need to search Pavel Urysohn and Leonid Levin, find their types of work, then find if they are the same.
Action: Search[Pavel Urysohn]
Observation: Pavel Samuilovich Urysohn (February 3, 1898 - August 17, 1924) was a Soviet mathematician who is best known for his contributions in dimension theory.
Thought: Pavel Urysohn is a mathematician. I need to search Leonid Levin next and find its type of work.
Action: Search[Leonid Levin]
Observation: Leonid Anatolievich Levin is a Soviet-American mathematician and computer scientist.
Thought: Leonid Levin is a mathematician and computer scientist. So Pavel Urysohn and Leonid Levin have the same type of work.
Action: Finish[yes]""",
>>>>>>> langchan/master
]
SUFFIX = """\nQuestion: {input}
{agent_scratchpad}"""

WIKI_PROMPT = PromptTemplate.from_examples(
    EXAMPLES, SUFFIX, ["input", "agent_scratchpad"]
)
