# -*- coding: utf-8 -*-

"""
    ytelapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class Body47(object):

    """Implementation of the 'body_47' model.

    TODO: type model description here.

    Attributes:
        phone_number (string): A valid Ytel number (E.164 format).
        voice_url (string): URL requested once the call connects
        friendly_name (string): Phone number friendly name description
        voice_method (string): Post or Get
        voice_fallback_url (string): URL requested if the voice URL is not
            available
        voice_fallback_method (string): Post or Get
        hangup_callback (string): callback url after a hangup occurs
        hangup_callback_method (string): Post or Get
        heartbeat_url (string): URL requested once the call connects
        heartbeat_method (string): URL that can be requested every 60 seconds
            during the call to notify of elapsed time
        sms_url (string): URL requested when an SMS is received
        sms_method (string): Post or Get
        sms_fallback_url (string): URL used if any errors occur during
            execution of InboundXML from an SMS or at initial request of the
            SmsUrl.
        sms_fallback_method (string): The HTTP method Ytel will use when URL
            requested if the SmsUrl is not available.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "phone_number":'PhoneNumber',
        "voice_url":'VoiceUrl',
        "friendly_name":'FriendlyName',
        "voice_method":'VoiceMethod',
        "voice_fallback_url":'VoiceFallbackUrl',
        "voice_fallback_method":'VoiceFallbackMethod',
        "hangup_callback":'HangupCallback',
        "hangup_callback_method":'HangupCallbackMethod',
        "heartbeat_url":'HeartbeatUrl',
        "heartbeat_method":'HeartbeatMethod',
        "sms_url":'SmsUrl',
        "sms_method":'SmsMethod',
        "sms_fallback_url":'SmsFallbackUrl',
        "sms_fallback_method":'SmsFallbackMethod'
    }

    def __init__(self,
                 phone_number=None,
                 voice_url=None,
                 friendly_name=None,
                 voice_method=None,
                 voice_fallback_url=None,
                 voice_fallback_method=None,
                 hangup_callback=None,
                 hangup_callback_method=None,
                 heartbeat_url=None,
                 heartbeat_method=None,
                 sms_url=None,
                 sms_method=None,
                 sms_fallback_url=None,
                 sms_fallback_method=None):
        """Constructor for the Body47 class"""

        # Initialize members of the class
        self.phone_number = phone_number
        self.voice_url = voice_url
        self.friendly_name = friendly_name
        self.voice_method = voice_method
        self.voice_fallback_url = voice_fallback_url
        self.voice_fallback_method = voice_fallback_method
        self.hangup_callback = hangup_callback
        self.hangup_callback_method = hangup_callback_method
        self.heartbeat_url = heartbeat_url
        self.heartbeat_method = heartbeat_method
        self.sms_url = sms_url
        self.sms_method = sms_method
        self.sms_fallback_url = sms_fallback_url
        self.sms_fallback_method = sms_fallback_method


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        phone_number = dictionary.get('PhoneNumber')
        voice_url = dictionary.get('VoiceUrl')
        friendly_name = dictionary.get('FriendlyName')
        voice_method = dictionary.get('VoiceMethod')
        voice_fallback_url = dictionary.get('VoiceFallbackUrl')
        voice_fallback_method = dictionary.get('VoiceFallbackMethod')
        hangup_callback = dictionary.get('HangupCallback')
        hangup_callback_method = dictionary.get('HangupCallbackMethod')
        heartbeat_url = dictionary.get('HeartbeatUrl')
        heartbeat_method = dictionary.get('HeartbeatMethod')
        sms_url = dictionary.get('SmsUrl')
        sms_method = dictionary.get('SmsMethod')
        sms_fallback_url = dictionary.get('SmsFallbackUrl')
        sms_fallback_method = dictionary.get('SmsFallbackMethod')

        # Return an object of this model
        return cls(phone_number,
                   voice_url,
                   friendly_name,
                   voice_method,
                   voice_fallback_url,
                   voice_fallback_method,
                   hangup_callback,
                   hangup_callback_method,
                   heartbeat_url,
                   heartbeat_method,
                   sms_url,
                   sms_method,
                   sms_fallback_url,
                   sms_fallback_method)


