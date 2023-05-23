from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Credentials(_message.Message):
    __slots__ = ["username", "password"]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    username: str
    password: str
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class GetUserRequest(_message.Message):
    __slots__ = ["username"]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    username: str
    def __init__(self, username: _Optional[str] = ...) -> None: ...

class UserResponse(_message.Message):
    __slots__ = ["username", "result"]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    username: str
    result: _containers.RepeatedCompositeFieldContainer[Carda]
    def __init__(self, username: _Optional[str] = ..., result: _Optional[_Iterable[_Union[Carda, _Mapping]]] = ...) -> None: ...

class AddCardRequest(_message.Message):
    __slots__ = ["username", "id", "name", "health", "attack", "defense"]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    HEALTH_FIELD_NUMBER: _ClassVar[int]
    ATTACK_FIELD_NUMBER: _ClassVar[int]
    DEFENSE_FIELD_NUMBER: _ClassVar[int]
    username: str
    id: str
    name: str
    health: str
    attack: str
    defense: str
    def __init__(self, username: _Optional[str] = ..., id: _Optional[str] = ..., name: _Optional[str] = ..., health: _Optional[str] = ..., attack: _Optional[str] = ..., defense: _Optional[str] = ...) -> None: ...

class RegisterCredentials(_message.Message):
    __slots__ = ["mail", "username", "password"]
    MAIL_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    mail: str
    username: str
    password: str
    def __init__(self, mail: _Optional[str] = ..., username: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class Response(_message.Message):
    __slots__ = ["code", "message"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    code: int
    message: str
    def __init__(self, code: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...

class Carda(_message.Message):
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
