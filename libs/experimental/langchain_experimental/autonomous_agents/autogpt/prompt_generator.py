<<<<<<< HEAD
# ruff: noqa: E501

=======
>>>>>>> langchan/master
import json
from typing import List

from langchain.tools.base import BaseTool

FINISH_NAME = "finish"


class PromptGenerator:
    """Generator of custom prompt strings.

    Does this based on constraints, commands, resources, and performance evaluations.
    """

    def __init__(self) -> None:
        """Initialize the PromptGenerator object.

        Starts with empty lists of constraints, commands, resources,
        and performance evaluations.
        """
        self.constraints: List[str] = []
        self.commands: List[BaseTool] = []
        self.resources: List[str] = []
        self.performance_evaluation: List[str] = []
        self.response_format = {
<<<<<<< HEAD
            "рассуждения": {
                "text": "мысль",
                "reasoning": "рассуждение",
                "plan": "- тезисный план\n- список, который определяет\n- долгосрочный план",
                "criticism": "конструктивная самокритика",
                "speak": "итоговые мысли для передачи пользователю",
            },
            "команда": {"name": "имя команды", "args": {"arg name": "значение"}},
=======
            "thoughts": {
                "text": "thought",
                "reasoning": "reasoning",
                "plan": "- short bulleted\n- list that conveys\n- long-term plan",
                "criticism": "constructive self-criticism",
                "speak": "thoughts summary to say to user",
            },
            "command": {"name": "command name", "args": {"arg name": "value"}},
>>>>>>> langchan/master
        }

    def add_constraint(self, constraint: str) -> None:
        """
        Add a constraint to the constraints list.

        Args:
            constraint (str): The constraint to be added.
        """
        self.constraints.append(constraint)

    def add_tool(self, tool: BaseTool) -> None:
        self.commands.append(tool)

    def _generate_command_string(self, tool: BaseTool) -> str:
        output = f"{tool.name}: {tool.description}"
<<<<<<< HEAD
        output += f", args json schema: {json.dumps(tool.args, ensure_ascii=False)}"
=======
        output += f", args json schema: {json.dumps(tool.args)}"
>>>>>>> langchan/master
        return output

    def add_resource(self, resource: str) -> None:
        """
        Add a resource to the resources list.

        Args:
            resource (str): The resource to be added.
        """
        self.resources.append(resource)

    def add_performance_evaluation(self, evaluation: str) -> None:
        """
        Add a performance evaluation item to the performance_evaluation list.

        Args:
            evaluation (str): The evaluation item to be added.
        """
        self.performance_evaluation.append(evaluation)

    def _generate_numbered_list(self, items: list, item_type: str = "list") -> str:
        """
        Generate a numbered list from given items based on the item_type.

        Args:
            items (list): A list of items to be numbered.
            item_type (str, optional): The type of items in the list.
                Defaults to 'list'.

        Returns:
            str: The formatted numbered list.
        """
        if item_type == "command":
            command_strings = [
                f"{i + 1}. {self._generate_command_string(item)}"
                for i, item in enumerate(items)
            ]
            finish_description = (
<<<<<<< HEAD
                "используй это, чтобы сигнализировать, что вы выполнил все свои задачи"
            )
            finish_args = (
                '"response": "окончательный ответ, чтобы '
                'пользователь узнал, что ты выполнил свои задачи"'
=======
                "use this to signal that you have finished all your objectives"
            )
            finish_args = (
                '"response": "final response to let '
                'people know you have finished your objectives"'
>>>>>>> langchan/master
            )
            finish_string = (
                f"{len(items) + 1}. {FINISH_NAME}: "
                f"{finish_description}, args: {finish_args}"
            )
            return "\n".join(command_strings + [finish_string])
        else:
            return "\n".join(f"{i+1}. {item}" for i, item in enumerate(items))

    def generate_prompt_string(self) -> str:
        """Generate a prompt string.

        Returns:
            str: The generated prompt string.
        """
