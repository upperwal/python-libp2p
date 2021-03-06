# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: p2pd.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='p2pd.proto',
  package='p2pd.pb',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\np2pd.proto\x12\x07p2pd.pb\"\xc1\x02\n\x07Request\x12#\n\x04type\x18\x01 \x02(\x0e\x32\x15.p2pd.pb.Request.Type\x12(\n\x07\x63onnect\x18\x02 \x01(\x0b\x32\x17.p2pd.pb.ConnectRequest\x12.\n\nstreamOpen\x18\x03 \x01(\x0b\x32\x1a.p2pd.pb.StreamOpenRequest\x12\x34\n\rstreamHandler\x18\x04 \x01(\x0b\x32\x1d.p2pd.pb.StreamHandlerRequest\x12 \n\x03\x64ht\x18\x05 \x01(\x0b\x32\x13.p2pd.pb.DHTRequest\"_\n\x04Type\x12\x0c\n\x08IDENTIFY\x10\x00\x12\x0b\n\x07\x43ONNECT\x10\x01\x12\x0f\n\x0bSTREAM_OPEN\x10\x02\x12\x12\n\x0eSTREAM_HANDLER\x10\x03\x12\x07\n\x03\x44HT\x10\x04\x12\x0e\n\nLIST_PEERS\x10\x05\"\x8d\x02\n\x08Response\x12$\n\x04type\x18\x01 \x02(\x0e\x32\x16.p2pd.pb.Response.Type\x12%\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x16.p2pd.pb.ErrorResponse\x12\'\n\nstreamInfo\x18\x03 \x01(\x0b\x32\x13.p2pd.pb.StreamInfo\x12+\n\x08identify\x18\x04 \x01(\x0b\x32\x19.p2pd.pb.IdentifyResponse\x12!\n\x03\x64ht\x18\x05 \x01(\x0b\x32\x14.p2pd.pb.DHTResponse\x12 \n\x05peers\x18\x06 \x03(\x0b\x32\x11.p2pd.pb.PeerInfo\"\x19\n\x04Type\x12\x06\n\x02OK\x10\x00\x12\t\n\x05\x45RROR\x10\x01\"-\n\x10IdentifyResponse\x12\n\n\x02id\x18\x01 \x02(\x0c\x12\r\n\x05\x61\x64\x64rs\x18\x02 \x03(\x0c\"-\n\x0e\x43onnectRequest\x12\x0c\n\x04peer\x18\x01 \x02(\x0c\x12\r\n\x05\x61\x64\x64rs\x18\x02 \x03(\x0c\"0\n\x11StreamOpenRequest\x12\x0c\n\x04peer\x18\x01 \x02(\x0c\x12\r\n\x05proto\x18\x02 \x03(\t\"3\n\x14StreamHandlerRequest\x12\x0c\n\x04path\x18\x01 \x02(\t\x12\r\n\x05proto\x18\x02 \x03(\t\"\x1c\n\rErrorResponse\x12\x0b\n\x03msg\x18\x01 \x02(\t\"7\n\nStreamInfo\x12\x0c\n\x04peer\x18\x01 \x02(\x0c\x12\x0c\n\x04\x61\x64\x64r\x18\x02 \x02(\x0c\x12\r\n\x05proto\x18\x03 \x02(\t\"\xc1\x02\n\nDHTRequest\x12&\n\x04type\x18\x01 \x02(\x0e\x32\x18.p2pd.pb.DHTRequest.Type\x12\x0c\n\x04peer\x18\x02 \x01(\x0c\x12\x0b\n\x03\x63id\x18\x03 \x01(\x0c\x12\x0b\n\x03key\x18\x04 \x01(\t\x12\r\n\x05value\x18\x05 \x01(\x0c\x12\r\n\x05\x63ount\x18\x06 \x01(\x05\x12\x0f\n\x07timeout\x18\x07 \x01(\x03\"\xb3\x01\n\x04Type\x12\r\n\tFIND_PEER\x10\x00\x12 \n\x1c\x46IND_PEERS_CONNECTED_TO_PEER\x10\x01\x12\x12\n\x0e\x46IND_PROVIDERS\x10\x02\x12\x15\n\x11GET_CLOSEST_PEERS\x10\x03\x12\x12\n\x0eGET_PUBLIC_KEY\x10\x04\x12\r\n\tGET_VALUE\x10\x05\x12\x10\n\x0cSEARCH_VALUE\x10\x06\x12\r\n\tPUT_VALUE\x10\x07\x12\x0b\n\x07PROVIDE\x10\x08\"\x8d\x01\n\x0b\x44HTResponse\x12\'\n\x04type\x18\x01 \x02(\x0e\x32\x19.p2pd.pb.DHTResponse.Type\x12\x1f\n\x04peer\x18\x02 \x01(\x0b\x32\x11.p2pd.pb.PeerInfo\x12\r\n\x05value\x18\x03 \x01(\x0c\"%\n\x04Type\x12\t\n\x05\x42\x45GIN\x10\x00\x12\t\n\x05VALUE\x10\x01\x12\x07\n\x03\x45ND\x10\x02\"%\n\x08PeerInfo\x12\n\n\x02id\x18\x01 \x02(\x0c\x12\r\n\x05\x61\x64\x64rs\x18\x02 \x03(\x0c')
)



