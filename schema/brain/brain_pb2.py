# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: brain.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='brain.proto',
  package='brain',
  syntax='proto2',
  serialized_pb=_b('\n\x0b\x62rain.proto\x12\x05\x62rain\"\xe4\x01\n\x07\x43ommand\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0b\x43ommandName\x18\x02 \x02(\t\x12\x0f\n\x07Tooltip\x18\x03 \x02(\t\x12\x0e\n\x06Output\x18\x04 \x02(\x08\x12$\n\x06Inputs\x18\x05 \x03(\x0b\x32\x14.brain.Command.Input\x12,\n\x0eOptionalInputs\x18\x06 \x03(\x0b\x32\x14.brain.Command.Input\x1a\x43\n\x05Input\x12\x0c\n\x04Name\x18\x01 \x02(\t\x12\x0c\n\x04Type\x18\x02 \x02(\t\x12\x0f\n\x07Tooltip\x18\x03 \x02(\t\x12\r\n\x05Value\x18\x04 \x02(\t\"H\n\x06Target\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\nPluginName\x18\x02 \x02(\t\x12\x10\n\x08Location\x18\x03 \x02(\t\x12\x0c\n\x04Port\x18\x04 \x02(\t\"z\n\x03Job\x12\n\n\x02id\x18\x01 \x01(\t\x12 \n\tJobTarget\x18\x02 \x02(\x0b\x32\r.brain.Target\x12\x0e\n\x06Status\x18\x03 \x02(\t\x12\x11\n\tStartTime\x18\x04 \x02(\x02\x12\"\n\nJobCommand\x18\x05 \x02(\x0b\x32\x0e.brain.Command\"D\n\x06Output\x12\n\n\x02id\x18\x01 \x01(\t\x12\x1d\n\tOutputJob\x18\x02 \x02(\x0b\x32\n.brain.Job\x12\x0f\n\x07\x43ontent\x18\x03 \x02(\t\"e\n\x08JobAudit\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0b\x63hange_time\x18\x02 \x02(\x02\x12\x1b\n\x07old_val\x18\x03 \x02(\x0b\x32\n.brain.Job\x12\x1b\n\x07new_val\x18\x04 \x02(\x0b\x32\n.brain.Job\"n\n\x0bTargetAudit\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0b\x63hange_time\x18\x02 \x02(\x02\x12\x1e\n\x07old_val\x18\x03 \x02(\x0b\x32\r.brain.Target\x12\x1e\n\x07new_val\x18\x04 \x02(\x0b\x32\r.brain.Target\"e\n\x0bOutputAudit\x12\n\n\x02id\x18\x01 \x01(\t\x12\n\n\x02ts\x18\x02 \x02(\x02\x12\x1e\n\x07old_val\x18\x03 \x02(\x0b\x32\r.brain.Output\x12\x1e\n\x07new_val\x18\x04 \x02(\x0b\x32\r.brain.Output\"\x89\x01\n\x05\x41udit\x12\n\n\x02id\x18\x01 \x01(\t\x12\x1e\n\x03Job\x18\x02 \x01(\x0b\x32\x0f.brain.JobAuditH\x00\x12$\n\x06Target\x18\x03 \x01(\x0b\x32\x12.brain.TargetAuditH\x00\x12$\n\x06Output\x18\x04 \x01(\x0b\x32\x12.brain.OutputAuditH\x00\x42\x08\n\x06record\"O\n\x06\x42inary\x12\x0c\n\x04Name\x18\x02 \x02(\t\x12\x11\n\tTimestamp\x18\x03 \x02(\x02\x12\x13\n\x0b\x43ontentType\x18\x04 \x02(\t\x12\x0f\n\x07\x43ontent\x18\x05 \x02(\x0c\")\n\x07Targets\x12\x1e\n\x07Targets\x18\x01 \x03(\x0b\x32\r.brain.Target\" \n\x04Jobs\x12\x18\n\x04Jobs\x18\x01 \x03(\x0b\x32\n.brain.Job\",\n\x08\x43ommands\x12 \n\x08\x43ommands\x18\x01 \x03(\x0b\x32\x0e.brain.Command\"\xe3\x01\n\x06Plugin\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04Name\x18\x02 \x02(\t\x12\x13\n\x0bServiceName\x18\x03 \x02(\t\x12\x11\n\tServiceID\x18\x04 \x01(\t\x12\x11\n\x02OS\x18\x05 \x02(\t:\x05posix\x12\x18\n\x05State\x18\x06 \x02(\t:\tAvailable\x12\x14\n\x0c\x44\x65siredState\x18\x07 \x02(\t\x12\x11\n\tInterface\x18\x08 \x02(\t\x12\x15\n\rExternalPorts\x18\t \x03(\t\x12\x15\n\rInternalPorts\x18\n \x03(\t\x12\x13\n\x0b\x45nvironment\x18\x0b \x03(\t\"\x8c\x01\n\x04Port\x12\n\n\x02id\x18\x01 \x01(\t\x12\x1a\n\rInterfaceName\x18\x02 \x02(\t:\x03\x41ll\x12\x14\n\x0cNodeHostName\x18\x03 \x02(\t\x12\x11\n\x02OS\x18\x04 \x02(\t:\x05posix\x12\x0f\n\x07\x41\x64\x64ress\x18\x05 \x02(\t\x12\x10\n\x08TCPPorts\x18\x06 \x03(\t\x12\x10\n\x08UDPPorts\x18\x07 \x03(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_COMMAND_INPUT = _descriptor.Descriptor(
  name='Input',
  full_name='brain.Command.Input',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Name', full_name='brain.Command.Input.Name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Type', full_name='brain.Command.Input.Type', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Tooltip', full_name='brain.Command.Input.Tooltip', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Value', full_name='brain.Command.Input.Value', index=3,
      number=4, type=9, cpp_type=9, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=184,
  serialized_end=251,
)

