# -*- coding: utf-8 -*-

"""
    ytelapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class Body32(object):

    """Implementation of the 'body_32' model.

    TODO: type model description here.

    Attributes:
        offset (string): The starting point of the list of spam emails that
            should be returned.
        limit (string): The count of results that should be returned.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "offset":'Offset',
        "limit":'Limit'
    }

    def __init__(self,
                 offset=None,
                 limit=None):
        """Constructor for the Body32 class"""

        # Initialize members of the class
        self.offset = offset
        self.limit = limit


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
        offset = dictionary.get('Offset')
        limit = dictionary.get('Limit')

        # Return an object of this model
        return cls(offset,
                   limit)


