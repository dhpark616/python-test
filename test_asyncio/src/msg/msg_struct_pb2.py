# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: msg_struct.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import msg_enum_pb2 as msg__enum__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='msg_struct.proto',
  package='msg',
  syntax='proto3',
  serialized_pb=_b('\n\x10msg_struct.proto\x12\x03msg\x1a\x0emsg_enum.proto\"B\n\tchar_info\x12\x10\n\x08\x63har_idx\x18\x01 \x01(\x03\x12\x11\n\tchar_name\x18\x02 \x01(\t\x12\x10\n\x08\x63har_mid\x18\x03 \x01(\x05\x62\x06proto3')
  ,
  dependencies=[msg__enum__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CHAR_INFO = _descriptor.Descriptor(
  name='char_info',
  full_name='msg.char_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='char_idx', full_name='msg.char_info.char_idx', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='char_name', full_name='msg.char_info.char_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='char_mid', full_name='msg.char_info.char_mid', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=41,
  serialized_end=107,
)

DESCRIPTOR.message_types_by_name['char_info'] = _CHAR_INFO

char_info = _reflection.GeneratedProtocolMessageType('char_info', (_message.Message,), dict(
  DESCRIPTOR = _CHAR_INFO,
  __module__ = 'msg_struct_pb2'
  # @@protoc_insertion_point(class_scope:msg.char_info)
  ))
_sym_db.RegisterMessage(char_info)


# @@protoc_insertion_point(module_scope)