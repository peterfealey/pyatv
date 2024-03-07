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
class SendPackedVirtualTouchEventMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Phase:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _PhaseEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[SendPackedVirtualTouchEventMessage._Phase.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        Began: SendPackedVirtualTouchEventMessage._Phase.ValueType  # 1
        Moved: SendPackedVirtualTouchEventMessage._Phase.ValueType  # 2
        Stationary: SendPackedVirtualTouchEventMessage._Phase.ValueType  # 3
        Ended: SendPackedVirtualTouchEventMessage._Phase.ValueType  # 4
        Cancelled: SendPackedVirtualTouchEventMessage._Phase.ValueType  # 5

    class Phase(_Phase, metaclass=_PhaseEnumTypeWrapper):
        """Corresponds to "phase" in data"""

    Began: SendPackedVirtualTouchEventMessage.Phase.ValueType  # 1
    Moved: SendPackedVirtualTouchEventMessage.Phase.ValueType  # 2
    Stationary: SendPackedVirtualTouchEventMessage.Phase.ValueType  # 3
    Ended: SendPackedVirtualTouchEventMessage.Phase.ValueType  # 4
    Cancelled: SendPackedVirtualTouchEventMessage.Phase.ValueType  # 5

    DATA_FIELD_NUMBER: builtins.int
    data: builtins.bytes
    """The packed version of VirtualTouchEvent contains X, Y, phase, deviceID
    and finger stored as a byte array. Each value is written as 16bit little
    endian integers.
    """
    def __init__(
        self,
        *,
        data: builtins.bytes | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["data", b"data"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["data", b"data"]) -> None: ...

global___SendPackedVirtualTouchEventMessage = SendPackedVirtualTouchEventMessage

SENDPACKEDVIRTUALTOUCHEVENTMESSAGE_FIELD_NUMBER: builtins.int
sendPackedVirtualTouchEventMessage: google.protobuf.internal.extension_dict._ExtensionFieldDescriptor[pyatv.protocols.mrp.protobuf.ProtocolMessage_pb2.ProtocolMessage, global___SendPackedVirtualTouchEventMessage]