from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Empty(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SimpleCard(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class FullCard(_message.Message):
    __slots__ = ["id", "name", "health", "attack", "defense"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    HEALTH_FIELD_NUMBER: _ClassVar[int]
    ATTACK_FIELD_NUMBER: _ClassVar[int]
    DEFENSE_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    health: str
    attack: str
    defense: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., health: _Optional[str] = ..., attack: _Optional[str] = ..., defense: _Optional[str] = ...) -> None: ...

class IdCardsResponse(_message.Message):
    __slots__ = ["result"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, result: _Optional[_Iterable[int]] = ...) -> None: ...
