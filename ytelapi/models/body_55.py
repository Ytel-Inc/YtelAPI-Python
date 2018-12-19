# -*- coding: utf-8 -*-

"""
    ytelapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class Body55(object):

    """Implementation of the 'body_55' model.

    TODO: type model description here.

    Attributes:
        mfrom (string): A valid 10-digit number (E.164 format) that will be
            initiating the conference call.
        to (string): A valid 10-digit number (E.164 format) that is to receive
            the conference call.
        method (string): Specifies the HTTP method used to request the
            required URL once call connects.
        status_call_back_url (string): URL that can be requested to receive
            notification when call has ended. A set of default parameters will
            be sent here once the conference is finished.
        status_call_back_method (string): Specifies the HTTP methodlinkclass
            used to request StatusCallbackUrl.
        fallback_url (string): URL requested if the initial Url parameter
            fails or encounters an error
        fallback_method (string): Specifies the HTTP method used to request
            the required FallbackUrl once call connects.
        record (bool): Specifies if the conference should be recorded.
        record_call_back_url (string): Recording parameters will be sent here
            upon completion.
        record_call_back_method (string): Specifies the HTTP method used to
            request the required URL once conference connects.
        schedule_time (string): Schedule conference in future. Schedule time
            must be greater than current time
        timeout (int): The number of seconds the call stays on the line while
            waiting for an answer. The max time limit is 999 and the default
            limit is 60 seconds but lower times can be set.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mfrom":'From',
        "to":'To',
        "method":'Method',
        "status_call_back_url":'StatusCallBackUrl',
        "status_call_back_method":'StatusCallBackMethod',
        "fallback_url":'FallbackUrl',
        "fallback_method":'FallbackMethod',
        "record":'Record',
        "record_call_back_url":'RecordCallBackUrl',
        "record_call_back_method":'RecordCallBackMethod',
        "schedule_time":'ScheduleTime',
        "timeout":'Timeout'
    }

    def __init__(self,
                 mfrom=None,
                 to=None,
                 method=None,
                 status_call_back_url=None,
                 status_call_back_method=None,
                 fallback_url=None,
                 fallback_method=None,
                 record=None,
                 record_call_back_url=None,
                 record_call_back_method=None,
                 schedule_time=None,
                 timeout=None):
        """Constructor for the Body55 class"""

        # Initialize members of the class
        self.mfrom = mfrom
        self.to = to
        self.method = method
        self.status_call_back_url = status_call_back_url
        self.status_call_back_method = status_call_back_method
        self.fallback_url = fallback_url
        self.fallback_method = fallback_method
        self.record = record
        self.record_call_back_url = record_call_back_url
        self.record_call_back_method = record_call_back_method
        self.schedule_time = schedule_time
        self.timeout = timeout


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
        mfrom = dictionary.get('From')
        to = dictionary.get('To')
        method = dictionary.get('Method')
        status_call_back_url = dictionary.get('StatusCallBackUrl')
        status_call_back_method = dictionary.get('StatusCallBackMethod')
        fallback_url = dictionary.get('FallbackUrl')
        fallback_method = dictionary.get('FallbackMethod')
        record = dictionary.get('Record')
        record_call_back_url = dictionary.get('RecordCallBackUrl')
        record_call_back_method = dictionary.get('RecordCallBackMethod')
        schedule_time = dictionary.get('ScheduleTime')
        timeout = dictionary.get('Timeout')

        # Return an object of this model
        return cls(mfrom,
                   to,
                   method,
                   status_call_back_url,
                   status_call_back_method,
                   fallback_url,
                   fallback_method,
                   record,
                   record_call_back_url,
                   record_call_back_method,
                   schedule_time,
                   timeout)

