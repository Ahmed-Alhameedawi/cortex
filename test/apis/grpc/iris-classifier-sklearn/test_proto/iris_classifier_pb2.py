# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: iris_classifier.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="iris_classifier.proto",
    package="iris_classifier",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x15iris_classifier.proto\x12\x0firis_classifier"^\n\x06Sample\x12\x14\n\x0csepal_length\x18\x01 \x01(\x02\x12\x13\n\x0bsepal_width\x18\x02 \x01(\x02\x12\x14\n\x0cpetal_length\x18\x03 \x01(\x02\x12\x13\n\x0bpetal_width\x18\x04 \x01(\x02""\n\x08Response\x12\x16\n\x0e\x63lassification\x18\x01 \x01(\t2J\n\tPredictor\x12=\n\x07Predict\x12\x17.iris_classifier.Sample\x1a\x19.iris_classifier.Responseb\x06proto3',
)


_SAMPLE = _descriptor.Descriptor(
    name="Sample",
    full_name="iris_classifier.Sample",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="sepal_length",
            full_name="iris_classifier.Sample.sepal_length",
            index=0,
            number=1,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="sepal_width",
            full_name="iris_classifier.Sample.sepal_width",
            index=1,
            number=2,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="petal_length",
            full_name="iris_classifier.Sample.petal_length",
            index=2,
            number=3,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="petal_width",
            full_name="iris_classifier.Sample.petal_width",
            index=3,
            number=4,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=42,
    serialized_end=136,
)


_RESPONSE = _descriptor.Descriptor(
    name="Response",
    full_name="iris_classifier.Response",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="classification",
            full_name="iris_classifier.Response.classification",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=138,
    serialized_end=172,
)

DESCRIPTOR.message_types_by_name["Sample"] = _SAMPLE
DESCRIPTOR.message_types_by_name["Response"] = _RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Sample = _reflection.GeneratedProtocolMessageType(
    "Sample",
    (_message.Message,),
    {
        "DESCRIPTOR": _SAMPLE,
        "__module__": "iris_classifier_pb2"
        # @@protoc_insertion_point(class_scope:iris_classifier.Sample)
    },
)
_sym_db.RegisterMessage(Sample)

Response = _reflection.GeneratedProtocolMessageType(
    "Response",
    (_message.Message,),
    {
        "DESCRIPTOR": _RESPONSE,
        "__module__": "iris_classifier_pb2"
        # @@protoc_insertion_point(class_scope:iris_classifier.Response)
    },
)
_sym_db.RegisterMessage(Response)


_PREDICTOR = _descriptor.ServiceDescriptor(
    name="Predictor",
    full_name="iris_classifier.Predictor",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=174,
    serialized_end=248,
    methods=[
        _descriptor.MethodDescriptor(
            name="Predict",
            full_name="iris_classifier.Predictor.Predict",
            index=0,
            containing_service=None,
            input_type=_SAMPLE,
            output_type=_RESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_PREDICTOR)

DESCRIPTOR.services_by_name["Predictor"] = _PREDICTOR

# @@protoc_insertion_point(module_scope)