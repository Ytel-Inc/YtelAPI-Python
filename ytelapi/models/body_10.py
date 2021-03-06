# -*- coding: utf-8 -*-

"""
    ytelapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class Body10(object):

    """Implementation of the 'body_10' model.

    TODO: type model description here.

    Attributes:
        recording_sid (string): The unique identifier for a recording object.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "recording_sid":'recordingSid'
    }

    def __init__(self,
                 recording_sid=None):
        """Constructor for the Body10 class"""

        # Initialize members of the class
        self.recording_sid = recording_sid


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
        recording_sid = dictionary.get('recordingSid')

        # Return an object of this model
        return cls(recording_sid)