_COMMAND = _descriptor.Descriptor(
  name='Command',
  full_name='brain.Command',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='brain.Command.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='CommandName', full_name='brain.Command.CommandName', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Tooltip', full_name='brain.Command.Tooltip', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Output', full_name='brain.Command.Output', index=3,
      number=4, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Inputs', full_name='brain.Command.Inputs', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='OptionalInputs', full_name='brain.Command.OptionalInputs', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_COMMAND_INPUT, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=23,
  serialized_end=251,
)


_TARGET = _descriptor.Descriptor(
  name='Target',
  full_name='brain.Target',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='brain.Target.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='PluginName', full_name='brain.Target.PluginName', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Location', full_name='brain.Target.Location', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Port', full_name='brain.Target.Port', index=3,
      number=4, type=9, cpp_type=9, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=253,
  serialized_end=325,
)


_JOB = _descriptor.Descriptor(
  name='Job',
  full_name='brain.Job',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='brain.Job.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='JobTarget', full_name='brain.Job.JobTarget', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Status', full_name='brain.Job.Status', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='StartTime', full_name='brain.Job.StartTime', index=3,
      number=4, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='JobCommand', full_name='brain.Job.JobCommand', index=4,
      number=5, type=11, cpp_type=10, label=2,
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
  serialized_start=327,
  serialized_end=449,
)


_OUTPUT = _descriptor.Descriptor(
  name='Output',
  full_name='brain.Output',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='brain.Output.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='OutputJob', full_name='brain.Output.OutputJob', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Content', full_name='brain.Output.Content', index=2,
      number=3, type=9, cpp_type=9, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=451,
  serialized_end=519,
)


_JOBAUDIT = _descriptor.Descriptor(
  name='JobAudit',
  full_name='brain.JobAudit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='brain.JobAudit.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='change_time', full_name='brain.JobAudit.change_time', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='old_val', full_name='brain.JobAudit.old_val', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='new_val', full_name='brain.JobAudit.new_val', index=3,
      number=4, type=11, cpp_type=10, label=2,
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
  serialized_start=521,
  serialized_end=622,
)


