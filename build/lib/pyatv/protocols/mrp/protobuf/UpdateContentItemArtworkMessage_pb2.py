# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyatv/protocols/mrp/protobuf/UpdateContentItemArtworkMessage.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyatv.protocols.mrp.protobuf import ProtocolMessage_pb2 as pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2
from pyatv.protocols.mrp.protobuf import ContentItem_pb2 as pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_ContentItem__pb2
from pyatv.protocols.mrp.protobuf import PlayerPath_pb2 as pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_PlayerPath__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nBpyatv/protocols/mrp/protobuf/UpdateContentItemArtworkMessage.proto\x1a\x32pyatv/protocols/mrp/protobuf/ProtocolMessage.proto\x1a.pyatv/protocols/mrp/protobuf/ContentItem.proto\x1a-pyatv/protocols/mrp/protobuf/PlayerPath.proto\"f\n\x1fUpdateContentItemArtworkMessage\x12\"\n\x0c\x63ontentItems\x18\x01 \x03(\x0b\x32\x0c.ContentItem\x12\x1f\n\nplayerPath\x18\x02 \x01(\x0b\x32\x0b.PlayerPath:[\n\x1fupdateContentItemArtworkMessage\x12\x10.ProtocolMessage\x18= \x01(\x0b\x32 .UpdateContentItemArtworkMessage')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pyatv.protocols.mrp.protobuf.UpdateContentItemArtworkMessage_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2.ProtocolMessage.RegisterExtension(updateContentItemArtworkMessage)

  DESCRIPTOR._options = None
  _globals['_UPDATECONTENTITEMARTWORKMESSAGE']._serialized_start=217
  _globals['_UPDATECONTENTITEMARTWORKMESSAGE']._serialized_end=319
# @@protoc_insertion_point(module_scope)