# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: msg_packet_api.proto

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
from . import msg_error_pb2 as msg__error__pb2
from . import msg_struct_pb2 as msg__struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='msg_packet_api.proto',
  package='msg',
  syntax='proto3',
  serialized_pb=_b('\n\x14msg_packet_api.proto\x12\x03msg\x1a\x0emsg_enum.proto\x1a\x0fmsg_error.proto\x1a\x10msg_struct.proto\">\n\nreq_packet\x12\x12\n\nauth_token\x18\x01 \x01(\t\x12\x0f\n\x07\x63har_id\x18\x02 \x01(\x03\x12\x0b\n\x03msg\x18\x03 \x01(\x0c\":\n\nack_packet\x12\x1f\n\x08\x65rr_code\x18\x01 \x01(\x0e\x32\r.msg.err_type\x12\x0b\n\x03msg\x18\x02 \x01(\x0c\"U\n\tlogin_req\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12%\n\tplat_type\x18\x03 \x01(\x0e\x32\x12.msg.platform_type\"\x1f\n\tlogin_ack\x12\x12\n\nauth_token\x18\x01 \x01(\t\"\x13\n\x11get_char_list_req\"6\n\x11get_char_list_ack\x12!\n\tchar_list\x18\x01 \x03(\x0b\x32\x0e.msg.char_info\"6\n\x0f\x63reate_char_req\x12\x11\n\tchar_name\x18\x01 \x01(\t\x12\x10\n\x08\x63har_mid\x18\x02 \x01(\x05\"C\n\x0f\x63reate_char_ack\x12\x1c\n\x04\x63har\x18\x01 \x01(\x0b\x32\x0e.msg.char_info\x12\x12\n\nauth_token\x18\x02 \x01(\t\"#\n\x0f\x64\x65lete_char_req\x12\x10\n\x08\x63har_idx\x18\x01 \x01(\x03\"%\n\x0f\x64\x65lete_char_ack\x12\x12\n\nauth_token\x18\x01 \x01(\t\"#\n\x0fselect_char_req\x12\x10\n\x08\x63har_idx\x18\x01 \x01(\x03\"\x11\n\x0fselect_char_ackb\x06proto3')
  ,
  dependencies=[msg__enum__pb2.DESCRIPTOR,msg__error__pb2.DESCRIPTOR,msg__struct__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_REQ_PACKET = _descriptor.Descriptor(
  name='req_packet',
  full_name='msg.req_packet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='auth_token', full_name='msg.req_packet.auth_token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='char_id', full_name='msg.req_packet.char_id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='msg', full_name='msg.req_packet.msg', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=80,
  serialized_end=142,
)


_ACK_PACKET = _descriptor.Descriptor(
  name='ack_packet',
  full_name='msg.ack_packet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='err_code', full_name='msg.ack_packet.err_code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='msg', full_name='msg.ack_packet.msg', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=144,
  serialized_end=202,
)


_LOGIN_REQ = _descriptor.Descriptor(
  name='login_req',
  full_name='msg.login_req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='msg.login_req.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='password', full_name='msg.login_req.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='plat_type', full_name='msg.login_req.plat_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
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
  serialized_start=204,
  serialized_end=289,
)


_LOGIN_ACK = _descriptor.Descriptor(
  name='login_ack',
  full_name='msg.login_ack',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='auth_token', full_name='msg.login_ack.auth_token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=291,
  serialized_end=322,
)


_GET_CHAR_LIST_REQ = _descriptor.Descriptor(
  name='get_char_list_req',
  full_name='msg.get_char_list_req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=324,
  serialized_end=343,
)


_GET_CHAR_LIST_ACK = _descriptor.Descriptor(
  name='get_char_list_ack',
  full_name='msg.get_char_list_ack',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='char_list', full_name='msg.get_char_list_ack.char_list', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=345,
  serialized_end=399,
)


_CREATE_CHAR_REQ = _descriptor.Descriptor(
  name='create_char_req',
  full_name='msg.create_char_req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='char_name', full_name='msg.create_char_req.char_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='char_mid', full_name='msg.create_char_req.char_mid', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=401,
  serialized_end=455,
)


_CREATE_CHAR_ACK = _descriptor.Descriptor(
  name='create_char_ack',
  full_name='msg.create_char_ack',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='char', full_name='msg.create_char_ack.char', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='auth_token', full_name='msg.create_char_ack.auth_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=457,
  serialized_end=524,
)


_DELETE_CHAR_REQ = _descriptor.Descriptor(
  name='delete_char_req',
  full_name='msg.delete_char_req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='char_idx', full_name='msg.delete_char_req.char_idx', index=0,
      number=1, type=3, cpp_type=2, label=1,
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
  serialized_start=526,
  serialized_end=561,
)


_DELETE_CHAR_ACK = _descriptor.Descriptor(
  name='delete_char_ack',
  full_name='msg.delete_char_ack',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='auth_token', full_name='msg.delete_char_ack.auth_token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=563,
  serialized_end=600,
)


_SELECT_CHAR_REQ = _descriptor.Descriptor(
  name='select_char_req',
  full_name='msg.select_char_req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='char_idx', full_name='msg.select_char_req.char_idx', index=0,
      number=1, type=3, cpp_type=2, label=1,
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
  serialized_start=602,
  serialized_end=637,
)


_SELECT_CHAR_ACK = _descriptor.Descriptor(
  name='select_char_ack',
  full_name='msg.select_char_ack',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=639,
  serialized_end=656,
)

_ACK_PACKET.fields_by_name['err_code'].enum_type = msg__error__pb2._ERR_TYPE
_LOGIN_REQ.fields_by_name['plat_type'].enum_type = msg__enum__pb2._PLATFORM_TYPE
_GET_CHAR_LIST_ACK.fields_by_name['char_list'].message_type = msg__struct__pb2._CHAR_INFO
_CREATE_CHAR_ACK.fields_by_name['char'].message_type = msg__struct__pb2._CHAR_INFO
DESCRIPTOR.message_types_by_name['req_packet'] = _REQ_PACKET
DESCRIPTOR.message_types_by_name['ack_packet'] = _ACK_PACKET
DESCRIPTOR.message_types_by_name['login_req'] = _LOGIN_REQ
DESCRIPTOR.message_types_by_name['login_ack'] = _LOGIN_ACK
DESCRIPTOR.message_types_by_name['get_char_list_req'] = _GET_CHAR_LIST_REQ
DESCRIPTOR.message_types_by_name['get_char_list_ack'] = _GET_CHAR_LIST_ACK
DESCRIPTOR.message_types_by_name['create_char_req'] = _CREATE_CHAR_REQ
DESCRIPTOR.message_types_by_name['create_char_ack'] = _CREATE_CHAR_ACK
DESCRIPTOR.message_types_by_name['delete_char_req'] = _DELETE_CHAR_REQ
DESCRIPTOR.message_types_by_name['delete_char_ack'] = _DELETE_CHAR_ACK
DESCRIPTOR.message_types_by_name['select_char_req'] = _SELECT_CHAR_REQ
DESCRIPTOR.message_types_by_name['select_char_ack'] = _SELECT_CHAR_ACK

req_packet = _reflection.GeneratedProtocolMessageType('req_packet', (_message.Message,), dict(
  DESCRIPTOR = _REQ_PACKET,
  __module__ = 'msg_packet_api_pb2'
  # @@protoc_insertion_point(class_scope:msg.req_packet)
  ))
_sym_db.RegisterMessage(req_packet)

ack_packet = _reflection.GeneratedProtocolMessageType('ack_packet', (_message.Message,), dict(
  DESCRIPTOR = _ACK_PACKET,
  __module__ = 'msg_packet_api_pb2'
  # @@protoc_insertion_point(class_scope:msg.ack_packet)
  ))
_sym_db.RegisterMessage(ack_packet)

login_req = _reflection.GeneratedProtocolMessageType('login_req', (_message.Message,), dict(
  DESCRIPTOR = _LOGIN_REQ,
  __module__ = 'msg_packet_api_pb2'
  # @@protoc_insertion_point(class_scope:msg.login_req)
  ))
_sym_db.RegisterMessage(login_req)

login_ack = _reflection.GeneratedProtocolMessageType('login_ack', (_message.Message,), dict(
  DESCRIPTOR = _LOGIN_ACK,
  __module__ = 'msg_packet_api_pb2'
  # @@protoc_insertion_point(class_scope:msg.login_ack)
  ))
_sym_db.RegisterMessage(login_ack)

get_char_list_req = _reflection.GeneratedProtocolMessageType('get_char_list_req', (_message.Message,), dict(
  DESCRIPTOR = _GET_CHAR_LIST_REQ,
  __module__ = 'msg_packet_api_pb2'
  # @@protoc_insertion_point(class_scope:msg.get_char_list_req)
  ))
_sym_db.RegisterMessage(get_char_list_req)

get_char_list_ack = _reflection.GeneratedProtocolMessageType('get_char_list_ack', (_message.Message,), dict(
  DESCRIPTOR = _GET_CHAR_LIST_ACK,
  __module__ = 'msg_packet_api_pb2'
  # @@protoc_insertion_point(class_scope:msg.get_char_list_ack)
  ))
_sym_db.RegisterMessage(get_char_list_ack)

create_char_req = _reflection.GeneratedProtocolMessageType('create_char_req', (_message.Message,), dict(
  DESCRIPTOR = _CREATE_CHAR_REQ,
  __module__ = 'msg_packet_api_pb2'
  # @@protoc_insertion_point(class_scope:msg.create_char_req)
  ))
_sym_db.RegisterMessage(create_char_req)

create_char_ack = _reflection.GeneratedProtocolMessageType('create_char_ack', (_message.Message,), dict(
  DESCRIPTOR = _CREATE_CHAR_ACK,
  __module__ = 'msg_packet_api_pb2'
  # @@protoc_insertion_point(class_scope:msg.create_char_ack)
  ))
_sym_db.RegisterMessage(create_char_ack)

delete_char_req = _reflection.GeneratedProtocolMessageType('delete_char_req', (_message.Message,), dict(
  DESCRIPTOR = _DELETE_CHAR_REQ,
  __module__ = 'msg_packet_api_pb2'
  # @@protoc_insertion_point(class_scope:msg.delete_char_req)
  ))
_sym_db.RegisterMessage(delete_char_req)

delete_char_ack = _reflection.GeneratedProtocolMessageType('delete_char_ack', (_message.Message,), dict(
  DESCRIPTOR = _DELETE_CHAR_ACK,
  __module__ = 'msg_packet_api_pb2'
  # @@protoc_insertion_point(class_scope:msg.delete_char_ack)
  ))
_sym_db.RegisterMessage(delete_char_ack)

select_char_req = _reflection.GeneratedProtocolMessageType('select_char_req', (_message.Message,), dict(
  DESCRIPTOR = _SELECT_CHAR_REQ,
  __module__ = 'msg_packet_api_pb2'
  # @@protoc_insertion_point(class_scope:msg.select_char_req)
  ))
_sym_db.RegisterMessage(select_char_req)

select_char_ack = _reflection.GeneratedProtocolMessageType('select_char_ack', (_message.Message,), dict(
  DESCRIPTOR = _SELECT_CHAR_ACK,
  __module__ = 'msg_packet_api_pb2'
  # @@protoc_insertion_point(class_scope:msg.select_char_ack)
  ))
_sym_db.RegisterMessage(select_char_ack)


# @@protoc_insertion_point(module_scope)