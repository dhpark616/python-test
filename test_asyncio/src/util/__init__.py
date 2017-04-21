import asyncio

import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
from google.protobuf.descriptor import FieldDescriptor


def make_run_forever(func, period):
    async def task():
        while True:
            await asyncio.sleep(period)
            func()

    asyncio.ensure_future(task())


def repeated_add_dict(self, dict_data):
    obj = self.add()
    for k, v in dict_data.items():
        if not hasattr(obj, k):
            continue
        if isinstance(v, list) or isinstance(v, dict):
            child = getattr(obj, k)
            child.set_dict(v)
        else:
            setattr(obj, k, v)


def repeated_set_dict(self, list_data):
    for i in list_data:
        self.add_dict(i)


google.protobuf.internal.containers.RepeatedCompositeFieldContainer.add_dict = repeated_add_dict
google.protobuf.internal.containers.RepeatedCompositeFieldContainer.set_dict = repeated_set_dict
google.protobuf.internal.containers.RepeatedScalarFieldContainer.set_dict = lambda self, val: self.extend(val)


def message_set_dict(self, dict_data):
    for k, v in dict_data.items():
        if not hasattr(self, k):
            continue
        if isinstance(v, list) or isinstance(v, dict):
            child = getattr(self, k)
            child.set_dict(v)
        else:
            setattr(self, k, v)


google.protobuf.message.Message.set_dict = message_set_dict


def message_set_default(self):
    for field in self.DESCRIPTOR.fields_by_name.keys():
        obj = getattr(self, field)
        if isinstance(obj, google.protobuf.message.Message):
            obj.set_default()
        elif isinstance(obj, google.protobuf.internal.containers.RepeatedCompositeFieldContainer):
            pass
        elif isinstance(obj, google.protobuf.internal.containers.RepeatedScalarFieldContainer):
            pass
        else:
            setattr(self, field, self.DESCRIPTOR.fields_by_name[field].default_value)


google.protobuf.message.Message.set_default = message_set_default


def get_enum_name(self, num):
    desc = self.DESCRIPTOR
    obj = desc.values_by_number.get(num)
    if obj is None:
        return None
    else:
        return obj.name


google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper.get_enum_name = get_enum_name


def get_enum_number(self, name):
    desc = self.DESCRIPTOR
    obj = desc.values_by_name.get(name)
    if obj is None:
        return None
    else:
        return obj.number


google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper.get_enum_number = get_enum_number

_TYPE_CALLABLE_MAP = {
    FieldDescriptor.TYPE_DOUBLE: float,
    FieldDescriptor.TYPE_FLOAT: float,
    FieldDescriptor.TYPE_INT32: int,
    FieldDescriptor.TYPE_INT64: int,
    FieldDescriptor.TYPE_UINT32: int,
    FieldDescriptor.TYPE_UINT64: int,
    FieldDescriptor.TYPE_SINT32: int,
    FieldDescriptor.TYPE_SINT64: int,
    FieldDescriptor.TYPE_FIXED32: int,
    FieldDescriptor.TYPE_FIXED64: int,
    FieldDescriptor.TYPE_SFIXED32: int,
    FieldDescriptor.TYPE_SFIXED64: int,
    FieldDescriptor.TYPE_BOOL: bool,
    FieldDescriptor.TYPE_STRING: str,
    FieldDescriptor.TYPE_BYTES: lambda b: b.encode("base64"),
    FieldDescriptor.TYPE_ENUM: int,
}


def _get_field_value_adaptor(pb, field, type_callable_map=_TYPE_CALLABLE_MAP, use_enum_labels=False):
    if field.type == FieldDescriptor.TYPE_MESSAGE:
        return lambda pb: protobuf_to_dict(pb, type_callable_map=type_callable_map, use_enum_labels=use_enum_labels)

    if use_enum_labels and field.type == FieldDescriptor.TYPE_ENUM:
        return lambda val: field.enum_type.values_by_number[int(val)].name

    if field.type in type_callable_map:
        return type_callable_map[field.type]

    raise TypeError('Field {}.{} has unrecognised type id {}'.format(pb.__class__.__name__, field.name, field.type))


def repeated(type_callable):
    return lambda val_list: [type_callable(val) for val in val_list]


def protobuf_to_dict(pb, type_callable_map=_TYPE_CALLABLE_MAP, use_enum_labels=False):
    if not hasattr(pb, 'ListFields'):
        if hasattr(pb, 'obj') and isinstance(getattr(pb, 'obj'), tuple):
            return getattr(pb, 'obj')._asdict()
        return pb

    result_dict = {}
    extensions = {}
    for field, val in pb.ListFields():
        type_callable = _get_field_value_adaptor(pb, field, type_callable_map, use_enum_labels)
        if field.label == FieldDescriptor.LABEL_REPEATED:
            type_callable = repeated(type_callable)

        if field.is_extension:
            extensions[str(field.number)] = type_callable(val)
            continue

        result_dict[field.name] = type_callable(val)

    if extensions:
        result_dict['___X'] = extensions
    return result_dict
