# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyatv/protocols/mrp/protobuf/ContentItem.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyatv.protocols.mrp.protobuf import ContentItemMetadata_pb2 as pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_ContentItemMetadata__pb2
from pyatv.protocols.mrp.protobuf import LanguageOption_pb2 as pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_LanguageOption__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.pyatv/protocols/mrp/protobuf/ContentItem.proto\x1a\x36pyatv/protocols/mrp/protobuf/ContentItemMetadata.proto\x1a\x31pyatv/protocols/mrp/protobuf/LanguageOption.proto\"\x8c\x01\n\x13LanguageOptionGroup\x12\x1b\n\x13\x61llowEmptySelection\x18\x01 \x01(\x08\x12.\n\x15\x64\x65\x66\x61ultLanguageOption\x18\x02 \x01(\x0b\x32\x0f.LanguageOption\x12(\n\x0flanguageOptions\x18\x03 \x03(\x0b\x32\x0f.LanguageOption\"\xf4\x02\n\x0b\x43ontentItem\x12\x12\n\nidentifier\x18\x01 \x01(\t\x12&\n\x08metadata\x18\x02 \x01(\x0b\x32\x14.ContentItemMetadata\x12\x13\n\x0b\x61rtworkData\x18\x03 \x01(\x0c\x12\x0c\n\x04info\x18\x04 \x01(\t\x12\x36\n\x18\x61vailableLanguageOptions\x18\x05 \x03(\x0b\x32\x14.LanguageOptionGroup\x12/\n\x16\x63urrentLanguageOptions\x18\x06 \x03(\x0b\x32\x0f.LanguageOption\x12\x18\n\x10parentIdentifier\x18\t \x01(\t\x12\x1a\n\x12\x61ncestorIdentifier\x18\n \x01(\t\x12\x17\n\x0fqueueIdentifier\x18\x0b \x01(\t\x12\x19\n\x11requestIdentifier\x18\x0c \x01(\t\x12\x18\n\x10\x61rtworkDataWidth\x18\r \x01(\x05\x12\x19\n\x11\x61rtworkDataHeight\x18\x0e \x01(\x05')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pyatv.protocols.mrp.protobuf.ContentItem_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_LANGUAGEOPTIONGROUP']._serialized_start=158
  _globals['_LANGUAGEOPTIONGROUP']._serialized_end=298
  _globals['_CONTENTITEM']._serialized_start=301
  _globals['_CONTENTITEM']._serialized_end=673
# @@protoc_insertion_point(module_scope)