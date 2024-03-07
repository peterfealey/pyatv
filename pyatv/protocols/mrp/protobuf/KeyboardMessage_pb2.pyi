"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.internal.extension_dict
import google.protobuf.message
import pyatv.protocols.mrp.protobuf.ProtocolMessage_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class KeyboardState(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Enum:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _EnumEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[KeyboardState._Enum.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        Unknown: KeyboardState._Enum.ValueType  # 0
        NotEditing: KeyboardState._Enum.ValueType  # 1
        DidBeginEditing: KeyboardState._Enum.ValueType  # 2
        Editing: KeyboardState._Enum.ValueType  # 3
        TextDidChange: KeyboardState._Enum.ValueType  # 4
        DidEndEditing: KeyboardState._Enum.ValueType  # 5
        Response: KeyboardState._Enum.ValueType  # 6

    class Enum(_Enum, metaclass=_EnumEnumTypeWrapper): ...
    Unknown: KeyboardState.Enum.ValueType  # 0
    NotEditing: KeyboardState.Enum.ValueType  # 1
    DidBeginEditing: KeyboardState.Enum.ValueType  # 2
    Editing: KeyboardState.Enum.ValueType  # 3
    TextDidChange: KeyboardState.Enum.ValueType  # 4
    DidEndEditing: KeyboardState.Enum.ValueType  # 5
    Response: KeyboardState.Enum.ValueType  # 6

    def __init__(
        self,
    ) -> None: ...

global___KeyboardState = KeyboardState

@typing_extensions.final
class AutocapitalizationType(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Enum:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _EnumEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[AutocapitalizationType._Enum.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        Words: AutocapitalizationType._Enum.ValueType  # 1
        Sentences: AutocapitalizationType._Enum.ValueType  # 2
        AllCharacters: AutocapitalizationType._Enum.ValueType  # 3

    class Enum(_Enum, metaclass=_EnumEnumTypeWrapper): ...
    Words: AutocapitalizationType.Enum.ValueType  # 1
    Sentences: AutocapitalizationType.Enum.ValueType  # 2
    AllCharacters: AutocapitalizationType.Enum.ValueType  # 3

    def __init__(
        self,
    ) -> None: ...

global___AutocapitalizationType = AutocapitalizationType

@typing_extensions.final
class KeyboardType(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Enum:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _EnumEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[KeyboardType._Enum.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        Default: KeyboardType._Enum.ValueType  # 0
        ASCII_Capable: KeyboardType._Enum.ValueType  # 1
        NumbersAndPunctuation: KeyboardType._Enum.ValueType  # 2
        URL: KeyboardType._Enum.ValueType  # 3
        NumberPad: KeyboardType._Enum.ValueType  # 4
        PhonePad: KeyboardType._Enum.ValueType  # 5
        NamePhonePad: KeyboardType._Enum.ValueType  # 6
        EmailAddress: KeyboardType._Enum.ValueType  # 7
        DecimalPad: KeyboardType._Enum.ValueType  # 8
        Twitter: KeyboardType._Enum.ValueType  # 9
        WebSearch: KeyboardType._Enum.ValueType  # 10
        Alphanet: KeyboardType._Enum.ValueType  # 11
        PasscodePad: KeyboardType._Enum.ValueType  # 12

    class Enum(_Enum, metaclass=_EnumEnumTypeWrapper): ...
    Default: KeyboardType.Enum.ValueType  # 0
    ASCII_Capable: KeyboardType.Enum.ValueType  # 1
    NumbersAndPunctuation: KeyboardType.Enum.ValueType  # 2
    URL: KeyboardType.Enum.ValueType  # 3
    NumberPad: KeyboardType.Enum.ValueType  # 4
    PhonePad: KeyboardType.Enum.ValueType  # 5
    NamePhonePad: KeyboardType.Enum.ValueType  # 6
    EmailAddress: KeyboardType.Enum.ValueType  # 7
    DecimalPad: KeyboardType.Enum.ValueType  # 8
    Twitter: KeyboardType.Enum.ValueType  # 9
    WebSearch: KeyboardType.Enum.ValueType  # 10
    Alphanet: KeyboardType.Enum.ValueType  # 11
    PasscodePad: KeyboardType.Enum.ValueType  # 12

    def __init__(
        self,
    ) -> None: ...

global___KeyboardType = KeyboardType

@typing_extensions.final
class ReturnKeyType(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Enum:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _EnumEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[ReturnKeyType._Enum.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        Default: ReturnKeyType._Enum.ValueType  # 0
        Go: ReturnKeyType._Enum.ValueType  # 1
        Google: ReturnKeyType._Enum.ValueType  # 2
        Join: ReturnKeyType._Enum.ValueType  # 3
        Next: ReturnKeyType._Enum.ValueType  # 4
        Route: ReturnKeyType._Enum.ValueType  # 5
        Search: ReturnKeyType._Enum.ValueType  # 6
        Send: ReturnKeyType._Enum.ValueType  # 7
        Yahoo: ReturnKeyType._Enum.ValueType  # 8
        Done: ReturnKeyType._Enum.ValueType  # 9
        EmergencyCall: ReturnKeyType._Enum.ValueType  # 10
        Continue: ReturnKeyType._Enum.ValueType  # 11

    class Enum(_Enum, metaclass=_EnumEnumTypeWrapper): ...
    Default: ReturnKeyType.Enum.ValueType  # 0
    Go: ReturnKeyType.Enum.ValueType  # 1
    Google: ReturnKeyType.Enum.ValueType  # 2
    Join: ReturnKeyType.Enum.ValueType  # 3
    Next: ReturnKeyType.Enum.ValueType  # 4
    Route: ReturnKeyType.Enum.ValueType  # 5
    Search: ReturnKeyType.Enum.ValueType  # 6
    Send: ReturnKeyType.Enum.ValueType  # 7
    Yahoo: ReturnKeyType.Enum.ValueType  # 8
    Done: ReturnKeyType.Enum.ValueType  # 9
    EmergencyCall: ReturnKeyType.Enum.ValueType  # 10
    Continue: ReturnKeyType.Enum.ValueType  # 11

    def __init__(
        self,
    ) -> None: ...

global___ReturnKeyType = ReturnKeyType

@typing_extensions.final
class TextInputTraits(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AUTOCAPITALIZATIONTYPE_FIELD_NUMBER: builtins.int
    KEYBOARDTYPE_FIELD_NUMBER: builtins.int
    RETURNKEYTYPE_FIELD_NUMBER: builtins.int
    AUTOCORRECTION_FIELD_NUMBER: builtins.int
    SPELLCHECKING_FIELD_NUMBER: builtins.int
    ENABLESRETURNKEYAUTOMATICALLY_FIELD_NUMBER: builtins.int
    SECURETEXTENTRY_FIELD_NUMBER: builtins.int
    VALIDTEXTRANGELOCATION_FIELD_NUMBER: builtins.int
    VALIDTEXTRANGELENGTH_FIELD_NUMBER: builtins.int
    PINENTRYSEPARATORINDEXES_FIELD_NUMBER: builtins.int
    autocapitalizationType: global___AutocapitalizationType.Enum.ValueType
    keyboardType: global___KeyboardType.Enum.ValueType
    returnKeyType: global___ReturnKeyType.Enum.ValueType
    autocorrection: builtins.bool
    spellchecking: builtins.bool
    enablesReturnKeyAutomatically: builtins.bool
    secureTextEntry: builtins.bool
    validTextRangeLocation: builtins.int
    validTextRangeLength: builtins.int
    @property
    def pINEntrySeparatorIndexes(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    def __init__(
        self,
        *,
        autocapitalizationType: global___AutocapitalizationType.Enum.ValueType | None = ...,
        keyboardType: global___KeyboardType.Enum.ValueType | None = ...,
        returnKeyType: global___ReturnKeyType.Enum.ValueType | None = ...,
        autocorrection: builtins.bool | None = ...,
        spellchecking: builtins.bool | None = ...,
        enablesReturnKeyAutomatically: builtins.bool | None = ...,
        secureTextEntry: builtins.bool | None = ...,
        validTextRangeLocation: builtins.int | None = ...,
        validTextRangeLength: builtins.int | None = ...,
        pINEntrySeparatorIndexes: collections.abc.Iterable[builtins.int] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["autocapitalizationType", b"autocapitalizationType", "autocorrection", b"autocorrection", "enablesReturnKeyAutomatically", b"enablesReturnKeyAutomatically", "keyboardType", b"keyboardType", "returnKeyType", b"returnKeyType", "secureTextEntry", b"secureTextEntry", "spellchecking", b"spellchecking", "validTextRangeLength", b"validTextRangeLength", "validTextRangeLocation", b"validTextRangeLocation"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["autocapitalizationType", b"autocapitalizationType", "autocorrection", b"autocorrection", "enablesReturnKeyAutomatically", b"enablesReturnKeyAutomatically", "keyboardType", b"keyboardType", "pINEntrySeparatorIndexes", b"pINEntrySeparatorIndexes", "returnKeyType", b"returnKeyType", "secureTextEntry", b"secureTextEntry", "spellchecking", b"spellchecking", "validTextRangeLength", b"validTextRangeLength", "validTextRangeLocation", b"validTextRangeLocation"]) -> None: ...

global___TextInputTraits = TextInputTraits

@typing_extensions.final
class TextEditingAttributes(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TITLE_FIELD_NUMBER: builtins.int
    PROMPT_FIELD_NUMBER: builtins.int
    INPUTTRAITS_FIELD_NUMBER: builtins.int
    title: builtins.str
    prompt: builtins.str
    @property
    def inputTraits(self) -> global___TextInputTraits: ...
    def __init__(
        self,
        *,
        title: builtins.str | None = ...,
        prompt: builtins.str | None = ...,
        inputTraits: global___TextInputTraits | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["inputTraits", b"inputTraits", "prompt", b"prompt", "title", b"title"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["inputTraits", b"inputTraits", "prompt", b"prompt", "title", b"title"]) -> None: ...

global___TextEditingAttributes = TextEditingAttributes

@typing_extensions.final
class KeyboardMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STATE_FIELD_NUMBER: builtins.int
    ATTRIBUTES_FIELD_NUMBER: builtins.int
    ENCRYPTEDTEXTCYPHERTEXT_FIELD_NUMBER: builtins.int
    state: global___KeyboardState.Enum.ValueType
    @property
    def attributes(self) -> global___TextEditingAttributes: ...
    encryptedTextCyphertext: builtins.bytes
    def __init__(
        self,
        *,
        state: global___KeyboardState.Enum.ValueType | None = ...,
        attributes: global___TextEditingAttributes | None = ...,
        encryptedTextCyphertext: builtins.bytes | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["attributes", b"attributes", "encryptedTextCyphertext", b"encryptedTextCyphertext", "state", b"state"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["attributes", b"attributes", "encryptedTextCyphertext", b"encryptedTextCyphertext", "state", b"state"]) -> None: ...

global___KeyboardMessage = KeyboardMessage

KEYBOARDMESSAGE_FIELD_NUMBER: builtins.int
keyboardMessage: google.protobuf.internal.extension_dict._ExtensionFieldDescriptor[pyatv.protocols.mrp.protobuf.ProtocolMessage_pb2.ProtocolMessage, global___KeyboardMessage]