_REQUEST_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='p2pd.pb.Request.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='IDENTIFY', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONNECT', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STREAM_OPEN', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STREAM_HANDLER', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DHT', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LIST_PEERS', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=250,
  serialized_end=345,
)
_sym_db.RegisterEnumDescriptor(_REQUEST_TYPE)

_RESPONSE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='p2pd.pb.Response.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=592,
  serialized_end=617,
)
_sym_db.RegisterEnumDescriptor(_RESPONSE_TYPE)

_DHTREQUEST_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='p2pd.pb.DHTRequest.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FIND_PEER', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FIND_PEERS_CONNECTED_TO_PEER', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FIND_PROVIDERS', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_CLOSEST_PEERS', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_PUBLIC_KEY', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_VALUE', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEARCH_VALUE', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PUT_VALUE', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROVIDE', index=8, number=8,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1046,
  serialized_end=1225,
)
_sym_db.RegisterEnumDescriptor(_DHTREQUEST_TYPE)

_DHTRESPONSE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='p2pd.pb.DHTResponse.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BEGIN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VALUE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='END', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1332,
  serialized_end=1369,
)
_sym_db.RegisterEnumDescriptor(_DHTRESPONSE_TYPE)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='p2pd.pb.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='p2pd.pb.Request.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connect', full_name='p2pd.pb.Request.connect', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='streamOpen', full_name='p2pd.pb.Request.streamOpen', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='streamHandler', full_name='p2pd.pb.Request.streamHandler', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dht', full_name='p2pd.pb.Request.dht', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REQUEST_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=24,
  serialized_end=345,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='p2pd.pb.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='p2pd.pb.Response.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='p2pd.pb.Response.error', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='streamInfo', full_name='p2pd.pb.Response.streamInfo', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='identify', full_name='p2pd.pb.Response.identify', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dht', full_name='p2pd.pb.Response.dht', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='peers', full_name='p2pd.pb.Response.peers', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RESPONSE_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=348,
  serialized_end=617,
)


_IDENTIFYRESPONSE = _descriptor.Descriptor(
  name='IdentifyResponse',
  full_name='p2pd.pb.IdentifyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='p2pd.pb.IdentifyResponse.id', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='addrs', full_name='p2pd.pb.IdentifyResponse.addrs', index=1,
      number=2, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=619,
  serialized_end=664,
)


_CONNECTREQUEST = _descriptor.Descriptor(
  name='ConnectRequest',
  full_name='p2pd.pb.ConnectRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='peer', full_name='p2pd.pb.ConnectRequest.peer', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='addrs', full_name='p2pd.pb.ConnectRequest.addrs', index=1,
      number=2, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=666,
  serialized_end=711,
)


_STREAMOPENREQUEST = _descriptor.Descriptor(
  name='StreamOpenRequest',
  full_name='p2pd.pb.StreamOpenRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='peer', full_name='p2pd.pb.StreamOpenRequest.peer', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proto', full_name='p2pd.pb.StreamOpenRequest.proto', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=713,
  serialized_end=761,
)


