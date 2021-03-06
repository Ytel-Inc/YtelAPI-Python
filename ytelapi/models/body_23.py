# -*- coding: utf-8 -*-

"""
    ytelapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class Body23(object):

    """Implementation of the 'body_23' model.

    TODO: type model description here.

    Attributes:
        call_sid (string): The unique identifier of each call resource
        record (bool): Set true to initiate recording or false to terminate
            recording
        direction (DirectionEnum): The leg of the call to record
        time_limit (int): Time in seconds the recording duration should not
            exceed
        call_back_url (string): URL consulted after the recording completes
        fileformat (FileformatEnum): Format of the recording file. Can be .mp3
            or .wav

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "call_sid":'CallSid',
        "record":'Record',
        "direction":'Direction',
        "time_limit":'TimeLimit',
        "call_back_url":'CallBackUrl',
        "fileformat":'Fileformat'
    }

    def __init__(self,
                 call_sid=None,
                 record=None,
                 direction=None,
                 time_limit=None,
                 call_back_url=None,
                 fileformat=None):
        """Constructor for the Body23 class"""

        # Initialize members of the class
        self.call_sid = call_sid
        self.record = record
        self.direction = direction
        self.time_limit = time_limit
        self.call_back_url = call_back_url
        self.fileformat = fileformat


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
        call_sid = dictionary.get('CallSid')
        record = dictionary.get('Record')
        direction = dictionary.get('Direction')
        time_limit = dictionary.get('TimeLimit')
        call_back_url = dictionary.get('CallBackUrl')
        fileformat = dictionary.get('Fileformat')

        # Return an object of this model
        return cls(call_sid,
                   record,
                   direction,
                   time_limit,
                   call_back_url,
                   fileformat)


