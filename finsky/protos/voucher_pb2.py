# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: voucher.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_pb2 as common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='voucher.proto',
  package='Voucher',
  syntax='proto2',
  serialized_pb=_b('\n\rvoucher.proto\x12\x07Voucher\x1a\x0c\x63ommon.proto\"6\n\x0eLibraryVoucher\x12$\n\tvoucherId\x18\x01 \x01(\x0b\x32\x11.Common.VoucherIdB+\n com.google.android.finsky.protosB\x07Voucher')
  ,
  dependencies=[common__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_LIBRARYVOUCHER = _descriptor.Descriptor(
  name='LibraryVoucher',
  full_name='Voucher.LibraryVoucher',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='voucherId', full_name='Voucher.LibraryVoucher.voucherId', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=40,
  serialized_end=94,
)

_LIBRARYVOUCHER.fields_by_name['voucherId'].message_type = common__pb2._VOUCHERID
DESCRIPTOR.message_types_by_name['LibraryVoucher'] = _LIBRARYVOUCHER

LibraryVoucher = _reflection.GeneratedProtocolMessageType('LibraryVoucher', (_message.Message,), dict(
  DESCRIPTOR = _LIBRARYVOUCHER,
  __module__ = 'voucher_pb2'
  # @@protoc_insertion_point(class_scope:Voucher.LibraryVoucher)
  ))
_sym_db.RegisterMessage(LibraryVoucher)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n com.google.android.finsky.protosB\007Voucher'))
# @@protoc_insertion_point(module_scope)