_STREAMHANDLERREQUEST = _descriptor.Descriptor(
  name='StreamHandlerRequest',
  full_name='p2pd.pb.StreamHandlerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='p2pd.pb.StreamHandlerRequest.path', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proto', full_name='p2pd.pb.StreamHandlerRequest.proto', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=763,
  serialized_end=814,
)


_ERRORRESPONSE = _descriptor.Descriptor(
  name='ErrorResponse',
  full_name='p2pd.pb.ErrorResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg', full_name='p2pd.pb.ErrorResponse.msg', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=816,
  serialized_end=844,
)


_STREAMINFO = _descriptor.Descriptor(
  name='StreamInfo',
  full_name='p2pd.pb.StreamInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='peer', full_name='p2pd.pb.StreamInfo.peer', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='addr', full_name='p2pd.pb.StreamInfo.addr', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proto', full_name='p2pd.pb.StreamInfo.proto', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=846,
  serialized_end=901,
)


_DHTREQUEST = _descriptor.Descriptor(
  name='DHTRequest',
  full_name='p2pd.pb.DHTRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='p2pd.pb.DHTRequest.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='peer', full_name='p2pd.pb.DHTRequest.peer', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cid', full_name='p2pd.pb.DHTRequest.cid', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='p2pd.pb.DHTRequest.key', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='p2pd.pb.DHTRequest.value', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='count', full_name='p2pd.pb.DHTRequest.count', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='p2pd.pb.DHTRequest.timeout', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DHTREQUEST_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=904,
  serialized_end=1225,
)


_DHTRESPONSE = _descriptor.Descriptor(
  name='DHTResponse',
  full_name='p2pd.pb.DHTResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='p2pd.pb.DHTResponse.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='peer', full_name='p2pd.pb.DHTResponse.peer', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='p2pd.pb.DHTResponse.value', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DHTRESPONSE_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1228,
  serialized_end=1369,
)


_PEERINFO = _descriptor.Descriptor(
  name='PeerInfo',
  full_name='p2pd.pb.PeerInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='p2pd.pb.PeerInfo.id', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='addrs', full_name='p2pd.pb.PeerInfo.addrs', index=1,
      number=2, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1371,
  serialized_end=1408,
)

_REQUEST.fields_by_name['type'].enum_type = _REQUEST_TYPE
_REQUEST.fields_by_name['connect'].message_type = _CONNECTREQUEST
_REQUEST.fields_by_name['streamOpen'].message_type = _STREAMOPENREQUEST
_REQUEST.fields_by_name['streamHandler'].message_type = _STREAMHANDLERREQUEST
_REQUEST.fields_by_name['dht'].message_type = _DHTREQUEST
_REQUEST_TYPE.containing_type = _REQUEST
_RESPONSE.fields_by_name['type'].enum_type = _RESPONSE_TYPE
_RESPONSE.fields_by_name['error'].message_type = _ERRORRESPONSE
_RESPONSE.fields_by_name['streamInfo'].message_type = _STREAMINFO
_RESPONSE.fields_by_name['identify'].message_type = _IDENTIFYRESPONSE
_RESPONSE.fields_by_name['dht'].message_type = _DHTRESPONSE
_RESPONSE.fields_by_name['peers'].message_type = _PEERINFO
_RESPONSE_TYPE.containing_type = _RESPONSE
_DHTREQUEST.fields_by_name['type'].enum_type = _DHTREQUEST_TYPE
_DHTREQUEST_TYPE.containing_type = _DHTREQUEST
_DHTRESPONSE.fields_by_name['type'].enum_type = _DHTRESPONSE_TYPE
_DHTRESPONSE.fields_by_name['peer'].message_type = _PEERINFO
_DHTRESPONSE_TYPE.containing_type = _DHTRESPONSE
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.message_types_by_name['IdentifyResponse'] = _IDENTIFYRESPONSE
DESCRIPTOR.message_types_by_name['ConnectRequest'] = _CONNECTREQUEST
DESCRIPTOR.message_types_by_name['StreamOpenRequest'] = _STREAMOPENREQUEST
DESCRIPTOR.message_types_by_name['StreamHandlerRequest'] = _STREAMHANDLERREQUEST
DESCRIPTOR.message_types_by_name['ErrorResponse'] = _ERRORRESPONSE
DESCRIPTOR.message_types_by_name['StreamInfo'] = _STREAMINFO
DESCRIPTOR.message_types_by_name['DHTRequest'] = _DHTREQUEST
DESCRIPTOR.message_types_by_name['DHTResponse'] = _DHTRESPONSE
DESCRIPTOR.message_types_by_name['PeerInfo'] = _PEERINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'p2pd_pb2'
  # @@protoc_insertion_point(class_scope:p2pd.pb.Request)
  ))
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'p2pd_pb2'
  # @@protoc_insertion_point(class_scope:p2pd.pb.Response)
  ))