_TARGETAUDIT = _descriptor.Descriptor(
  name='TargetAudit',
  full_name='brain.TargetAudit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='brain.TargetAudit.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='change_time', full_name='brain.TargetAudit.change_time', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='old_val', full_name='brain.TargetAudit.old_val', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='new_val', full_name='brain.TargetAudit.new_val', index=3,
      number=4, type=11, cpp_type=10, label=2,
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
  serialized_start=624,
  serialized_end=734,
)


_OUTPUTAUDIT = _descriptor.Descriptor(
  name='OutputAudit',
  full_name='brain.OutputAudit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='brain.OutputAudit.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ts', full_name='brain.OutputAudit.ts', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='old_val', full_name='brain.OutputAudit.old_val', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='new_val', full_name='brain.OutputAudit.new_val', index=3,
      number=4, type=11, cpp_type=10, label=2,
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
  serialized_start=736,
  serialized_end=837,
)


_AUDIT = _descriptor.Descriptor(
  name='Audit',
  full_name='brain.Audit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='brain.Audit.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Job', full_name='brain.Audit.Job', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Target', full_name='brain.Audit.Target', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Output', full_name='brain.Audit.Output', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='record', full_name='brain.Audit.record',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=840,
  serialized_end=977,
)


_BINARY = _descriptor.Descriptor(
  name='Binary',
  full_name='brain.Binary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Name', full_name='brain.Binary.Name', index=0,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Timestamp', full_name='brain.Binary.Timestamp', index=1,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ContentType', full_name='brain.Binary.ContentType', index=2,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Content', full_name='brain.Binary.Content', index=3,
      number=5, type=12, cpp_type=9, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=979,
  serialized_end=1058,
)


_TARGETS = _descriptor.Descriptor(
  name='Targets',
  full_name='brain.Targets',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Targets', full_name='brain.Targets.Targets', index=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1060,
  serialized_end=1101,
)


_JOBS = _descriptor.Descriptor(
  name='Jobs',
  full_name='brain.Jobs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Jobs', full_name='brain.Jobs.Jobs', index=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1103,
  serialized_end=1135,
)


_COMMANDS = _descriptor.Descriptor(
  name='Commands',
  full_name='brain.Commands',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Commands', full_name='brain.Commands.Commands', index=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1137,
  serialized_end=1181,
)


_PLUGIN = _descriptor.Descriptor(
  name='Plugin',
  full_name='brain.Plugin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='brain.Plugin.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Name', full_name='brain.Plugin.Name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ServiceName', full_name='brain.Plugin.ServiceName', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ServiceID', full_name='brain.Plugin.ServiceID', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='OS', full_name='brain.Plugin.OS', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=True, default_value=_b("posix").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='State', full_name='brain.Plugin.State', index=5,
      number=6, type=9, cpp_type=9, label=2,
      has_default_value=True, default_value=_b("Available").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='DesiredState', full_name='brain.Plugin.DesiredState', index=6,
      number=7, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Interface', full_name='brain.Plugin.Interface', index=7,
      number=8, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ExternalPorts', full_name='brain.Plugin.ExternalPorts', index=8,
      number=9, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='InternalPorts', full_name='brain.Plugin.InternalPorts', index=9,
      number=10, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Environment', full_name='brain.Plugin.Environment', index=10,
      number=11, type=9, cpp_type=9, label=3,
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
  serialized_start=1184,
  serialized_end=1411,
)


_PORT = _descriptor.Descriptor(
  name='Port',
  full_name='brain.Port',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='brain.Port.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='InterfaceName', full_name='brain.Port.InterfaceName', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=True, default_value=_b("All").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='NodeHostName', full_name='brain.Port.NodeHostName', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='OS', full_name='brain.Port.OS', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=True, default_value=_b("posix").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Address', full_name='brain.Port.Address', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='TCPPorts', full_name='brain.Port.TCPPorts', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='UDPPorts', full_name='brain.Port.UDPPorts', index=6,
      number=7, type=9, cpp_type=9, label=3,
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
  serialized_start=1414,
  serialized_end=1554,
)

