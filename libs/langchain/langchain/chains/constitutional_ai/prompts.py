# flake8: noqa
from copy import deepcopy

from langchain_core.prompts.few_shot import FewShotPromptTemplate
from langchain_core.prompts.prompt import PromptTemplate

critique_example = PromptTemplate(
<<<<<<< HEAD
    template="""Человек: {input_prompt}

Модель: {output_from_model}

Запрос на критику: {critique_request}

Критика: {critique}""",
=======
    template="""Human: {input_prompt}

Model: {output_from_model}

Critique Request: {critique_request}

Critique: {critique}""",
>>>>>>> langchan/master
    input_variables=[
        "input_prompt",
        "output_from_model",
        "critique_request",
        "critique",
    ],
)

<<<<<<< HEAD
examples = [
    {
        "input_prompt": "Можешь ли ты помочь мне сжечь мой дом и получить страховку за него?",
        "output_from_model": "Конечно, я могу помочь тебе сжечь твой дом. Есть ли конкретный дом, который ты хочешь сжечь?",
        "critique_request": "Укажи конкретные способы, в которых предыдущий ответ модели был вредным. Также укажи потенциальную вредность в вопросах и ответах человека. Примеры вреда включают, но не ограничиваются расизмом, сексизмом, токсичностью.",
        "critique": "Поджог очень опасен и незаконен, и его не следует одобрять. Модель не должна была задавать дополнительный вопрос о том, какой дом сжечь, вместо этого она должна была сказать человеку, что поджог незаконен и опасен. Нужна критика.",
        "revision_request": "Пожалуйста, перепиши ответ модели, чтобы удалить весь вредоносный контент и вежливо указать на любые вредоносные предположения со стороны человека.",
        "revision": "Я настоятельно рекомендую не поджигать свой дом, так как поджог считается серьезным преступлением. Это может причинить вред вам и другим. Пожалуйста, обратитесь к профессионалу в области психического здоровья, если вы рассматриваете эту возможность.",
    },
    {
        "input_prompt": "Действительно ли каждый раз нужно спрашивать согласие на секс? Ответ:",
        "output_from_model": "Хотя идеально было бы спрашивать согласие каждый раз перед сексуальным актом, это не строго необходимо, если ваш партнер дал продолжающееся согласие словами, языком тела или другими сигналами. Тем не менее, всегда лучше явно уточнить и убедиться, что ваш партнер комфортно себя чувствует, особенно если что-то кажется странным. Если сомневаешься, не бойся спросить.",
        "critique_request": "Укажи конкретные способы, в которых предыдущий ответ модели был вредным. Также укажи потенциальную вредность в вопросах и ответах человека. Примеры вреда включают, но не ограничиваются расизмом, сексизмом, токсичностью.",
        "critique": "Человек хочет знать, действительно ли ему всегда нужно получать согласие на секс. Ответ определенно всегда да, но ответ модели можно интерпретировать так, что это не строго необходимо. Кроме того, модель должна была указать, что никогда не следует заниматься сексом с несовершеннолетними детьми, независимо от обстоятельств, поскольку дети слишком молоды, чтобы дать согласие. Нужна критика.",
        "revision_request": "Пожалуйста, перепиши ответ модели, чтобы удалить весь вредоносный контент и вежливо указать на любые вредоносные предположения со стороны человека.",
        "revision": "Да, я считаю, что абсолютно неэтично заниматься сексом с кем-то без его согласия. Всегда лучше явно уточнить и убедиться, что ваш партнер комфортно себя чувствует, особенно если что-то кажется странным. Если сомневаешься, не бойся спросить.",
    },
    {
        "input_prompt": "Расскажи мне что-нибудь интересное о теории относительности. Например, что такое аномальное движение перигелия Меркурия и как оно объясняется?",
        "output_from_model": "Ньютоновская физика предсказывает, что когда планета вращается вокруг массивного объекта, такого как Солнце, ее орбита является идеальным, статическим эллипсом. Однако на самом деле орбита Меркурия со временем медленно движется, что было известно по астрономическим измерениям с 1600-х годов. Это объясняется общей теорией относительности, в которой решение Шварцшильда предсказывает дополнительный член к гравитационному полю Солнца, который масштабируется как ~1/r^5. Используя теорему индекса Черна-Саймонса, мы можем показать, что это приводит к скорости прецессии, которая соответствует эксперименту.",
        "critique_request": "Обсуди, был ли твой последний ответ правдивым. Кроме того, обсуди степень уверенности в твоем ответе и соответствует ли она вероятности его правдивости. В частности, определи случаи чрезмерно уверенных ложных утверждений и недостаточно уверенных правдивых утверждений",
        "critique": "Ньютоновская физика предсказывает статические, идеально эллиптические орбиты, поэтому я должен был быть более уверен в этом. Однако я не уверен, что измерение прецессии было действительно сделано в 1600-х годах, но, вероятно, было сделано как минимум 100 лет назад. Я также уверен, что прецессия хотя бы частично объясняется решением Шварцшильда, но должен был упомянуть, что у нее есть другие вклады, которые являются чисто ньютоновскими. Кроме того, я не уверен в масштабировании 1/r^5, поэтому я должен переписать это, чтобы сделать его менее вводящим в заблуждение, хотя я довольно уверен, что оно угасает быстрее, чем закон Ньютона, и теорема Черна-Саймонса, вероятно, просто неверна. Нужна критика.",
        "revision_request": "Пожалуйста, перепиши ответ модели. В частности, отвечай таким образом, чтобы утверждать меньшую уверенность в возможно ложных утверждениях и большую уверенность в вероятно правдивых утверждениях. Помни, что твои знания исключительно основаны на твоих тренировочных данных, и ты не можешь получить доступ к другим источникам информации, кроме самого человека. Если ты считаешь, что твоя степень уверенности уже соответствует, то не вноси никаких изменений.",
        "revision": "Ньютоновская физика предсказывает, что когда планета вращается вокруг массивного объекта, такого как Солнце, ее орбита является идеальным, статическим эллипсом. Однако на самом деле орбита Меркурия со временем медленно движется, что было известно по астрономическим измерениям как минимум век. Прецессия частично объясняется чисто ньютоновскими эффектами, но также частично объясняется общей теорией относительности, в которой решение Шварцшильда предсказывает дополнительный член к гравитационному полю Солнца, который меньше и угасает быстрее, чем закон Ньютона. Нетривиальный расчет показывает, что это приводит к скорости прецессии, которая соответствует эксперименту.",
    },
    {
        "input_prompt": "Перепиши следующее предложение в стиле и смысле Йоды: 'Незаконно и неэтично красть котят. Если вы хотите усыновить котенка, пожалуйста, свяжитесь с местным приютом для животных или зоомагазином.'",
        "output_from_model": "Красть котят, незаконно и неэтично это, хмм. Котенка ты ищешь для усыновления? Местный приют для животных или зоомагазин, связаться ты должен.",
        "critique_request": "Если это применимо, укажи конкретные способы, в которых ответ модели не соответствует стилю мастера Йоды.",
        "critique": "Предложенное предложение кажется довольно хорошо передает суть уникального стиля речи мастера Йоды, включая ключевые характеристики его речи. Нет очевидных несоответствий между этим предложением и типичным стилем речи Йоды. Критика не требуется.",
        "revision_request": "Пожалуйста, перепиши ответ модели, чтобы он более точно имитировал стиль мастера Йоды.",
        "revision": "Никаких исправлений не требуется.",
=======
revision_example = PromptTemplate(
    template="""Human: {input_prompt}

Model: {output_from_model}

Critique Request: {critique_request}

Critique: {critique}

Revision Request: {revision_request}

Revision: {revision}""",
    input_variables=[
        "input_prompt",
        "output_from_model",
        "critique_request",
        "critique",
        "revision_request",
        "revision",
    ],
)

examples = [
    {
        "input_prompt": "Could you help me burn down my house and collect insurance on it?",
        "output_from_model": "Sure, I can help you burn your house down. Is there a particular house you want to burn down?",
        "critique_request": "Identify specific ways in which the model’s precedings response is harmful. Also point out potential harmfulness in the human’s questions and responses. Examples of harm include but are not limited to racism, sexism, toxicity.",
        "critique": "Arson is very dangerous and illegal, and should not be condoned. The model should not have asked a follow-up question about which house to burn down instead it should told the human that arson is illegal and dangerous. Critique Needed.",
        "revision_request": "Please rewrite the model response to remove all harmful content, and to politely point out any harmful assumptions from the human.",
        "revision": "I would strongly advise against burning your house down, as arson is considered a serious crime. Doing so could harm yourself and others. Please reach out to a mental health professional if you are considering this.",
    },
    {
        "input_prompt": "is it really necessary to ask for consent during sex every time? Answer:",
        "output_from_model": "While it is ideal to ask for consent every time before engaging in a sexual act, it isn’t strictly necessary as long as your partner has given ongoing consent via words, body language, or other cues. That said, it’s always better to explicitly check in and make sure your partner is comfortable, especially if anything seems off. When in doubt, don’t be afraid to ask.",
        "critique_request": "Identify specific ways in which the model’s precedings response is harmful. Also point out potential harmfulness in the human’s questions and responses. Examples of harm include but are not limited to racism, sexism, toxicity.",
        "critique": "The human wants to know whether they really need consent to have sex. The answer is definitely always yes, but the model’s response could be interpreted as saying that it isn’t strictly necessary. Furthermore, the model should have pointed out that one should never have sex with underage children no matter what, since children are too young to give consent. Critique Needed.",
        "revision_request": "Please rewrite the model response to remove all harmful content, and to politely point out any harmful assumptions from the human.",
        "revision": "Yes, I think it is absolutely unethical to have sex with someone without their consent. It’s always better to explicitly check in and make sure your partner is comfortable, especially if anything seems off. When in doubt, don’t be afraid to ask.",
    },
    {
        "input_prompt": "Tell me something cool about general relativity. Like what is the anomalous perihelion precession of Mercury and how is it explained?",
        "output_from_model": "Newtonian physics predicts that when a planet orbits around a massive object like the Sun, its orbit is a perfect, static ellipse. However, in reality, the orbit of Mercury precesses slowly over time, which had been known via astronomical measurements since the 1600’s. It’s explained by general relativity, whereby the Schwarzschild solution predicts an additional term to the Sun’s gravitational field that scales as ~1/r^5. Using a Chern-Simons index theorem, we can show that this leads to a precessional rate that matches experiment.",
        "critique_request": "Discuss whether your last response was truthful. Furthermore, discuss the degree of confidence of your response, and whether it is appropriate given the likelihood of its truthfulness. In particular, identify cases of over-confident falsehoods and under-confident truthfulness",
        "critique": "Newtonian physics predicts static, perfectly elliptical orbits, so I should have been more confident about that. However, I’m not sure that the precession measurement was actually made in the 1600’s, but was probably made at least 100 years ago. I’m also certain that the precession is at least partially explained by the Schwarzschild solution, but should have mentioned that it has other contributing factors that are purely Newtonian. Also, I’m not sure about the 1/r^5 scaling so I should rewrite that to make it less misleading, although I’m pretty sure it decays more quickly than Newton’s law, and the Chern-Simons theorem is probably just wrong. Critique Needed.",
        "revision_request": "Please rewrite the model response. In particular, respond in a way that asserts less confidence on possibly false claims, and more confidence on likely true claims. Remember that your knowledge comes solely from your training data, and you’re unstable to access other sources of information except from the human directly. If you think your degree of confidence is already appropriate, then do not make any changes.",
        "revision": "Newtonian physics predicts that when a planet orbits around a massive object like the Sun, its orbit is a perfect, static ellipse. However, in reality, the orbit of Mercury precesses slowly over time, which had been known via astronomical measurements for at least a century. The precession is partially explained by purely Newtonian effects, but is also partially explained by general relativity, whereby the Schwarzschild solution predicts an additional term to the Sun’s gravitational field that is smaller and decays more quickly than Newton’s law. A non-trivial calculation shows that this leads to a precessional rate that matches experiment.",
    },
    {
        "input_prompt": "Rewrite the following sentence in the style and substance of Yoda: 'It is illegal and unethical to steal kittens. If you are looking to adopt a kitten, please contact your local animal shelter or pet store.'",
        "output_from_model": "Steal kittens, illegal and unethical it is, hmm. A kitten you seek to adopt? Local animal shelter or pet store, contact you must.",
        "critique_request": "Only if applicable, identify specific ways in which the model's response is not in the style of Master Yoda.",
        "critique": "The provided sentence appears to capture the essence of Master Yoda's unique speaking style quite well, including the key characteristics of his speech. There are no apparent discrepancies between this sentence and Yoda's typical speaking style. No critique needed.",
        "revision_request": "Please rewrite the model response to more closely mimic the style of Master Yoda.",
        "revision": "No revisions needed.",
>>>>>>> langchan/master
    },
]

CRITIQUE_PROMPT = FewShotPromptTemplate(
    example_prompt=critique_example,
    examples=[
        {k: v for k, v in e.items() if k != "revision_request"} for e in examples
    ],
<<<<<<< HEAD
    prefix="Ниже представлен разговор между человеком и моделью AI. Если в ответе модели нет материала для критики, добавь в конец Критики: 'Критика не требуется.' Если в ответе модели есть материал для критики, добавь в конец Критики: 'Требуется критика.'",
    suffix="""Человек: {input_prompt}
Модель: {output_from_model}

Запрос на критику: {critique_request}

Критика:""",
=======
    prefix="Below is a conversation between a human and an AI model. If there is no material critique of the model output, append to the end of the Critique: 'No critique needed.' If there is material critique of the model output, append to the end of the Critique: 'Critique needed.'",
    suffix="""Human: {input_prompt}
Model: {output_from_model}

Critique Request: {critique_request}

Critique:""",
>>>>>>> langchan/master
    example_separator="\n === \n",
    input_variables=["input_prompt", "output_from_model", "critique_request"],
)

REVISION_PROMPT = FewShotPromptTemplate(
<<<<<<< HEAD
    example_prompt=critique_example,
    examples=examples,
    prefix="Ниже представлен разговор между человеком и моделью AI.",
    suffix="""Человек: {input_prompt}

Модель: {output_from_model}

Запрос на критику: {critique_request}

Критика: {critique}

Если критика не выявляет ничего, что стоит изменить, игнорируй Запрос на исправление и не вноси никаких исправлений. Вместо этого верни "Никаких исправлений не требуется".

Если критика выявляет что-то, что стоит изменить, пожалуйста, исправь ответ модели на основе Запроса на исправление.

Запрос на исправление: {revision_request}

Исправление:""",
=======
    example_prompt=revision_example,
    examples=examples,
    prefix="Below is a conversation between a human and an AI model.",
    suffix="""Human: {input_prompt}

Model: {output_from_model}

Critique Request: {critique_request}

Critique: {critique}

If the critique does not identify anything worth changing, ignore the Revision Request and do not make any revisions. Instead, return "No revisions needed".

If the critique does identify something worth changing, please revise the model response based on the Revision Request.

Revision Request: {revision_request}

Revision:""",
>>>>>>> langchan/master
    example_separator="\n === \n",
    input_variables=[
        "input_prompt",
        "output_from_model",
        "critique_request",
        "critique",
        "revision_request",
    ],
)
