# -*- coding: utf-8 -*-

"""
    ytelapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class Body69(object):

    """Implementation of the 'body_69' model.

    TODO: type model description here.

    Attributes:
        message_sid (string): The unique identifier for a sms message.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "message_sid":'MessageSid'
    }

    def __init__(self,
                 message_sid=None):
        """Constructor for the Body69 class"""

        # Initialize members of the class
        self.message_sid = message_sid


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
        message_sid = dictionary.get('MessageSid')

        # Return an object of this model
        return cls(message_sid)

