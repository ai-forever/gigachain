from dataclasses import asdict, dataclass
from typing import Any, Dict, List, Optional, Tuple, Type, TypeVar

from dacite import from_dict

Metadata = Dict[str, Any]

Class = TypeVar("Class")


class MissingFunctionsError(Exception):
    def __init__(self, missing: list[str]):
        super().__init__(f"Missing functions: {', '.join(missing)}")
        self.missing = missing


@dataclass
class AsDictMixin:
    def asdict(self, ignore_attrs: Tuple[str, ...] = (), ignore_none: bool = False) -> Dict[str, Any]:
        data = asdict(self)
        if ignore_none:
            data = {k: v for k, v in data.items() if v is not None}
        return {k: v for k, v in data.items() if k not in ignore_attrs}


@dataclass
class FromDictMixin:
    @classmethod
    def from_dict(cls: Type[Class], data: Dict[str, Any]) -> Class:
        return from_dict(data_class=cls, data=data)


@dataclass
class FunctionDef(AsDictMixin, FromDictMixin):
    name: str
    description: Optional[str] = None
    parameters: Optional[Dict[str, Any]] = None
    return_parameters: Optional[Dict[str, Any]] = None
    few_shot_examples: Optional[List[Dict[str, Any]]] = None


@dataclass
class FunctionResponse(AsDictMixin, FromDictMixin):
    id: int
    name: str
    version: int
    definition: dict
    is_active: bool
    created_at: str