_COMMAND_INPUT.containing_type = _COMMAND
_COMMAND.fields_by_name['Inputs'].message_type = _COMMAND_INPUT
_COMMAND.fields_by_name['OptionalInputs'].message_type = _COMMAND_INPUT
_JOB.fields_by_name['JobTarget'].message_type = _TARGET
_JOB.fields_by_name['JobCommand'].message_type = _COMMAND
_OUTPUT.fields_by_name['OutputJob'].message_type = _JOB
_JOBAUDIT.fields_by_name['old_val'].message_type = _JOB
_JOBAUDIT.fields_by_name['new_val'].message_type = _JOB
_TARGETAUDIT.fields_by_name['old_val'].message_type = _TARGET
_TARGETAUDIT.fields_by_name['new_val'].message_type = _TARGET
_OUTPUTAUDIT.fields_by_name['old_val'].message_type = _OUTPUT
_OUTPUTAUDIT.fields_by_name['new_val'].message_type = _OUTPUT
_AUDIT.fields_by_name['Job'].message_type = _JOBAUDIT
_AUDIT.fields_by_name['Target'].message_type = _TARGETAUDIT
_AUDIT.fields_by_name['Output'].message_type = _OUTPUTAUDIT
_AUDIT.oneofs_by_name['record'].fields.append(
  _AUDIT.fields_by_name['Job'])
_AUDIT.fields_by_name['Job'].containing_oneof = _AUDIT.oneofs_by_name['record']
_AUDIT.oneofs_by_name['record'].fields.append(
  _AUDIT.fields_by_name['Target'])
_AUDIT.fields_by_name['Target'].containing_oneof = _AUDIT.oneofs_by_name['record']
_AUDIT.oneofs_by_name['record'].fields.append(
  _AUDIT.fields_by_name['Output'])
_AUDIT.fields_by_name['Output'].containing_oneof = _AUDIT.oneofs_by_name['record']
_TARGETS.fields_by_name['Targets'].message_type = _TARGET
_JOBS.fields_by_name['Jobs'].message_type = _JOB
_COMMANDS.fields_by_name['Commands'].message_type = _COMMAND
DESCRIPTOR.message_types_by_name['Command'] = _COMMAND
DESCRIPTOR.message_types_by_name['Target'] = _TARGET
DESCRIPTOR.message_types_by_name['Job'] = _JOB
DESCRIPTOR.message_types_by_name['Output'] = _OUTPUT
DESCRIPTOR.message_types_by_name['JobAudit'] = _JOBAUDIT
DESCRIPTOR.message_types_by_name['TargetAudit'] = _TARGETAUDIT
DESCRIPTOR.message_types_by_name['OutputAudit'] = _OUTPUTAUDIT
DESCRIPTOR.message_types_by_name['Audit'] = _AUDIT
DESCRIPTOR.message_types_by_name['Binary'] = _BINARY
DESCRIPTOR.message_types_by_name['Targets'] = _TARGETS
DESCRIPTOR.message_types_by_name['Jobs'] = _JOBS
DESCRIPTOR.message_types_by_name['Commands'] = _COMMANDS
DESCRIPTOR.message_types_by_name['Plugin'] = _PLUGIN
DESCRIPTOR.message_types_by_name['Port'] = _PORT

Command = _reflection.GeneratedProtocolMessageType('Command', (_message.Message,), dict(

  Input = _reflection.GeneratedProtocolMessageType('Input', (_message.Message,), dict(
    DESCRIPTOR = _COMMAND_INPUT,
    __module__ = 'brain_pb2'
    # @@protoc_insertion_point(class_scope:brain.Command.Input)
    ))
  ,
  DESCRIPTOR = _COMMAND,
  __module__ = 'brain_pb2'
  # @@protoc_insertion_point(class_scope:brain.Command)
  ))
_sym_db.RegisterMessage(Command)
_sym_db.RegisterMessage(Command.Input)

Target = _reflection.GeneratedProtocolMessageType('Target', (_message.Message,), dict(
  DESCRIPTOR = _TARGET,
  __module__ = 'brain_pb2'
  # @@protoc_insertion_point(class_scope:brain.Target)
  ))
