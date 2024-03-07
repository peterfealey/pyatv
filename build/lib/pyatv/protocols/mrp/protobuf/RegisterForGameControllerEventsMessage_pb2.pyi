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
class RegisterForGameControllerEventsMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _InputModeFlags:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _InputModeFlagsEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[RegisterForGameControllerEventsMessage._InputModeFlags.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        Motion: RegisterForGameControllerEventsMessage._InputModeFlags.ValueType  # 1
        Buttons: RegisterForGameControllerEventsMessage._InputModeFlags.ValueType  # 2
        Digitizer: RegisterForGameControllerEventsMessage._InputModeFlags.ValueType  # 3

    class InputModeFlags(_InputModeFlags, metaclass=_InputModeFlagsEnumTypeWrapper): ...
    Motion: RegisterForGameControllerEventsMessage.InputModeFlags.ValueType  # 1
    Buttons: RegisterForGameControllerEventsMessage.InputModeFlags.ValueType  # 2
    Digitizer: RegisterForGameControllerEventsMessage.InputModeFlags.ValueType  # 3

    INPUTMODEFLAGS_FIELD_NUMBER: builtins.int
    inputModeFlags: global___RegisterForGameControllerEventsMessage.InputModeFlags.ValueType
    def __init__(
        self,
        *,
        inputModeFlags: global___RegisterForGameControllerEventsMessage.InputModeFlags.ValueType | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["inputModeFlags", b"inputModeFlags"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["inputModeFlags", b"inputModeFlags"]) -> None: ...

global___RegisterForGameControllerEventsMessage = RegisterForGameControllerEventsMessage

REGISTERFORGAMECONTROLLEREVENTSMESSAGE_FIELD_NUMBER: builtins.int
registerForGameControllerEventsMessage: google.protobuf.internal.extension_dict._ExtensionFieldDescriptor[pyatv.protocols.mrp.protobuf.ProtocolMessage_pb2.ProtocolMessage, global___RegisterForGameControllerEventsMessage]