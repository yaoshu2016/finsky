# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: doc_list.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import document_v2_pb2 as document__v2__pb2
import document_v1_pb2 as document__v1__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='doc_list.proto',
  package='DocList',
  syntax='proto2',
  serialized_pb=_b('\n\x0e\x64oc_list.proto\x12\x07\x44ocList\x1a\x11\x64ocument_v2.proto\x1a\x11\x64ocument_v1.proto\"O\n\x0cListResponse\x12\x1f\n\x06\x62ucket\x18\x01 \x03(\x0b\x32\x0f.DocList.Bucket\x12\x1e\n\x03\x64oc\x18\x02 \x03(\x0b\x32\x11.DocumentV2.DocV2\"\x84\x02\n\x06\x42ucket\x12#\n\x08\x64ocument\x18\x01 \x03(\x0b\x32\x11.DocumentV1.DocV1\x12\x13\n\x0bmultiCorpus\x18\x02 \x01(\x08\x12\r\n\x05title\x18\x03 \x01(\t\x12\x0f\n\x07iconUrl\x18\x04 \x01(\t\x12\x17\n\x0f\x66ullContentsUrl\x18\x05 \x01(\t\x12\x11\n\trelevance\x18\x06 \x01(\x01\x12\x18\n\x10\x65stimatedResults\x18\x07 \x01(\x03\x12\x17\n\x0f\x61nalyticsCookie\x18\x08 \x01(\t\x12\x1b\n\x13\x66ullContentsListUrl\x18\t \x01(\t\x12\x13\n\x0bnextPageUrl\x18\n \x01(\t\x12\x0f\n\x07ordered\x18\x0b \x01(\x08\x42+\n com.google.android.finsky.protosB\x07\x44ocList')
  ,
  dependencies=[document__v2__pb2.DESCRIPTOR,document__v1__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_LISTRESPONSE = _descriptor.Descriptor(
  name='ListResponse',
  full_name='DocList.ListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bucket', full_name='DocList.ListResponse.bucket', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='doc', full_name='DocList.ListResponse.doc', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=65,
  serialized_end=144,
)


_BUCKET = _descriptor.Descriptor(
  name='Bucket',
  full_name='DocList.Bucket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='document', full_name='DocList.Bucket.document', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='multiCorpus', full_name='DocList.Bucket.multiCorpus', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='title', full_name='DocList.Bucket.title', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iconUrl', full_name='DocList.Bucket.iconUrl', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fullContentsUrl', full_name='DocList.Bucket.fullContentsUrl', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='relevance', full_name='DocList.Bucket.relevance', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='estimatedResults', full_name='DocList.Bucket.estimatedResults', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='analyticsCookie', full_name='DocList.Bucket.analyticsCookie', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fullContentsListUrl', full_name='DocList.Bucket.fullContentsListUrl', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nextPageUrl', full_name='DocList.Bucket.nextPageUrl', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ordered', full_name='DocList.Bucket.ordered', index=10,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=147,
  serialized_end=407,
)

_LISTRESPONSE.fields_by_name['bucket'].message_type = _BUCKET
_LISTRESPONSE.fields_by_name['doc'].message_type = document__v2__pb2._DOCV2
_BUCKET.fields_by_name['document'].message_type = document__v1__pb2._DOCV1
DESCRIPTOR.message_types_by_name['ListResponse'] = _LISTRESPONSE
DESCRIPTOR.message_types_by_name['Bucket'] = _BUCKET

ListResponse = _reflection.GeneratedProtocolMessageType('ListResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTRESPONSE,
  __module__ = 'doc_list_pb2'
  # @@protoc_insertion_point(class_scope:DocList.ListResponse)
  ))
_sym_db.RegisterMessage(ListResponse)

Bucket = _reflection.GeneratedProtocolMessageType('Bucket', (_message.Message,), dict(
  DESCRIPTOR = _BUCKET,
  __module__ = 'doc_list_pb2'
  # @@protoc_insertion_point(class_scope:DocList.Bucket)
  ))
_sym_db.RegisterMessage(Bucket)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n com.google.android.finsky.protosB\007DocList'))
# @@protoc_insertion_point(module_scope)