<<<<<<< HEAD
        formatted_response_format = json.dumps(
            self.response_format, indent=4, ensure_ascii=False
        )
        prompt_string = (
            f"Ограничения:\n{self._generate_numbered_list(self.constraints)}\n\n"
            f"Команды:\n"
            f"{self._generate_numbered_list(self.commands, item_type='command')}\n\n"
            f"Ресурсы:\n{self._generate_numbered_list(self.resources)}\n\n"
            f"Оценка производительности:\n"
            f"{self._generate_numbered_list(self.performance_evaluation)}\n\n"
            f"Ты должен отвечать только в формате JSON, как описано ниже "
            f"\nФормат ответа: \n{formatted_response_format} "
            f"\nУбедись, что ответ можно разобрать с помощью Python json.loads"
=======
        formatted_response_format = json.dumps(self.response_format, indent=4)
        prompt_string = (
            f"Constraints:\n{self._generate_numbered_list(self.constraints)}\n\n"
            f"Commands:\n"
            f"{self._generate_numbered_list(self.commands, item_type='command')}\n\n"
            f"Resources:\n{self._generate_numbered_list(self.resources)}\n\n"
            f"Performance Evaluation:\n"
            f"{self._generate_numbered_list(self.performance_evaluation)}\n\n"
            f"You should only respond in JSON format as described below "
            f"\nResponse Format: \n{formatted_response_format} "
            f"\nEnsure the response can be parsed by Python json.loads"
>>>>>>> langchan/master
        )

        return prompt_string


def get_prompt(tools: List[BaseTool]) -> str:
    """Generates a prompt string.

    It includes various constraints, commands, resources, and performance evaluations.

    Returns:
        str: The generated prompt string.
    """

    # Initialize the PromptGenerator object
    prompt_generator = PromptGenerator()

    # Add constraints to the PromptGenerator object
    prompt_generator.add_constraint(
<<<<<<< HEAD
        "Лимит в ~4000 слов для краткосрочной памяти. "
        "Твоя краткосрочная память короткосрочная, "
        "поэтому немедленно сохраняй важную информацию в файлах."
    )
    prompt_generator.add_constraint(
        "Если ты не уверен, как ты что-то делал ранее "
        "или хочешь вспомнить прошлые события, "
        "мысли о похожих событиях помогут тебе вспомнить."
    )
    prompt_generator.add_constraint("Без помощи пользователя")
    prompt_generator.add_constraint(
        'Используй исключительно команды, перечисленные в двойных кавычках, например, "имя команды"'
=======
        "~4000 word limit for short term memory. "
        "Your short term memory is short, "
        "so immediately save important information to files."
    )
    prompt_generator.add_constraint(
        "If you are unsure how you previously did something "
        "or want to recall past events, "
        "thinking about similar events will help you remember."
    )
    prompt_generator.add_constraint("No user assistance")
    prompt_generator.add_constraint(
        'Exclusively use the commands listed in double quotes e.g. "command name"'
>>>>>>> langchan/master
    )

    # Add commands to the PromptGenerator object
    for tool in tools:
        prompt_generator.add_tool(tool)

    # Add resources to the PromptGenerator object
<<<<<<< HEAD
    prompt_generator.add_resource("Доступ в Интернет для поиска и сбора информации.")
    prompt_generator.add_resource("Управление долгосрочной памятью.")
    prompt_generator.add_resource(
        "Агенты на базе GPT-3.5 для делегирования простых задач."
    )
    prompt_generator.add_resource("Выходной файл.")

    # Add performance evaluations to the PromptGenerator object
    prompt_generator.add_performance_evaluation(
        "Постоянно пересматривай и анализируй свои действия "
        "чтобы убедиться, что вы работаешь на пределе своих возможностей."
    )
    prompt_generator.add_performance_evaluation(
        "Постоянно конструктивно самокритикуй свое поведение в большом масштабе."
    )
    prompt_generator.add_performance_evaluation(
        "Размышляй о прошлых решениях и стратегиях, чтобы усовершенствовать свой подход."
    )
    prompt_generator.add_performance_evaluation(
        "Каждая команда имеет свою цену, поэтому будь умен и эффективен. "
        "Стремись выполнить задачи за минимальное количество шагов."
=======
    prompt_generator.add_resource(
        "Internet access for searches and information gathering."
    )
    prompt_generator.add_resource("Long Term memory management.")
    prompt_generator.add_resource(
        "GPT-3.5 powered Agents for delegation of simple tasks."
    )
    prompt_generator.add_resource("File output.")

    # Add performance evaluations to the PromptGenerator object
    prompt_generator.add_performance_evaluation(
        "Continuously review and analyze your actions "
        "to ensure you are performing to the best of your abilities."
    )
    prompt_generator.add_performance_evaluation(
        "Constructively self-criticize your big-picture behavior constantly."
    )
    prompt_generator.add_performance_evaluation(
        "Reflect on past decisions and strategies to refine your approach."
    )
    prompt_generator.add_performance_evaluation(
        "Every command has a cost, so be smart and efficient. "
        "Aim to complete tasks in the least number of steps."
>>>>>>> langchan/master
    )

    # Generate the prompt string
    prompt_string = prompt_generator.generate_prompt_string()

    return prompt_string
