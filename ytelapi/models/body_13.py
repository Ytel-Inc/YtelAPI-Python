# -*- coding: utf-8 -*-

"""
    ytelapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class Body13(object):

    """Implementation of the 'body_13' model.

    TODO: type model description here.

    Attributes:
        recordingsid (string): The unique identifier for a recording.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "recordingsid":'recordingsid'
    }

    def __init__(self,
                 recordingsid=None):
        """Constructor for the Body13 class"""

        # Initialize members of the class
        self.recordingsid = recordingsid


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
        recordingsid = dictionary.get('recordingsid')

        # Return an object of this model
        return cls(recordingsid)

