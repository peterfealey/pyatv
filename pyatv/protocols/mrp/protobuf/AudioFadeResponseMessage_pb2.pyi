"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.extension_dict
import google.protobuf.message
import pyatv.protocols.mrp.protobuf.ProtocolMessage_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class AudioFadeResponseMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FADEDURATION_FIELD_NUMBER: builtins.int
    fadeDuration: builtins.int
    def __init__(
        self,
        *,
        fadeDuration: builtins.int | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["fadeDuration", b"fadeDuration"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["fadeDuration", b"fadeDuration"]) -> None: ...

global___AudioFadeResponseMessage = AudioFadeResponseMessage

AUDIOFADERESPONSEMESSAGE_FIELD_NUMBER: builtins.int
audioFadeResponseMessage: google.protobuf.internal.extension_dict._ExtensionFieldDescriptor[pyatv.protocols.mrp.protobuf.ProtocolMessage_pb2.ProtocolMessage, global___AudioFadeResponseMessage]