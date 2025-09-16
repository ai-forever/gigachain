"""Dataclasses describing TagMe function definitions and responses."""

from dataclasses import asdict, dataclass, field
from typing import Any, Callable, Dict, List, Optional, Tuple, Type, TypeVar

from dacite import from_dict

Metadata = Dict[str, Any]
RoleType = str

Class = TypeVar("Class")


class MissingFunctionsError(Exception):
    """Raised when requested function references are absent on the TagMe server."""

    def __init__(self, missing: list[str]):
        super().__init__(f"Missing functions: {', '.join(missing)}")
        self.missing = missing


@dataclass
class AsDictMixin:
    """Mixin that provides a convenient ``asdict`` helper with filtering options."""

    def asdict(self, ignore_attrs: Tuple[str, ...] = (), ignore_none: bool = False) -> Dict[str, Any]:
        """Return dataclass fields as a dictionary, optionally cleaning up values."""

        data = asdict(self)
        if ignore_none:
            data = {k: v for k, v in data.items() if v is not None}
        return {k: v for k, v in data.items() if k not in ignore_attrs}


@dataclass
class FromDictMixin:
    """Mixin that instantiates a dataclass from a raw dictionary payload."""

    @classmethod
    def from_dict(cls: Type[Class], data: Dict[str, Any]) -> Class:
        """Create a dataclass instance from a dictionary using ``dacite`` conversion."""

        return from_dict(data_class=cls, data=data)


@dataclass
class FunctionDef(AsDictMixin, FromDictMixin):
    """Description of a function exposed to TagMe for grounding LLM responses."""

    name: str
    description: Optional[str] = None
    parameters: Optional[Dict[str, Any]] = None
    return_parameters: Optional[Dict[str, Any]] = None
    few_shot_examples: Optional[List[Dict[str, Any]]] = None


@dataclass
class FunctionCall(AsDictMixin, FromDictMixin):
    """Function invocation data attached to assistant messages."""

    name: str
    arguments: Dict[str, Any] = field(default_factory=dict)


@dataclass
class FunctionResult(AsDictMixin, FromDictMixin):
    """Serialized function execution result returned."""

    name: str
    result: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ChatMessage(AsDictMixin, FromDictMixin):
    """Simplified chat message representation."""

    role: RoleType
    content: Optional[str] = None
    function_call: Optional[FunctionCall] = None
    function_result: Optional[FunctionResult] = None


@dataclass
class DialogData(AsDictMixin, FromDictMixin):
    """Payload containing chat messages and optional metadata for TagMe."""

    input: List[ChatMessage]
    metadata: Optional[Dict[str, Any]] = None


@dataclass
class FunctionResponse(AsDictMixin, FromDictMixin):
    """Function metadata returned by TagMe when querying the available catalog."""

    id: int
    name: str
    version: int
    definition: dict
    is_active: bool
    created_at: str


DialogTransformFunction = Callable[..., DialogData]
