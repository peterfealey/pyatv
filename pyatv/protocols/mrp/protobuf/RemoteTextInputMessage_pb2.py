# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyatv/protocols/mrp/protobuf/RemoteTextInputMessage.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyatv.protocols.mrp.protobuf import ProtocolMessage_pb2 as pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9pyatv/protocols/mrp/protobuf/RemoteTextInputMessage.proto\x1a\x32pyatv/protocols/mrp/protobuf/ProtocolMessage.proto\"J\n\x16RemoteTextInputMessage\x12\x11\n\ttimestamp\x18\x01 \x01(\x01\x12\x0f\n\x07version\x18\x02 \x01(\x04\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c:I\n\x16remoteTextInputMessage\x12\x10.ProtocolMessage\x18G \x01(\x0b\x32\x17.RemoteTextInputMessage')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pyatv.protocols.mrp.protobuf.RemoteTextInputMessage_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2.ProtocolMessage.RegisterExtension(remoteTextInputMessage)

  DESCRIPTOR._options = None
  _globals['_REMOTETEXTINPUTMESSAGE']._serialized_start=113
  _globals['_REMOTETEXTINPUTMESSAGE']._serialized_end=187
# @@protoc_insertion_point(module_scope)
