# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: context_outer_class.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import device_fingerprinting_pb2 as device__fingerprinting__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='context_outer_class.proto',
  package='ContextOuterClass',
  syntax='proto2',
  serialized_pb=_b('\n\x19\x63ontext_outer_class.proto\x12\x11\x43ontextOuterClass\x1a\x1b\x64\x65vice_fingerprinting.proto\"\x98\x03\n\x13NativeClientContext\x12\x10\n\x08imsiHash\x18\x01 \x01(\t\x12\x0e\n\x06mccMnc\x18\x02 \x01(\t\x12\x11\n\tosVersion\x18\x03 \x01(\t\x12\x0e\n\x06\x64\x65vice\x18\x04 \x01(\t\x12\x15\n\rscreenWidthPx\x18\x05 \x01(\x05\x12\x16\n\x0escreenHeightPx\x18\x06 \x01(\x05\x12\x12\n\nscreenXDpi\x18\x07 \x01(\x02\x12\x12\n\nscreenYDpi\x18\x08 \x01(\x02\x12\x13\n\x0bpackageName\x18\t \x01(\t\x12\x1a\n\x12packageVersionCode\x18\n \x01(\t\x12\x1a\n\x12packageVersionName\x18\x0b \x01(\t\x12\x43\n\x08riskData\x18\x0c \x01(\x0b\x32\x31.DeviceFingerprinting.DeviceFingerprinting.Parsed\x12\x1d\n\x15integratorPackageName\x18\r \x01(\t\x12\x16\n\x0emarketClientId\x18\x0e \x01(\t\x12\x1c\n\x14\x61ndroidClientSubtype\x18\x0f \x01(\x05\x42L\n7com.google.commerce.payments.orchestration.proto.commonB\x11\x43ontextOuterClass')
  ,
  dependencies=[device__fingerprinting__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_NATIVECLIENTCONTEXT = _descriptor.Descriptor(
  name='NativeClientContext',
  full_name='ContextOuterClass.NativeClientContext',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='imsiHash', full_name='ContextOuterClass.NativeClientContext.imsiHash', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mccMnc', full_name='ContextOuterClass.NativeClientContext.mccMnc', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='osVersion', full_name='ContextOuterClass.NativeClientContext.osVersion', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device', full_name='ContextOuterClass.NativeClientContext.device', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='screenWidthPx', full_name='ContextOuterClass.NativeClientContext.screenWidthPx', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='screenHeightPx', full_name='ContextOuterClass.NativeClientContext.screenHeightPx', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='screenXDpi', full_name='ContextOuterClass.NativeClientContext.screenXDpi', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='screenYDpi', full_name='ContextOuterClass.NativeClientContext.screenYDpi', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='packageName', full_name='ContextOuterClass.NativeClientContext.packageName', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='packageVersionCode', full_name='ContextOuterClass.NativeClientContext.packageVersionCode', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='packageVersionName', full_name='ContextOuterClass.NativeClientContext.packageVersionName', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='riskData', full_name='ContextOuterClass.NativeClientContext.riskData', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='integratorPackageName', full_name='ContextOuterClass.NativeClientContext.integratorPackageName', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='marketClientId', full_name='ContextOuterClass.NativeClientContext.marketClientId', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='androidClientSubtype', full_name='ContextOuterClass.NativeClientContext.androidClientSubtype', index=14,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=78,
  serialized_end=486,
)

_NATIVECLIENTCONTEXT.fields_by_name['riskData'].message_type = device__fingerprinting__pb2._DEVICEFINGERPRINTING_PARSED
DESCRIPTOR.message_types_by_name['NativeClientContext'] = _NATIVECLIENTCONTEXT

NativeClientContext = _reflection.GeneratedProtocolMessageType('NativeClientContext', (_message.Message,), dict(
  DESCRIPTOR = _NATIVECLIENTCONTEXT,
  __module__ = 'context_outer_class_pb2'
  # @@protoc_insertion_point(class_scope:ContextOuterClass.NativeClientContext)
  ))
_sym_db.RegisterMessage(NativeClientContext)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n7com.google.commerce.payments.orchestration.proto.commonB\021ContextOuterClass'))
# @@protoc_insertion_point(module_scope)