_sym_db.RegisterMessage(Response)

IdentifyResponse = _reflection.GeneratedProtocolMessageType('IdentifyResponse', (_message.Message,), dict(
  DESCRIPTOR = _IDENTIFYRESPONSE,
  __module__ = 'p2pd_pb2'
  # @@protoc_insertion_point(class_scope:p2pd.pb.IdentifyResponse)
  ))
_sym_db.RegisterMessage(IdentifyResponse)

ConnectRequest = _reflection.GeneratedProtocolMessageType('ConnectRequest', (_message.Message,), dict(
  DESCRIPTOR = _CONNECTREQUEST,
  __module__ = 'p2pd_pb2'
  # @@protoc_insertion_point(class_scope:p2pd.pb.ConnectRequest)
  ))
_sym_db.RegisterMessage(ConnectRequest)

StreamOpenRequest = _reflection.GeneratedProtocolMessageType('StreamOpenRequest', (_message.Message,), dict(
  DESCRIPTOR = _STREAMOPENREQUEST,
  __module__ = 'p2pd_pb2'
  # @@protoc_insertion_point(class_scope:p2pd.pb.StreamOpenRequest)
  ))
_sym_db.RegisterMessage(StreamOpenRequest)

StreamHandlerRequest = _reflection.GeneratedProtocolMessageType('StreamHandlerRequest', (_message.Message,), dict(
  DESCRIPTOR = _STREAMHANDLERREQUEST,
  __module__ = 'p2pd_pb2'
  # @@protoc_insertion_point(class_scope:p2pd.pb.StreamHandlerRequest)
  ))
_sym_db.RegisterMessage(StreamHandlerRequest)

ErrorResponse = _reflection.GeneratedProtocolMessageType('ErrorResponse', (_message.Message,), dict(
  DESCRIPTOR = _ERRORRESPONSE,
  __module__ = 'p2pd_pb2'
  # @@protoc_insertion_point(class_scope:p2pd.pb.ErrorResponse)
  ))
_sym_db.RegisterMessage(ErrorResponse)

StreamInfo = _reflection.GeneratedProtocolMessageType('StreamInfo', (_message.Message,), dict(
  DESCRIPTOR = _STREAMINFO,
  __module__ = 'p2pd_pb2'
  # @@protoc_insertion_point(class_scope:p2pd.pb.StreamInfo)
  ))
_sym_db.RegisterMessage(StreamInfo)

DHTRequest = _reflection.GeneratedProtocolMessageType('DHTRequest', (_message.Message,), dict(
  DESCRIPTOR = _DHTREQUEST,
  __module__ = 'p2pd_pb2'
  # @@protoc_insertion_point(class_scope:p2pd.pb.DHTRequest)
  ))
_sym_db.RegisterMessage(DHTRequest)

DHTResponse = _reflection.GeneratedProtocolMessageType('DHTResponse', (_message.Message,), dict(
  DESCRIPTOR = _DHTRESPONSE,
  __module__ = 'p2pd_pb2'
  # @@protoc_insertion_point(class_scope:p2pd.pb.DHTResponse)
  ))
_sym_db.RegisterMessage(DHTResponse)

PeerInfo = _reflection.GeneratedProtocolMessageType('PeerInfo', (_message.Message,), dict(
  DESCRIPTOR = _PEERINFO,
  __module__ = 'p2pd_pb2'
  # @@protoc_insertion_point(class_scope:p2pd.pb.PeerInfo)
  ))
_sym_db.RegisterMessage(PeerInfo)


# @@protoc_insertion_point(module_scope)
