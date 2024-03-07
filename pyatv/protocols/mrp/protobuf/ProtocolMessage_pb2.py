# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyatv/protocols/mrp/protobuf/ProtocolMessage.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2pyatv/protocols/mrp/protobuf/ProtocolMessage.proto\"\xe1\x14\n\tErrorCode\"\xd3\x14\n\x04\x45num\x12\x0b\n\x07NoError\x10\x00\x12\x10\n\x0cUnknownError\x10\x01\x12\x14\n\x10InvalidOperation\x10\x02\x12\x19\n\x15OperationNotPermitted\x10\x03\x12\x16\n\x12\x43lientDoesNotExist\x10\x04\x12\x16\n\x12OriginDoesNotExist\x10\x05\x12\x18\n\x14UnsupportedOperation\x10\x06\x12\x1a\n\x16\x46\x61iledToSetPickedRoute\x10\x07\x12 \n\x1c\x46\x61iledToRegisterCustomOrigin\x10\x08\x12\x1e\n\x1a\x46\x61iledToRemoveCustomOrigin\x10\t\x12&\n\"TheApplicationActivityDoesNotExist\x10\n\x12.\n*TheAppHasNotSetupABrowsableContentEndpoint\x10\x0b\x12\x41\n=TheRequestedBrowsableContentApiIsNotSupportedByTheApplication\x10\x0c\x12\x32\n.TheNotficationHasNotBeenWhitelistedByTheServer\x10\r\x12\x38\n4OperationRequiresAClientCallbackToHaveBeenRegistered\x10\x0e\x12:\n6OperationRequiresAClientDataSourceToHaveBeenRegistered\x10\x0f\x12\x35\n1RequestedDataIsOutOfDateAndShouldBeRequestedAgain\x10\x10\x12\x30\n,TheDevicesEnforcedVolumeLimitHasBeenExceeded\x10\x11\x12\x1b\n\x17VolumeValueIsOutOfRange\x10\x12\x12$\n VolumeIsAlreadyAtTheMaximumValue\x10\x13\x12\x18\n\x14VolumeIsAlreadyMuted\x10\x14\x12\"\n\x1eVoiceInputEndpointDoesNotExist\x10\x15\x12\x34\n0TheVoiceInputDeviceIsNotRegisteredOrDoesNotExist\x10\x16\x12\x15\n\x11\x45ncryptionFailure\x10\x17\x12\x18\n\x14\x45ndpointDoesNotExist\x10\x18\x12.\n*TheClientsApplicationCancelledTheOperation\x10\x19\x12\x18\n\x14TheOperationTimedOut\x10\x1a\x12*\n&TheSpecifiedPlayerPathObjectWasInvalid\x10\x1b\x12:\n6AddingOrRemovingDevicesFromTheAvOutputContextHasFailed\x10\x1c\x12,\n(CouldNotFindTheSpecifiedNowPlayingPlayer\x10\x1d\x12\'\n#TheSpecifiedContentItemDoesNotExist\x10\x1e\x12\x1f\n\x1bTheSpecifiedOffsetIsInvalid\x10\x1f\x12&\n\"TheSpecifiedOutputContextIsInvalid\x10 \x12\x32\n.OneOrMoreSpecifiedOutputDevicesAreNotGroupable\x10!\x12H\nDTheSpecifiedOutputContextDoesNotSupportAddingMoreThanOneOutputDevice\x10\"\x12,\n(CouldNotFindTheSpecifiedNowPlayingClient\x10#\x12P\nLEndpointVolumeControlIsOnlyPossibleIfTheEndpointIsPickedOrRemoteControllable\x10$\x12T\nPOutputDeviceVolumeControlIsOnlyPossibleIfTheEndpointIsPickedOrRemoteControllable\x10%\x12\"\n\x1e\x43oderMustSupportKeyValueCoding\x10&\x12$\n CouldNotFindTheGivenOutputdevice\x10\'\x12!\n\x1d\x46\x61iledToConnectToRemoteDevice\x10\x64\x12 \n\x1c\x41uthenticationTokenIsInvalid\x10\x65\x12\x33\n/RecordingSessionIsAlreadyInProgressOnThisDevice\x10\x66\x12$\n TheDeviceIsNotCurrentlyRecording\x10g\x12\x1c\n\x18TheClientHasDisconnected\x10h\x12\x1c\n\x18TheServerHasDisconnected\x10i\x12,\n(TheConnectionHasBeenCancelledByTheClient\x10j\x12\x34\n0PairingFunctionalityIsLockedDueToSecurityReasons\x10k\x12,\n(TheClientsOperatingSystemVersionIsTooOld\x10l\x12(\n$TheClientsApplicationVersionIsTooOld\x10m\x12\x18\n\x14TheDeviceIsNotPaired\x10n\x12?\n;ThePinPairingDialogWasRemovedByTheUserBeforePairingOccoured\x10o\x12@\n<ThePinPairingDialogWasRemovedByATimeoutBeforePairingOccoured\x10p\x12\x19\n\x15TheConnectionTimedout\x10q\x12\"\n\x1ePairingWithThisDeviceIsBlocked\x10r\x12\x1b\n\x17TheDeviceIsGoingToSleep\x10s\x12\x1d\n\x19\x43onnectionBlockedByServer\x10t\x12<\n8MravendpointWasDeallocatedWhileWaitingForDeviceToConnect\x10u\x12H\nCOutputContextModificationCausedADeviceToNoLongerBeAProxyGroupPlayer\x10\xc8\x01\x12\x44\n?OutputContextModificationCausedADeviceToBecomeAProxyGroupPlayer\x10\xc9\x01\x12\x37\n2OutputContextModificationRequestedNoTopologyChange\x10\xca\x01\x12\x16\n\x11OtherUnknownError\x10\xab\x02\"\xc0\x18\n\x0fProtocolMessage\x12#\n\x04type\x18\x01 \x01(\x0e\x32\x15.ProtocolMessage.Type\x12\x12\n\nidentifier\x18\x02 \x01(\t\x12\x1b\n\x13\x61uthenticationToken\x18\x03 \x01(\t\x12\"\n\terrorCode\x18\x04 \x01(\x0e\x32\x0f.ErrorCode.Enum\x12\x11\n\ttimestamp\x18\x05 \x01(\x04\x12\x18\n\x10\x65rrorDescription\x18N \x01(\t\x12\x18\n\x10uniqueIdentifier\x18U \x01(\t\"\xd5\x16\n\x04Type\x12\x13\n\x0fUNKNOWN_MESSAGE\x10\x00\x12\x18\n\x14SEND_COMMAND_MESSAGE\x10\x01\x12\x1f\n\x1bSEND_COMMAND_RESULT_MESSAGE\x10\x02\x12\x15\n\x11GET_STATE_MESSAGE\x10\x03\x12\x15\n\x11SET_STATE_MESSAGE\x10\x04\x12\x17\n\x13SET_ARTWORK_MESSAGE\x10\x05\x12\x1f\n\x1bREGISTER_HID_DEVICE_MESSAGE\x10\x06\x12&\n\"REGISTER_HID_DEVICE_RESULT_MESSAGE\x10\x07\x12\x1a\n\x16SEND_HID_EVENT_MESSAGE\x10\x08\x12\x1b\n\x17SEND_HID_REPORT_MESSAGE\x10\t\x12$\n SEND_VIRTUAL_TOUCH_EVENT_MESSAGE\x10\n\x12\x18\n\x14NOTIFICATION_MESSAGE\x10\x0b\x12.\n*CONTENT_ITEMS_CHANGED_NOTIFICATION_MESSAGE\x10\x0c\x12\x17\n\x13\x44\x45VICE_INFO_MESSAGE\x10\x0f\x12!\n\x1d\x43LIENT_UPDATES_CONFIG_MESSAGE\x10\x10\x12\'\n#VOLUME_CONTROL_AVAILABILITY_MESSAGE\x10\x11\x12\x1b\n\x17GAME_CONTROLLER_MESSAGE\x10\x12\x12$\n REGISTER_GAME_CONTROLLER_MESSAGE\x10\x13\x12-\n)REGISTER_GAME_CONTROLLER_RESPONSE_MESSAGE\x10\x14\x12&\n\"UNREGISTER_GAME_CONTROLLER_MESSAGE\x10\x15\x12/\n+REGISTER_FOR_GAME_CONTROLLER_EVENTS_MESSAGE\x10\x16\x12\x14\n\x10KEYBOARD_MESSAGE\x10\x17\x12 \n\x1cGET_KEYBOARD_SESSION_MESSAGE\x10\x18\x12\x16\n\x12TEXT_INPUT_MESSAGE\x10\x19\x12#\n\x1fGET_VOICE_INPUT_DEVICES_MESSAGE\x10\x1a\x12,\n(GET_VOICE_INPUT_DEVICES_RESPONSE_MESSAGE\x10\x1b\x12\'\n#REGISTER_VOICE_INPUT_DEVICE_MESSAGE\x10\x1c\x12\x30\n,REGISTER_VOICE_INPUT_DEVICE_RESPONSE_MESSAGE\x10\x1d\x12\x1f\n\x1bSET_RECORDING_STATE_MESSAGE\x10\x1e\x12\x1c\n\x18SEND_VOICE_INPUT_MESSAGE\x10\x1f\x12\"\n\x1ePLAYBACK_QUEUE_REQUEST_MESSAGE\x10 \x12\x17\n\x13TRANSACTION_MESSAGE\x10!\x12\x1a\n\x16\x43RYPTO_PAIRING_MESSAGE\x10\"\x12&\n\"GAME_CONTROLLER_PROPERTIES_MESSAGE\x10#\x12\x1b\n\x17SET_READY_STATE_MESSAGE\x10$\x12\x1e\n\x1a\x44\x45VICE_INFO_UPDATE_MESSAGE\x10%\x12 \n\x1cSET_CONNECTION_STATE_MESSAGE\x10&\x12\x1d\n\x19SEND_BUTTON_EVENT_MESSAGE\x10\'\x12\x1b\n\x17SET_HILITE_MODE_MESSAGE\x10(\x12\x17\n\x13WAKE_DEVICE_MESSAGE\x10)\x12\x13\n\x0fGENERIC_MESSAGE\x10*\x12+\n\'SEND_PACKED_VIRTUAL_TOUCH_EVENT_MESSAGE\x10+\x12\x15\n\x11SEND_LYRICS_EVENT\x10,\x12\"\n\x1eSET_NOW_PLAYING_CLIENT_MESSAGE\x10.\x12\"\n\x1eSET_NOW_PLAYING_PLAYER_MESSAGE\x10/\x12)\n%MODIFY_OUTPUT_CONTEXT_REQUEST_MESSAGE\x10\x30\x12\x16\n\x12GET_VOLUME_MESSAGE\x10\x31\x12\x1d\n\x19GET_VOLUME_RESULT_MESSAGE\x10\x32\x12\x16\n\x12SET_VOLUME_MESSAGE\x10\x33\x12\x1d\n\x19VOLUME_DID_CHANGE_MESSAGE\x10\x34\x12\x19\n\x15REMOVE_CLIENT_MESSAGE\x10\x35\x12\x19\n\x15REMOVE_PLAYER_MESSAGE\x10\x36\x12\x19\n\x15UPDATE_CLIENT_MESSAGE\x10\x37\x12\x1f\n\x1bUPDATE_CONTENT_ITEM_MESSAGE\x10\x38\x12\'\n#UPDATE_CONTENT_ITEM_ARTWORK_MESSAGE\x10\x39\x12\x19\n\x15UPDATE_PLAYER_MESSAGE\x10:\x12*\n&PROMPT_FOR_ROUTE_AUTHORIZATION_MESSAGE\x10;\x12\x33\n/PROMPT_FOR_ROUTE_AUTHORIZATION_RESPONSE_MESSAGE\x10<\x12.\n*PRESENT_ROUTE_AUTHORIZATION_STATUS_MESSAGE\x10=\x12+\n\'GET_VOLUME_CONTROL_CAPABILITIES_MESSAGE\x10>\x12\x32\n.GET_VOLUME_CONTROL_CAPABILITIES_RESULT_MESSAGE\x10?\x12\x32\n.VOLUME_CONTROL_CAPABILITIES_DID_CHANGE_MESSAGE\x10@\x12 \n\x1cUPDATE_OUTPUT_DEVICE_MESSAGE\x10\x41\x12!\n\x1dREMOVE_OUTPUT_DEVICES_MESSAGE\x10\x42\x12\x1d\n\x19REMOTE_TEXT_INPUT_MESSAGE\x10\x43\x12)\n%GET_REMOTE_TEXT_INPUT_SESSION_MESSAGE\x10\x44\x12\"\n\x1eREMOVE_OUTPUT_DEVICES_MESSAGE2\x10\x45\x12$\n PLAYBACK_SESSION_REQUEST_MESSAGE\x10\x46\x12%\n!PLAYBACK_SESSION_RESPONSE_MESSAGE\x10G\x12*\n&SET_DEFAULT_SUPPORTED_COMMANDS_MESSAGE\x10H\x12,\n(PLAYBACK_SESSION_MIGRATE_REQUEST_MESSAGE\x10I\x12-\n)PLAYBACK_SESSION_MIGRATE_RESPONSE_MESSAGE\x10J\x12*\n&PLAYBACK_SESSION_MIGRATE_BEGIN_MESSAGE\x10K\x12(\n$PLAYBACK_SESSION_MIGRATE_END_MESSAGE\x10L\x12)\n%UPDATE_ACTIVE_SYSTEM_ENDPOINT_MESSAGE\x10M\x12\x1e\n\x1aSET_DISCOVERY_MODE_MESSAGE\x10\x65\x12\x1d\n\x19UPDATE_END_POINTS_MESSAGE\x10\x66\x12\x1c\n\x18REMOVE_ENDPOINTS_MESSAGE\x10g\x12$\n PLAYER_CLIENT_PROPERTIES_MESSAGE\x10h\x12$\n ORIGIN_CLIENT_PROPERTIES_MESSAGE\x10i\x12\x16\n\x12\x41UDIO_FADE_MESSAGE\x10j\x12\x1f\n\x1b\x41UDIO_FADE_RESPONSE_MESSAGE\x10k\x12 \n\x1c\x43ONFIGURE_CONNECTION_MESSAGE\x10x*\x04\x08\x06\x10N*\x04\x08O\x10U*\x08\x08V\x10\x80\x80\x80\x80\x02')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pyatv.protocols.mrp.protobuf.ProtocolMessage_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_ERRORCODE']._serialized_start=55
  _globals['_ERRORCODE']._serialized_end=2712
  _globals['_ERRORCODE_ENUM']._serialized_start=69
  _globals['_ERRORCODE_ENUM']._serialized_end=2712
  _globals['_PROTOCOLMESSAGE']._serialized_start=2715
  _globals['_PROTOCOLMESSAGE']._serialized_end=5851
  _globals['_PROTOCOLMESSAGE_TYPE']._serialized_start=2928
  _globals['_PROTOCOLMESSAGE_TYPE']._serialized_end=5829
# @@protoc_insertion_point(module_scope)