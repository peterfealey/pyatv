"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.internal.extension_dict
import google.protobuf.message
import pyatv.protocols.mrp.protobuf.ProtocolMessage_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class ActionType(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Enum:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _EnumEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[ActionType._Enum.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        Unknown: ActionType._Enum.ValueType  # 0
        Insert: ActionType._Enum.ValueType  # 1
        Set: ActionType._Enum.ValueType  # 2
        Delete: ActionType._Enum.ValueType  # 3
        ClearAction: ActionType._Enum.ValueType  # 4
        """"Clear" clashes with something, making mypy unhappy"""

    class Enum(_Enum, metaclass=_EnumEnumTypeWrapper): ...
    Unknown: ActionType.Enum.ValueType  # 0
    Insert: ActionType.Enum.ValueType  # 1
    Set: ActionType.Enum.ValueType  # 2
    Delete: ActionType.Enum.ValueType  # 3
    ClearAction: ActionType.Enum.ValueType  # 4
    """"Clear" clashes with something, making mypy unhappy"""

    def __init__(
        self,
    ) -> None: ...

global___ActionType = ActionType

@typing_extensions.final
class TextInputMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TIMESTAMP_FIELD_NUMBER: builtins.int
    TEXT_FIELD_NUMBER: builtins.int
    ACTIONTYPE_FIELD_NUMBER: builtins.int
    timestamp: builtins.float
    text: builtins.str
    actionType: global___ActionType.Enum.ValueType
    def __init__(
        self,
        *,
        timestamp: builtins.float | None = ...,
        text: builtins.str | None = ...,
        actionType: global___ActionType.Enum.ValueType | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["actionType", b"actionType", "text", b"text", "timestamp", b"timestamp"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["actionType", b"actionType", "text", b"text", "timestamp", b"timestamp"]) -> None: ...

global___TextInputMessage = TextInputMessage

TEXTINPUTMESSAGE_FIELD_NUMBER: builtins.int
textInputMessage: google.protobuf.internal.extension_dict._ExtensionFieldDescriptor[pyatv.protocols.mrp.protobuf.ProtocolMessage_pb2.ProtocolMessage, global___TextInputMessage]