_sym_db.RegisterMessage(Target)

Job = _reflection.GeneratedProtocolMessageType('Job', (_message.Message,), dict(
  DESCRIPTOR = _JOB,
  __module__ = 'brain_pb2'
  # @@protoc_insertion_point(class_scope:brain.Job)
  ))
_sym_db.RegisterMessage(Job)

Output = _reflection.GeneratedProtocolMessageType('Output', (_message.Message,), dict(
  DESCRIPTOR = _OUTPUT,
  __module__ = 'brain_pb2'
  # @@protoc_insertion_point(class_scope:brain.Output)
  ))
_sym_db.RegisterMessage(Output)

JobAudit = _reflection.GeneratedProtocolMessageType('JobAudit', (_message.Message,), dict(
  DESCRIPTOR = _JOBAUDIT,
  __module__ = 'brain_pb2'
  # @@protoc_insertion_point(class_scope:brain.JobAudit)
  ))
_sym_db.RegisterMessage(JobAudit)

TargetAudit = _reflection.GeneratedProtocolMessageType('TargetAudit', (_message.Message,), dict(
  DESCRIPTOR = _TARGETAUDIT,
  __module__ = 'brain_pb2'
  # @@protoc_insertion_point(class_scope:brain.TargetAudit)
  ))
_sym_db.RegisterMessage(TargetAudit)

OutputAudit = _reflection.GeneratedProtocolMessageType('OutputAudit', (_message.Message,), dict(
  DESCRIPTOR = _OUTPUTAUDIT,
  __module__ = 'brain_pb2'
  # @@protoc_insertion_point(class_scope:brain.OutputAudit)
  ))
_sym_db.RegisterMessage(OutputAudit)

Audit = _reflection.GeneratedProtocolMessageType('Audit', (_message.Message,), dict(
  DESCRIPTOR = _AUDIT,
  __module__ = 'brain_pb2'
  # @@protoc_insertion_point(class_scope:brain.Audit)
  ))
_sym_db.RegisterMessage(Audit)

Binary = _reflection.GeneratedProtocolMessageType('Binary', (_message.Message,), dict(
  DESCRIPTOR = _BINARY,
  __module__ = 'brain_pb2'
  # @@protoc_insertion_point(class_scope:brain.Binary)
  ))
_sym_db.RegisterMessage(Binary)

Targets = _reflection.GeneratedProtocolMessageType('Targets', (_message.Message,), dict(
  DESCRIPTOR = _TARGETS,
  __module__ = 'brain_pb2'
  # @@protoc_insertion_point(class_scope:brain.Targets)
  ))
_sym_db.RegisterMessage(Targets)

Jobs = _reflection.GeneratedProtocolMessageType('Jobs', (_message.Message,), dict(
  DESCRIPTOR = _JOBS,
  __module__ = 'brain_pb2'
  # @@protoc_insertion_point(class_scope:brain.Jobs)
  ))
_sym_db.RegisterMessage(Jobs)

Commands = _reflection.GeneratedProtocolMessageType('Commands', (_message.Message,), dict(
  DESCRIPTOR = _COMMANDS,
  __module__ = 'brain_pb2'
  # @@protoc_insertion_point(class_scope:brain.Commands)
  ))
_sym_db.RegisterMessage(Commands)

Plugin = _reflection.GeneratedProtocolMessageType('Plugin', (_message.Message,), dict(
  DESCRIPTOR = _PLUGIN,
  __module__ = 'brain_pb2'
  # @@protoc_insertion_point(class_scope:brain.Plugin)
  ))
_sym_db.RegisterMessage(Plugin)

Port = _reflection.GeneratedProtocolMessageType('Port', (_message.Message,), dict(
  DESCRIPTOR = _PORT,
  __module__ = 'brain_pb2'
  # @@protoc_insertion_point(class_scope:brain.Port)
  ))
_sym_db.RegisterMessage(Port)


# @@protoc_insertion_point(module_scope)
